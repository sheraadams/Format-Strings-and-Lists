xlist = ["United States", "Canada", "Spain", "Russia", "Germany", "Mexico", "United Kingdom", "France", "Japan", "China", "Saudi Arabia", "South Korea", "Israel", "Iran", "Turkey", "India", "Australia", "Ukraine", "India", "Switzerland", "Italy", "Sweeden", "Egypt", "Netherlands", "Pakistan", "Quatar"]
str = input("copy here to sort:")
list1 = str.split(",")
print(sorted(list1))

str2 = input("copy to here here to remove quotes:")

for i in range(len(str2)):
     str2 = str2.replace("'", "")
     str2 = str2.replace('"', "")
print(str2)

str4 = input("copy here to add quotes to text: ")
str5 = str4.split(",")
print(str5)

str6 = input("copy here to strip unwanted characters from string:")
for i in range(len(str6)):
     str6 = str6.replace(" ", "")
     str6 = str6.replace("\n","")
print(str6)

str7 = input("copy here to strip unwanted characters from list:")
list2 = str7.split(",")
print(list2)
strippedlist = []
for i in list2:
    z = i.replace(' ','')
    strippedlist.append(z)

print(strippedlist)