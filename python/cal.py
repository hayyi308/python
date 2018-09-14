
cal = raw_input('Please enter a operator:')

print('input int a:')
a = int(input('a = '))
print('input int b:')
b = int(input('b = '))

if  cal == ('+'):
    print "\na+b = "+str(a+b)
elif  cal == ('-'):
    print "\na-b = "+str(a-b)
elif  cal == ('*'):
    print "\na*b = "+str(a*b)
elif  cal == ('/'):
    print "\na/b = "+str(a/b)
else:
    print "\nError!"
