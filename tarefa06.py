import random

def atividade1():
    al = random.randint(5,10)
    return al

def atividade2():
    al1 = random.randint(1,10)
    al2 = random.randint(2,10)
    al3 = random.randint(3,10)
    print(al1, al2, al3)

def atividade3():
    al  = random.randrange(10,30)
    print(al)


def atividade4():
    for i in range(10,0,-1):
        print(i)
        input("Pressione enter para continuar...")
        print("Fogo")
atividade4()

def atividade5():
    num=int(input("Digite um Numero inteiro: "))
    print(f'tabuada de mult de{num}:')
    for i in range(1,11):
        print(f"{num} x {i}={num * i }")
atividade5()       

def atividade6():
    for i in range(99,1,-2):
        print(i)
atividade6()        