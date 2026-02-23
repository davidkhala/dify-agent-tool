from davidkhala.ai.agent.dify.api.app import Conversation


def chat(base_url: str, api_key: str, user: str, template: str, **kwargs) -> str:
    c = Conversation(api_key, user)
    c.base_url = base_url
    r: Conversation.ChatResult = c.agent_chat(template, **kwargs)
    return r['answer']
