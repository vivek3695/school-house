z=int(input('how many times would you like to use: '))
for x in range(z):
    a=int(input('enter a natural number: '))
    l=[]
    if a==1:
        print('neither a prime nor a composite number')
    if a>1:
        for i in range(2,a):
            b=a%i
            l.append(b)
        if 0 in l:
            print('not a prime number')
        else:
            print('prime number')
