#  take two inputs, first_number and second_number.
# if the sum of the two numbers is greater than or equal to 10,
# print product of the two, if sum is less than 10, subtract first number from second.

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number: "))
sum_of_numbers = sum([first_number,second_number])
if sum_of_numbers > 10:
    print("Product of numbers: ", first_number * second_number)
elif sum_of_numbers == 10:
    print(first_number, second_number)
else:
    print("diffrence: ", first_number - second_number)