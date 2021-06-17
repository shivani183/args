#def myFun1(**kwargs):
   # for key, value in kwargs.items():
    #    print("%s == %s" % (key, value))

#myFun1(first='Geeks', mid='for', last='Geeks')


def myfun2(arg1,arg2,arg3):
    try:
     print("arg1:", arg1)
     print("arg2:", arg2)
     print("arg3:", arg3)
    except Exception:
        return 0

try:
 arg = ('first','second','third')
 myfun2(*arg)
 kwargs = {"arg1": "name", "arg2": "age", "arg3": "class"}
 myfun2(**kwargs)
except TypeError:
    print("something inappropriate")
except Exception:
    print("break")
finally:
    print("successful")





