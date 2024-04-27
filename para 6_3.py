def checker(var_1):
    if var_1 != str:
        raise TypeError(f"Sorry we can't work with{type(var_1)},we need type str")
    else:
        return  var_1
first_var = 10
checker(first_var)