try:
    def make_division_by(n: float):
        if n==0:
            raise ZeroDivisionError ("No está permitida la divisón por cero, ingrese otro número distinto de cero")
        def divisor(x: float) -> float:
            return x/n
        return divisor
except ZeroDivisionError as zde:
    print(zde)

def run():
    division_by_3=make_division_by(3)
    print(division_by_3(17))

    division_by_5=make_division_by(5)
    print(division_by_5(100))

    division_by_18=make_division_by(18)
    print(division_by_18(54))

    # division_by_0=make_division_by(0)
    # print(division_by_0(5))



if __name__=='__main__':
    run()

