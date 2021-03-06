""" Class for running povray """
from os import cpu_count
from subprocess import run, PIPE


class PovRunner:
    """ Runs povray from the shell and moves file to given folder """

    def __init__(self, pov_path, input_path, output_path):
        self._pov_exec = pov_path
        self._input_path = input_path
        self._output_path = output_path

    def run_pov(self):
        """ Runs povray """
        self._run_shell_command(
            [
                self._pov_exec,
                self._input_path,
                f"+WT{cpu_count()}",
                f"+o{self._output_path}",
            ]
        )

    @staticmethod
    def _run_shell_command(args):
        """ runs a given shell command """
        run(args, stdout=PIPE, stderr=PIPE, check=True)
