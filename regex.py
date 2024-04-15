import re
a="charlie chaplin and chaand and the chocolate candy factory"
b="suryapratapsingh0833@gmail.com"
c="hello"
d="xyz,zy,yz,xyzz,zxyyz,xz,xyy,xxy,zxy,yxzx"
print("1. Use of \ symbol in regex to discard the meaning of special character")
match=re.search(r"\.",b)
print(match)
print("2. Use of [] symbol in regex to find out particular charater or string present anywhere in string")
match=re.search(r"[p]",b)
print(match)
print("3. Use of ^ symbol in regex to find out wheather starting of string match with the given string")
match=re.search(r"^surya",b)
print(match)
print("4. Use of $ symbol in regex to find out wheather ending of string match with the given string")
match=re.search(r".com$",b)
print(match)
print("5. Use of . symbol in regex to get match any character . could be replace with any character ")
match=re.findall(r"c.a",a)
print(match)
print("6. Use of | symbol in regex to find out wheather any of the searched string match in the given string")
match=re.findall(r"cha|fact",a)
print(match)
print("7. Use of ? symbol in regex to find 0 or 1 occurances")
match=re.findall(r"ch?a",a)
print(match)
print("8. Use of * symbol in regex to find out any number of occurances")
match=re.findall(r"ch*a",a)
print(match)
print("9. Use of + symbol in regex to find out one or more occurances")
match=re.findall(r"xy+z",d)
print(match)
print("10. Use of  {} symbol to fill custom number of occurances")
match=re.findall(r"x{2,4}",d)
print(match)



