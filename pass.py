import random
def pass_generator(n):
    lst1 = list(range(65,91))
    lst2 = list(range(97,123))
    lst3 = list(range(10))
    lst4 = ['+','-','=','@','#','$','%','^']
    s1 = ''.join(chr(c) for c in lst1)
    s2 = ''.join(chr(c) for c in lst2)
    s3 = ''.join(str(i) for i in lst3)
    s4 = ''.join( c for c in lst4)
    s = s1 + s2 + s3 + s4
    p = ''
    for _ in range(n):
        p += random.choice(s)
    return p
kol = input("введите количество паролей:")
cim = input("введите количество символов:")
knumber = int(kol)
snumber = int(cim)

handle = open("pass.txt", "a")
for i in range(knumber): #сколько паролей будет записано
    handle.write(pass_generator(snumber))#кол-во символов в пароле
    handle.write("\n")
handle.close()
print ("записанно", kol ,"паролей")
print (cim,"знаков в каждом пароле")
