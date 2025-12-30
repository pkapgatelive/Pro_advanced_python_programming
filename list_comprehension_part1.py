# create the square of the numbers from 1 to 50 with the even numbers only

square_numbers = [i**2 for i in range(1, 50) if i % 2 == 0]
print(square_numbers)