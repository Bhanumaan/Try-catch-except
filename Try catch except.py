import new

try:
    print(x)
except:
    print("An exception occured")

try:
    print(x)
except NameError:                                          #NameError is a special kind of exception case
    print("variable x in not defined")
except:
    print("somehting else went wrong")

try:
    print('Hello world')
except:
    print("an error occured")
else:
    print("No error came \n ")

try: print(x)
except: print("error occured")
finally: print("try except is done now ")

print(" \n \n \n xxxx \n \n ")

try:
    f=open(new.txt)                                           #error will come because it is a read only file
    try:
        f.write("Added to the txt file")
    except:
        print("something went wrong")
    finally:
        f.close()
except:
    print("somehting went wrong while opening the file")


x= 2                    #if the number is negative it will trigger an error in RUN
if x < 0:
    raise Exception("Sorry no numbers below zero")

x=["happpy",23,44]
if not type(x) is list:
    raise TypeError("only intergers are allowed")





