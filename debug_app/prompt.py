from langchain_core.prompts import ChatPromptTemplate
from parser import Parser
Prompt=ChatPromptTemplate.from_template("Analyze this code and debug it.\n{format_instructions}\nCode: {user_code}",
    partial_variables={"format_instructions": Parser.get_format_instructions()})
