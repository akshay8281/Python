'''Qs 6 :- Write python program that swap two number with temp variable and
without temp variable.
'''

a = int(input("\nEnter First Number : "))
b = int(input("Enter Second Number : "))

print("\nBefore Swapping Number : ")

print("a = ",a)
print("b = ",b)

temp = a
a = b
b = temp

print("\nAfter Swapping Number : ")

print("a = ",a)
print("b = ",b)
