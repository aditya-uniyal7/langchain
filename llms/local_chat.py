from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:0.6b"
)

response = llm.invoke("Tell me a joke")
print(response.content)