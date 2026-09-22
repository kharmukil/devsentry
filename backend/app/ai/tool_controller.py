from backend.app.tools.dispatcher import ToolDispatcher


class ToolController:
    def __init__(self):
        self.dispatcher = ToolDispatcher()

    def execute_tool(self, tool_name: str):
        return self.dispatcher.execute(tool_name)
