def myfun(*argm):
 try:
    print(argm)
 except Exception:
     print("missing")
myfun("hey", "there", "how ", " can", " i", " help")


def myfun(sub1, *subs):
    try:
     print("my first statement:", sub1)
     for sub in subs:
        print("next other statements are:", sub)
    except Exception:
        print("invalid")


myfun("its true", "its not", "its wrong", "i can't", "that is false", "i can", "now done")

print("hello" "world")


def addtwonums(a, b):
    return a + b


def addthreenums(a, b, c):
    return a + b + c


print("add two nums")
print(addtwonums(4, 5))
print("add three nums")
print(addthreenums(1, 1, 1))


def AddNums(*nums):
    result = 0
    for num in nums:
        result = result + num
    return result


def addargwithdefault(arg1, *args):
    result = 0
    for arg in args:
        result = result + arg
    return result + arg1

try:
    print("adding multiple nums")
    print(AddNums(2, 1, 6, 79, 4, 5, 6))
    print(AddNums(1, 4, 6, 8, 43, 7, 823))
    print("add zero nums")
    print(addargwithdefault())
except TypeError:
    print("invalid")
except Exception:
    print("missing")
finally:
    print("done")
    

