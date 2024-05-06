
'''
print("Start Code")

a = int(input("Enter a First Number : "))
b = int(input("Enter a Second Number : "))

c = a/b

print("Division : ",c)


print("End Code")
'''
'''
try :
    print("Start Code")

    a = int(input("Enter a First Number : "))
    b = int(input("Enter a Second Number : "))

    c = a/b

    print("Division : ",c)

except :
    print("Exception Error")
    print("End Code")

'''
'''
try :
    print("Start Code")

    a = int(input("Enter a First Number : "))
    b = int(input("Enter a Second Number : "))

    c = a/b

    print("Division : ",c)

except ZeroDivisionError as e :
    print("Exception Error",e)
except ValueError as e :
    print("Exception Error",e)
    print("End Code")
'''

try :
    print("Start Code")

    a = int(input("Enter a First Number : "))
    b = int(input("Enter a Second Number : "))

    c = a/b

    print("Division : ",c)

except Exception as e :
    print("Exception Error",e)

    print("End Code")
