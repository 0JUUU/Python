abbrev = {}
abbrev['MI'] = "Michigan"
abbrev['MN'] = "Minnesota"
abbrev['TX'] = "Texas"
abbrev['CA'] = "California"

print(abbrev)
print(abbrev.keys())
print(abbrev.values())
print(len(abbrev))

print(abbrev.get('MI'))
print("FL" in abbrev)
print("CA" in abbrev)

keys = ['apples', 'oranges', 'bananas', 'cherries']
values = [3,4,2,10]
fruits = dict(zip(keys,values))
print(fruits)
print(sorted(fruits))

from operator import itemgetter
print(sorted(fruits.items(), key = itemgetter(0)))
print(sorted(fruits.items(), key = itemgetter(1)))