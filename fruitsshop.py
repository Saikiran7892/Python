#fruits shop

print('*'*10,'Fruits Shop','*'*10)
fruits=['apple','organge','banana','graphs']
cart=[]

while True:
    for i in fruits:
        print(i)
    print()
    print('1.add')
    print('2.remove')
    print('3.view')
    print('4.exit')
    print()
    ch=int(input('enter a choice:'))

    if ch==1:
        fruit=input('enter a fruit:')
        if fruit in fruits:
           if fruit in cart:
              print(fruit,'is already in cart')
           else:
              cart.append(fruit)
              print(fruit,'is added to the cart')
              print()
        else:
            print(fruit,'is not available in shop')
                
    elif ch==2:
        fruit=input('enter a fruit:')
        if fruit in cart:
            cart.remove(fruit)
            print(fruit,'is removed from cart')
        else:
            print(fruit,'is not available in the cart')
        print()
    elif ch==3:
        print('*'*10,'View Cart','*'*10)
        for f in cart:
            print(f,end=' ')
        print()
        print('*'*31)
    elif ch==4:
        print('exiting')
        break
    else:
        fruit=input('enter a correct option:')
        
