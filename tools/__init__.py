from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.core import chat


class AgentTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        api_key: str = tool_parameters.get("api_key")  # FIXME should be put into tool credential
        user: str = tool_parameters.get("user")
        query: str = tool_parameters.get("query")

        lines = chat(api_key, user, query)

        for m in lines :
            yield self.create_text_message(m)  # TODO is multiple round allowed?
