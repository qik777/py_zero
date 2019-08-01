isRunning = True
while isRunning:
    s = input('Enter something : ')
    if s == 'quit':
        isRunning = False
    if s == 'exit':
        break
    print('Length of the string is', len(s))
else:
    print('Done')
print('Done-2')