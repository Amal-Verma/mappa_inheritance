import re

def extract_commands(text):
    # Regular expression to find text between $$[ and ]$$
    pattern = r'\$\$\[([^]]+)\]\$\$'
    matches = re.findall(pattern, text)
    return matches
