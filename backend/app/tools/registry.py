from backend.app.tools.deployment_tool import DeploymentTool
from backend.app.tools.disk_tool import DiskTool
from backend.app.tools.log_tool import LogTool
from backend.app.tools.nginx_tool import NginxTool
from backend.app.tools.process_tool import ProcessTool


process_tool = ProcessTool()
disk_tool = DiskTool()
log_tool = LogTool()
nginx_tool = NginxTool()
deployment_tool = DeploymentTool()


TOOLS = {
    "check_running_processes": process_tool.check_running_processes,
    "check_disk_usage": disk_tool.check_disk_usage,
    "read_application_logs": log_tool.read_application_logs,
    "read_nginx_logs": nginx_tool.read_nginx_logs,
    "analyze_deployment": deployment_tool.analyze_deployment,
}
