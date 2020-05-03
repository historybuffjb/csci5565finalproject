""" Converts a specific json file into a pov file """
import sys
from pathlib import Path
from json import load


class PovConverter:
    """ Converts json to pov """

    def __init__(self, json_path):
        self.json_path = json_path
        self._json_data = None
        self._final_file_format = ""

    def convert_pov(self):
        """ Converts to pov """
        with open(self.json_path, "r") as json_file:
            self._json_data = load(json_file)
        self._generate_global_settings()
        self._generate_light_source()
        self._generate_camera()
        self._generate_background()
        self._generate_plane()
        self._generate_mesh()
        self._generate_object()

    def _generate_global_settings(self):
        """ Generates global settings for pov file """
        self._final_file_format += """
#version 3.5

global_settings {
    assumed_gamma 1
}
        """

    def _generate_light_source(self):
        """ Generates light source for pov file """
        self._final_file_format += """
light_source {
    <200, 200, 200>*10000
    rgb 1.3
}
        """

    # pylint: disable=R0914
    def _generate_camera(self):
        """ Generates a camera for pov file """
        values = self._json_data["POINTARRAY"]
        multiplier = 4
        max_x = ~sys.maxsize
        max_y = ~sys.maxsize
        max_z = ~sys.maxsize
        min_x = sys.maxsize
        min_y = sys.maxsize
        min_z = sys.maxsize
        for value in values:
            if value["maxx"] > max_x:
                max_x = value["maxx"]
            if value["minx"] < min_x:
                min_x = value["minx"]
            if value["maxy"] > max_y:
                max_y = value["maxy"]
            if value["miny"] < min_y:
                min_y = value["miny"]
            if value["maxz"] > max_z:
                max_z = value["maxz"]
            if value["minz"] < min_z:
                min_z = value["minz"]
        location_x = (abs(min_x) + abs(max_x)) * multiplier
        location_y = (abs(min_y) + abs(max_y)) * multiplier
        location_z = (abs(min_z) + abs(max_z)) * multiplier
        values = self._json_data["MESHMATRIX"]
        min_lookat_x = sys.maxsize
        min_lookat_y = sys.maxsize
        min_lookat_z = sys.maxsize
        for value in values:
            if value["center"][0] < min_lookat_x:
                min_lookat_x = value["center"][0]
            if value["center"][1] < min_lookat_y:
                min_lookat_y = value["center"][1]
            if value["center"][2] < min_lookat_z:
                min_lookat_z = value["center"][2]
        location = f"<{location_x}, {location_y}, {location_z}>"
        self._final_file_format += f"""
camera {{
  location    {location}
  direction   y
  sky         z
  up          z
  right       (4/3)*x
  look_at     <0, 0, 0>
  angle       20
}}
        """

    def _generate_background(self):
        """ Generates a background for pov file """
        self._final_file_format += """
background {
    color rgb <0.60, 0.70, 0.95>
}
        """

    def _generate_plane(self):
        """ Generates a background for pov file """
        values = self._json_data["POINTARRAY"]
        min_x = sys.maxsize
        min_y = sys.maxsize
        min_z = sys.maxsize
        for value in values:
            if value["minx"] < min_x:
                min_x = value["minx"]
            if value["miny"] < min_y:
                min_y = value["miny"]
            if value["minz"] < min_z:
                min_z = value["minz"]
        plane_val = min(min_x, min_y, min_z) * 2
        self._final_file_format += f"""
plane {{
  z, {plane_val}

  texture {{
    pigment {{
      bozo
      color_map {{
        [ 0.0 color rgb<0.356, 0.321, 0.274> ]
        [ 0.1 color rgb<0.611, 0.500, 0.500> ]
        [ 0.4 color rgb<0.745, 0.623, 0.623> ]
        [ 1.0 color rgb<0.837, 0.782, 0.745> ]
      }}
      warp {{ turbulence 0.6 }}
    }}
    finish {{
      diffuse 0.6
      ambient 0.1
      specular 0.2
      reflection {{
        0.2, 0.6
        fresnel on
      }}
      conserve_energy
    }}
  }}
}}
        """

    def _generate_texture(self, counter):
        """ Generates a texture for pov file """
        self._final_file_format += f"""
#declare Mesh_Texture_{counter}=
  texture{{
    pigment{{
      uv_mapping
      spiral2 8
      color_map {{
        [0.5 color rgb 1 ]
        [0.5 color rgb <0,0,0.2> ]
      }}
      scale 0.8
    }}
    finish {{
      specular 0.3
      roughness 0.01
    }}
}}
        """

    def _generate_mesh(self):
        """ Generates a mesh for pov file """
        point_iters = self._json_data["POINTARRAY"]
        face_iters = self._json_data["FACEARRAY"]
        for counter, value in enumerate(point_iters, 0):
            self._generate_texture(counter)
            self._mesh_string(
                value["vertices"],
                face_iters[counter]["faces"],
                value["nvertices"],
                face_iters[counter]["nfaces"],
                counter,
            )

    def _mesh_string(self, vertices, faces, num_vertices, num_faces, counter):
        """ Generates mesh strings for vertices and faces lists """
        self._generate_texture(counter)
        self._final_file_format += f"""
#declare Mesh_{counter}=
mesh2 {{
    vertex_vectors {{
        {num_vertices},
        {self._handle_point_array(vertices, 2)}
    }}
    face_indices {{
        {num_faces},
        {self._handle_face_array(faces, 2)}
    }}
}}
        """

    def _generate_object(self):
        """ Generates an object for pov file """
        for counter in range(len(self._json_data["POINTARRAY"])):
            self._final_file_format += f"""
object {{
  Mesh_{counter}
  texture {{ Mesh_Texture_{counter} }}
  rotate 90*z
}}
            """

    def _handle_point_array(self, vertices, num_tabs=0):
        """ Handles vertices from point_array """
        result = ""
        tabify = ""
        counter = 0
        for vertice in vertices:
            if counter == 0:
                result += f"{tabify}{self._convert_3d_into_pov(vertice)}, "
            if counter == 1:
                result += f"{self._convert_3d_into_pov(vertice)}, "
            if counter == 2:
                result += f"{self._convert_3d_into_pov(vertice)},\n"
                counter = -1
                tabify = "\t" * num_tabs
            counter += 1
        return result

    def _handle_face_array(self, faces, num_tabs=0):
        """ Handles face array data """
        result = ""
        tabify = ""
        counter = 0
        for face in faces:
            if counter == 0:
                result += f"{tabify}{self._convert_3d_into_pov(face)}, "
            if counter == 1:
                result += f"{self._convert_3d_into_pov(face)},\n"
                counter = -1
                tabify = "\t" * num_tabs
            counter += 1
        return result

    @staticmethod
    def _convert_3d_into_pov(vertice):
        """ Converts a 3d vector list into pov string """
        return f"<{vertice[0]}, {vertice[1]}, {vertice[2]}>"

    def save_pov(self, folder_path, file_name):
        """ Saves to pov file """
        output_file = Path(folder_path) / file_name
        with open(output_file, "w") as outfile:
            outfile.write(self._final_file_format)
