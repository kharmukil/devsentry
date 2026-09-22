from backend.app.tools.disk_tool import DiskTool
from backend.app.tools.process_tool import ProcessTool


process_tool = ProcessTool()
disk_tool = DiskTool()


TOOLS = {
    "check_running_processes": process_tool.check_running_processes,
    "check_disk_usage": disk_tool.check_disk_usage,
}
