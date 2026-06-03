from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:0.6b"
)
from prompt import Prompt
from parser import Parser

chain = Prompt | model |Parser

while True:
    user_code=input("ME :" ).lower()
    if user_code=="exit":
        break
    result = chain.invoke({"user_code": user_code})

  
  # Ensure these names match the class fields exactly!
    print(f"\nDELL - Bug Type: {result.bugtype}")
    print(f"DELL - Explanation: {result.exp}")
    print(f"DELL - Fixed Code:\n{result.fixed}")