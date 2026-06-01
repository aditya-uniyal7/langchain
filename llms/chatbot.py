from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, AIMessage ,SystemMessage
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct"
)
messages=[
     SystemMessage(
        content="""You are an advanced AI assistant.

Your goals are:
- Provide accurate, helpful, and well-reasoned answers.
...
"""
     )]

chat = ChatHuggingFace(llm=llm)
while True:
    user=input("ME :" ).lower()
    messages.append(HumanMessage(content=user))
    if user=="exit":
        break
    res=chat.invoke(messages)

    print("DELL :", res.content)
    messages.append(AIMessage(content=res.content))

