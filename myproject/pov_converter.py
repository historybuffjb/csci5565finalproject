""" Converts a specific json file into a pov file """

from json import load


class PovConverter:
    """ Converts json to pov """

    def __init__(self, json_path):
        self.json_path = json_path
        self.json = {}
        self._important_chunks = {
            "POINTARRAY": self._handle_point_array,
            "TEXVERTS": self._handle_tex_verts,
            "MESHMATRIX": self._handle_mesh_matrix,
            "FACEARRAY": self._handle_face_array,
            "MSHMATGROUP": self._handle_msh_mat_group,
            "SMOOTHGROUP": self._handle_smooth_group,
        }

    def convert_pov(self):
        """ Converts to pov """
        with open(self.json_path, "r") as json_file:
            json_data = load(json_file)
            for chunk in json_data:
                if chunk in self._important_chunks:
                    self._important_chunks[chunk](json_data[chunk])

    def _handle_point_array(self, chunk):
        """ Handles vertices from point_array """
        num_vertices = chunk["nvertices"]
        vertices = chunk["vertices"]
        end_result = "mesh2 {\n\tvertex_vectors {\n\t"
        end_result += f"{num_vertices},\n"
        counter = 0
        for vertice in vertices:
            if counter == 0:
                end_result += f"\t\t{self._convert_3d_into_pov(vertice)}, "
            if counter == 1:
                end_result += f"{self._convert_3d_into_pov(vertice)}, "
            if counter == 2:
                end_result += f"{self._convert_3d_into_pov(vertice)},\n"
                counter = -1
            counter += 1
        end_result += "\n\t}"
        print(end_result)

    def _handle_tex_verts(self, chunk):
        """ Handles vertices from tex_verts """
        # print(f"Tex Verts Data: {chunk}")

    def _handle_mesh_matrix(self, chunk):
        """ Handles mesh matrix """
        # print(f"Mesh Matrix Data: {chunk}")

    def _handle_face_array(self, chunk):
        """ Handles face array data """
        # print(f"Face Array Data: {chunk}")

    def _handle_msh_mat_group(self, chunk):
        """ Handles Mesh mat group """
        # print(f"MSH Mat Group Data: {chunk}")

    def _handle_smooth_group(self, chunk):
        """ Handles Smooth Group """
        # print(f"Smooth Group Data: {chunk}")

    @staticmethod
    def _convert_3d_into_pov(vertice):
        """ Converts a 3d list of points into pov string """
        return f"<{vertice[0]}, {vertice[1]}, {vertice[0]}>"
