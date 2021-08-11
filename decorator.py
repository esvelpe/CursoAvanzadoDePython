from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time=datetime.now()
        func(*args, **kwargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print("Pasaron " + str(time_elapsed.total_seconds())+" segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a: int, b: int)->int:
    return a+b

@execution_time
def saludo(nombre="cesar"):
    print(f'Hola {nombre}')

def run():
    random_func()
    suma(5,5)
    saludo("Facundo")
    



if __name__=='__main__':
    run()


























# def mayusculas(func):
#     def wrapper(texto):
#         return func(texto).upper()
#     return wrapper

# @mayusculas
# def mensaje(nombre):
#     return f'{nombre}, recibiste un mensaje'

# print(mensaje('Cesar'))