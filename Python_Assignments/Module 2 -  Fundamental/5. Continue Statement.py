# Qs 5 :- What is the purpose continue statement in python?


for i in range(1, 6):
    if i == 3:
        continue
    print(i)

'''
In Python, the continue statement is used to skip the rest of the code inside
a loop for the current iteration and continue to the next iteration of the loop.
It is often used in loops (such as for or while loops) to control the flow of
the loop based on certain conditions.'''

'''
In this example, the for loop iterates over the numbers 1 to 5. When i is equal
to 3, the continue statement is executed, causing the loop to skip the print(i)
statement for that iteration. As a result, the number 3 is not printed, and
the loop continues to the next iteration.
'''
