def is_prime_number(num: int)->bool:
    divisor: int=0
    for i in range(2,num):
        if num%i==0:
            divisor+=1
    if divisor==0:
        return True
    else:
        return False



def run():
    print(is_prime_number('a'))



if __name__=='__main__':
    run()