""" Q:5 Write a program that prints out the calls for a spaceship that is about to launch.
Countdown from 10 to 1 and then output Liftoff!
Here's a sample run of the program:
10 9 8 7 6 5 4 3 2 1 Liftoff!
There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable i. Recall that i will keep track of 
how many times the for loop has completed executing its body. As an example this code:
for i in range(10): print(i)
Will print out the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. 
The values printed in liftoff are 10 minus the number of times the for loop has completed.
"""
for i in range(10, 0, -1):
    print(i, end=" ")

print("Liftoff!")


"""Write a program that asks a user to enter a number. 
Your program will then double that number and print out the result.
 It will repeat that process until the value is 100 or greater.
For example if the user enters the number 2 you would then print:
4 8 16 32 64 128
Note that:
2 doubled is 4
4 doubled is 8
8 doubled is 16
and so on.
We stop at 128 because that value is greater than 100.
Maintain the current number in a variable named curr_value.
When you double the number, you should be updating curr_value.
Recall that you can double the value of curr_value using a line like:
curr_value = curr_value * 2
This program should have a while loop and the while loop condition should test if curr_value is less than 100.
Thus, your program will have the line:
while curr_value < 100:"""

# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Loop until curr_value is 100 or greater
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=" ")
