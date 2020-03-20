mylist = ['this','is','a','list']
for word in mylist:
    print(word.replace("is","at"))

mylist2 = [len(word) for word in mylist]
print(mylist2)

states = [('MI','Michigan','Lansing'), ('CA','California','Sacramento'), ('TX','Texas','Austin')]

sorted_capitals = [state[2] for state in states]
sorted_capitals.sort()
print(sorted_capitals)

fruits = {'apples':3, 'oranges':4, 'bananas':2, 'cherries':10}
fruitnames = [k for (k,v) in fruits.items()]
print(fruitnames)
 