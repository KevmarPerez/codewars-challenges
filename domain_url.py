import re

s = "www.zombie-bites.com" 

string = r"^http://|^https://|^www."
print(re.split(string, s))