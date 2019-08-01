# List Comprehension
listone = [2, 3, 4, 1, 5]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)
print()

# receive tuple and dict
def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print(powersum(2, 3, 4))
print(powersum(2, 10))
print()

# assert
mylist = ['item','help']
assert len(mylist) >= 1
print(mylist.pop())

assert len(mylist) >= 1
print(mylist.pop())

assert len(mylist) >= 1