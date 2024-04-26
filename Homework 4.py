class Собака:
    gav = 100

class Human:
    run = 40

class bomj(Human):
    run = 60


class homeless(Собака):
    gav = 150


class domestic(Собака):
    pass

Vasya = bomj()
Bobik = homeless()
Tyzuk = domestic()


print(Bobik.gav)
print(Tyzuk.gav)
print(Vasya.run)