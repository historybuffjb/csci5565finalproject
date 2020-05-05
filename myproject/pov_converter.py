""" Converts a specific json file into a pov file """
from sys import maxsize
from pathlib import Path


class PovConverter:
    """ Converts json to pov """

    def __init__(self, parser):
        self._parser = parser
        self._object_counter = 0
        self._minx = maxsize
        self._miny = maxsize
        self._minz = maxsize
        self._maxx = ~maxsize
        self._maxy = ~maxsize
        self._maxz = ~maxsize
        self._meshes_string = ""
        self._final_file_format = ""

    def convert_pov(self):
        """ Converts to pov """
        self._iter_chunks(self._parser.chunks)
        self._final_file_format += self._generate_global_settings()
        self._final_file_format += self._generate_light_source()
        self._final_file_format += self._generate_camera()
        self._final_file_format += self._generate_background()
        self._final_file_format += self._generate_plane()
        self._final_file_format += self._meshes_string

    def _iter_chunks(self, chunk):
        """ Iterate through parser chunks """
        if chunk.name == "NTRIOBJECT":
            self._meshes_string += self._generate_mesh(chunk)
        else:
            for child in chunk.children:
                self._iter_chunks(child)

    @staticmethod
    def _generate_global_settings():
        """ Generates global settings for pov file """
        return """
#include "colors.inc"
#include "shapes.inc"
#include "textures.inc"
#include "finish.inc"
#include "glass.inc"
#include "metals.inc"
#include "stones.inc"
#include "woods.inc"
#include "golds.inc"
#version 3.7

global_settings {
    assumed_gamma 1
    radiosity {
      pretrace_start 0.08
      pretrace_end   0.01
      count 150
      nearest_count 10
      error_bound 0.5
      recursion_limit 3
      low_error_factor 0.5
      gray_threshold 0.0
      minimum_reuse 0.005
      maximum_reuse 0.2
      brightness 1
      adc_bailout 0.005
    }
    photons {
    count 20000
    autostop 0
    jitter .4
    }
}
        """

    @staticmethod
    def _generate_light_source():
        """ Generates light source for pov file """
        return """
light_source {
    <200, 200, 200>*10000
    rgb 1.3
}
        """

    # pylint: disable=R0914
    def _generate_camera(self):
        """ Generates a camera for pov file """
        x_cam_loc = (abs(self._minx) + abs(self._maxx)) * 8
        y_cam_loc = (abs(self._miny) + abs(self._maxy)) * 8
        z_cam_loc = (abs(self._minz) + abs(self._maxz)) * 8
        camera_location = [x_cam_loc, y_cam_loc, z_cam_loc]
        lookat_location = [self._minx, self._miny, self._minz]
        return f"""
camera {{
  location    <{camera_location[0]}, {camera_location[1]}, {camera_location[2]}>
  direction   y
  sky         z
  up          z
  right       (4/3)*x
  look_at     <{lookat_location[0]}, {lookat_location[1]}, {lookat_location[2]}>
  angle       20
}}
        """

    @staticmethod
    def _generate_background():
        """ Generates a background for pov file """
        return """
background {
    color rgb <0.60, 0.70, 0.95>
}
        """

    def _generate_plane(self):
        """ Generates a background for pov file """
        return f"""
plane {{
  z, {self._minz}
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
      diffuse 0
      ambient 0
      specular 0.2
      reflection {{
        1.0
      }}
      conserve_energy
    }}
  }}
}}
        """

    def _generate_texture(self):
        """ Generates a texture for pov file """
        return f"""
#declare Mesh_Texture_{self._object_counter}=
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

    def _generate_mesh(self, chunk):
        """ Generates a mesh for pov file """
        result = ""
        point_iters = []
        num_vertices = 0
        face_iters = []
        num_faces = 0
        rot_vals = []
        cen_vals = []
        for child in chunk.children:
            if child.name == "POINTARRAY":
                child_dict = child.data.pov_convert()
                point_iters = child_dict["vertices"]
                num_vertices = child_dict["nvertices"]
            elif child.name == "FACEARRAY":
                child_dict = child.data.pov_convert()
                face_iters = child_dict["faces"]
                num_faces = child_dict["nfaces"]
            elif child.name == "MESHMATRIX":
                child_dict = child.data.pov_convert()
                rot_vals = child_dict["rot"]
                cen_vals = child_dict["center"]
        if 0 in [
            len(point_iters),
            num_vertices,
            len(face_iters),
            num_faces,
            rot_vals,
            cen_vals,
        ]:
            return ""
        result += self._generate_texture()
        result += self._mesh_string(point_iters, num_vertices, face_iters, num_faces)
        result += self._generate_object(rot_vals, cen_vals)
        self._object_counter += 1
        return result

    def _mesh_string(self, vertices, num_vertices, faces, num_faces):
        """ Generates mesh strings for vertices and faces lists """
        return f"""
#declare Mesh_{self._object_counter}=
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

    def _generate_object(self, rot_vals, cen_vals):
        """ Generates an object for pov file """
        return f"""
object {{
  Mesh_{self._object_counter}
  photons {{
    target
    refraction on
    reflection on
    collect on
    }}
  texture {{ Mesh_Texture_{self._object_counter} }}
  rotate 90*z
}}
            """

    def _handle_point_array(self, vertices, num_tabs=0):
        """ Handles vertices from point_array """
        result = ""
        tabify = ""
        counter = 0
        for vertice in vertices:
            self._calc_mins(vertice)
            self._calc_maxs(vertice)
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

    def _calc_mins(self, vertice):
        """ Calculate the minimum x y and z value """
        if vertice[0] < self._minx:
            self._minx = vertice[0]
        if vertice[1] < self._miny:
            self._miny = vertice[1]
        if vertice[2] < self._minz:
            self._minz = vertice[2]

    def _calc_maxs(self, vertice):
        if vertice[0] > self._maxx:
            self._maxx = vertice[0]
        if vertice[1] > self._maxy:
            self._maxy = vertice[1]
        if vertice[2] > self._maxz:
            self._maxz = vertice[2]

    @staticmethod
    def _convert_3d_into_pov(vertice):
        """ Converts a 3d vector list into pov string """
        return f"<{vertice[0]}, {vertice[1]}, {vertice[2]}>"

    def save_pov(self, folder_path, file_name):
        """ Saves to pov file """
        output_file = Path(folder_path) / file_name
        with open(output_file, "w") as outfile:
            outfile.write(self._final_file_format)
