from backend.app.tools.registry import TOOLS


class ToolDispatcher:
    def execute(self, tool_name: str):
        if tool_name not in TOOLS:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return TOOLS[tool_name]()
