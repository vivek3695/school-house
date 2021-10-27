c=0
list1=[2,4,1,5,3,9]
while True:
    print("this is the menu")
    print("1: Add a customer")
    print("2: Modify customer details")
    print("3: Delete customer details")
    print("4: sort customer list")
    print("5: display the sorted list")
    print("6: Exit")
    c=int(input("Enter your choice: "))
    if c==1:
        print("1: Add amount deposited")
        print("2: Add a customer account")
        d=int(input("Enter your choice"))
        if d==1:
            print(list1)
            amount=int(input("how much would you like to deposit?: "))
            pos=int(input("at what position"))
            list1.insert(pos, amount)
            print(list1)
        elif d==2:
            list2=eval(input("add a customer list"))
            list1.extend(list2)
            print(list1)
    elif c==2:
        print(list1)
        pos=int(input("at what position"))
        e=int(input("Enter your choice"))
        list1[pos]=e 
        print(list1)
    elif c==3:
        print(list1)
        pos=int(input("at what position would u like to delete: "))
        list1.remove(pos)
        print(list1)
    elif c==4:
        print("1: sort in ascending order")
        print("2: sort in descending order")
        f=int(input("enter your choice"))
        if f==1:
            list1.sort()
        elif f==2:
            list1.sort(reverse=True)
    elif c==5:
                print(list1)
    elif c==6:
        break
print("thank you")
