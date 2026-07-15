import shlex
import subprocess


class CommandService:

    @staticmethod
    def run(command):

        try:

            if isinstance(command, str):

                command = shlex.split(command)

            result = subprocess.run(

                command,

                capture_output=True,

                text=True,

                check=True

            )

            return result.stdout.strip()

        except subprocess.CalledProcessError:

            return None

    @staticmethod
    def run_raw(command):

        if isinstance(command, str):

            command = shlex.split(command)

        return subprocess.run(

            command,

            capture_output=True,

            text=True

        )