import re

text = "I am learning the Python"
pattern = r"Python"
replacement = "Devops"

new_text = re.sub(pattern, replacement, text)
print(f"Modified text :" , new_text)
