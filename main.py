from LLM.llm import generate_commands
from LLM.extract import extract_commands

print(extract_commands(generate_commands("directory name is Amal", "do a git pull")))