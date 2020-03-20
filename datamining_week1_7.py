mylist = ['this','is','a','list']
print(mylist)
print(type(mylist))

print("list" in mylist)
print(mylist[2])
print(mylist[:2])
print(mylist[2:])
mylist.append("too")

separator = " "
print(separator.join(mylist))

mylist.remove("is")
print(mylist)