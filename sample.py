import time

sta = time.time()

def calc(a, b): 
    for i in range(100000):
        a += i
        b -= i
    return print(4*a + 3*b)

def evalate(reslt):
    if reslt < 1:
        print("Execellent")
    elif reslt < 2:
        print("Very Good")
    elif reslt < 3:
        print("Good")
    elif reslt < 4:
        print("Average")
    else:
        print("Poor")
        
calc(0, 0)

end = time.time()

resltTime = end - sta
print(resltTime)
print(str(resltTime))
evalate(resltTime)

    
    