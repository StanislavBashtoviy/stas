class Собака:
    gav = 100


class homeless(Собака):
    gav = 150


class domestic(Собака):
    pass


Bobik = homeless()
Tyzuk = domestic()


print(Bobik.gav)
print(Tyzuk.gav)