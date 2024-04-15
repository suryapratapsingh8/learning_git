import re
a="harry potter"
print("1. \A symbol matches if staring of sting contain that value")
match=re.search(r"\Ahar",a)
print(match)