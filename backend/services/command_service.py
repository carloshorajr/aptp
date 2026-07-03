import subprocess

class CommandService:

    @staticmethod
    def run(command):

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )

            return result.stdout.strip()

        except subprocess.CalledProcessError as e:

            return None

    @staticmethod
    def run_raw(command):

        return subprocess.run(
            command,
            capture_output=True,
            text=True
        )