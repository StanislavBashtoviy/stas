try :
    print("Start")
    print(10/0)
    print("after error")
except NameError:
    print("We have a error")

except ZeroDivisionError:
    print("Impossible")
else:
    print("No problem")
finally:
    print("Last")


print("Code")
