from davidkhala.ai.agent.dify.api.app import Conversation
def chat(api_key: str, user: str, template: str, **kwargs) -> str:
    c = Conversation(api_key, user)
    r: Conversation.ChatResult = c.agent_chat(template, **kwargs)
    return r['answer']