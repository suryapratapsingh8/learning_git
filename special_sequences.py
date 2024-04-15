import re
a="harry potter"
print("1. \A symbol matches if staring of sting contain that value")
match=re.search(r"\Ahar",a)
print(match)
print("1. \b symbol matches if staring or ending of sting contain that value")
match=re.search(r"\bhar",a)
match1=re.search(r"er\b",a)
print(match,match1)