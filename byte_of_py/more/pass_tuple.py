# return 2 parameters
def get_error_details():
    return (2, 'details')

errnum, errstr = get_error_details()

print(errnum)
print(errstr)

a = 5; b = 8
print(a,b)
a , b= b, a
print(a,b)