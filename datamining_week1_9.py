MItuple = ('MI','Michigan','Lansing')
CAtuple = ('CA','California','Sacramento')
TXtuple = ('TX','Texas','Austin')

print(MItuple)
print(MItuple[1:])

states = [MItuple, CAtuple, TXtuple]
print(states)
print(states[2])
print(states[2][:])
print(states[2][1:])

states.sort(key=lambda state: state[2])
print(states)