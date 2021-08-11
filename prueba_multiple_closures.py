def operator(x):
        def multiplier(n):
            return x*n
        def sum(n):
            return x+n
        def division(n):
            assert n!=0,"No es válida la división por cero"
            return x/n
        def resta(n):
            return x-n
        return [multiplier,sum,division,resta]


def run():
    #Me genera una multiplicación por 5
    my_operation=operator(5)[0]
    #Me retorna 5*3=15
    print(my_operation(3))

    #Me genera una división por 6
    my_operation=operator(6)[2]
    #Me retorna 6/2=3
    print(my_operation(2))  




if __name__=='__main__':
    run()



    #operation=input("¿Qué operación quieres realizar?: ")
    # index:int
    # if operation=="multiplicacion":
    #     index=0
    # elif operation=="suma":
    #     index=1
    # elif operation=="division":
    #     index=2
    # elif operation=="resta":
    #     index=3
   
    # my_operation=operator(int(input("¿Con qué quieres operar?: ")))[index]
    # print(my_operation(int(input("¿Con qué lo quieres operar?: "))))