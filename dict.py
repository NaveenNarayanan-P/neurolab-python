branches = {}
print(type(branches))

branches['name'] = 'Peepul Park'
branches['floors'] = 4
branches['blocks'] = ['A','B','C','D']
branches['odc_names'] = ('office1', 'office2', 'office3')
branches['block_parking'] = {'A':100, 'B':234, 'C':212, 'D': 234}

print(branches)
print(len(branches)) 

#change Block B parking count to 300
branches['block_parking']['B'] = 300

print(branches.keys())
print(branches.values())

for key, value in branches.items():
    print(key + ' : ', value)

#compare dictionary
dict1 = {'a':1, 'b':2, 'lst': ['check']}
dict2 = {'a':1, 'lst': ['check'], 'b':2, 'b':334}
print(dict1 == dict2)


#deletion
del dict1['lst']
print(dict1)
# del dict2['b']

try:
    print(dict2['b'])
except KeyError as error:
    print('No such data available')

