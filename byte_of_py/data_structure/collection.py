bri = set(['brazil', 'russia', 'india'])
print('Is india in bri,result:',end=' ')
print('india' in bri)
print('Is usa in bri,result:',end=' ')
print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bri.remove('russia')
print('bri & bric,result:',end=' ')
print(bri & bric)