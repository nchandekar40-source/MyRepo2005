#Write a program for loop even numbers#
total_sum = 0  

for number in range(1, 51):
    if number % 2 == 0:
        total_sum += number  

print("The sum of all even numbers between 1 and 50 is:", total_sum)