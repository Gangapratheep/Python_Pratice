import re
text = " The quick brown fox"
pattern = r"fox"

search = re.search(pattern, text)

if search :
    print(f"Match found :", search.group())
else :
    print("No match found")
    
