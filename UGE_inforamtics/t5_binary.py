for n in range(20, 30): #cycle
    b = bin(n)[2:] #срез. в числах, в 

    if n % 2 == 0:
        b += '00'
    else:
        b += '11'


    b += str(b.count('1') % 2) #методы 

    r = int(b, 2)

    print(f'{b} {r}')

    if r > 177:
        print(r)
        break