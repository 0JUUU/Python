s1 = "This"
print(s1[1:])
print(len(s1))
print("Length of string is " + str(len(s1)))
print(s1.upper())
print(s1.lower()) 

s2 = "This is a string"
words = s2.split(' ')
print(words[0])
print(s2.replace('a','another'))
print(s2.replace('is','at'))
print(s2.find("a"))
print(s1 in s2)

print(s1 == 'This')
print(s1 < 'That')
print(s2 + " too")
print((s1 + " ")*3)