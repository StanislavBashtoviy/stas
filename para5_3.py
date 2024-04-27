data ='vasya'

print(hasattr(data, "reverse"))
print(hasattr(data, "index"))

print(getattr(data, "reverse", None))
print(getattr(data, "index", None))

def s_function():
    pass



print(callable(data))
print(callable(s_function()))
