from langchain_core.output_parsers import PydanticOutputParser
from schema import Debug

Parser=PydanticOutputParser(pydantic_object=(Debug))
