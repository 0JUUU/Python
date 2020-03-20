states = [('MI', 'Michigan', 'Lansing'),('CA', 'California', 'Sacramento'),
 ('TX', 'Texas', 'Austin'), ('MN', 'Minnesota', 'St Paul')]

with open('states.txt','w') as f:
     f.write('\n'.join('%s,%s,%s' % state for state in states))

with open('states.txt','r') as f:
    for line in f:
        fields = line.split(sep=',')
        print('State=',fields[1],'(',fields[0],')','Capital:',fields[2])
