import subprocess


class ProcessTool:
    def check_running_processes(self) -> str:
        result = subprocess.run(
            ["tasklist"],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout
