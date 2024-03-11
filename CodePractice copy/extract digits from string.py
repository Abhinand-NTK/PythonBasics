import re
inputstring  = "Abhinad587485"
digits = re.findall(r'\d+',inputstring)

print(digits)