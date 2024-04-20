class Human:
    height = 170


class Student(Human):
    height = 175


class Worker(Human):
    pass


vasya = Student()
masha = Worker()

print(vasya.height)
print(masha.height)

