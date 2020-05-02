""" Converts a specific json file into a pov file """

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
        self._generate_texture()
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

    def _generate_camera(self):
        """ Generates a camera for pov file """
        values = self._json_data["POINTARRAY"]
        multiplier = 8
        x_val = abs(values["maxx"]) * multiplier
        y_val = abs(values["maxy"]) * multiplier
        z_val = abs(values["maxz"]) * multiplier
        location = f"<{x_val}, {y_val}, {z_val}>"
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
        plane_val = (
            min(
                self._json_data["POINTARRAY"]["minx"],
                self._json_data["POINTARRAY"]["miny"],
                self._json_data["POINTARRAY"]["minz"],
            )
            * 2
        )
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

    def _generate_texture(self):
        """ Generates a texture for pov file """
        self._final_file_format += """
#declare Mesh_Texture=
  texture{
    pigment{
      uv_mapping
      spiral2 8
      color_map {
        [0.5 color rgb 1 ]
        [0.5 color rgb <0,0,0.2> ]
      }
      scale 0.8
    }
    finish {
      specular 0.3
      roughness 0.01
    }
}
        """

    def _generate_mesh(self):
        """ Generates a mesh for pov file """
        self._final_file_format += f"""
#declare Mesh=
mesh2 {{
    vertex_vectors {{
        {self._json_data["POINTARRAY"]["nvertices"]},
        {self._handle_point_array(self._json_data["POINTARRAY"]["vertices"], 2)}
    }}
    face_indices {{
        {self._json_data["FACEARRAY"]["nfaces"]},
        {self._handle_face_array(self._json_data["FACEARRAY"]["faces"], 2)}
    }}
}}
        """

    def _generate_object(self):
        """ Generates an object for pov file """
        self._final_file_format += """
object {
  Mesh
  texture { Mesh_Texture }
  rotate 180*z
  rotate 90*x
  translate < -2, 2, 1.5>
}
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
