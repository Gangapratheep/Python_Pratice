import re

text = "TCS,Amazon,Tech-mahindra,Infosys,Capgemini"
pattern = r","

split_result = re.split(pattern, text)
print("Split result :", split_result )
