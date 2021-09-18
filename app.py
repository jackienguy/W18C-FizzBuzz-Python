def divisable_nums(number_array):
    for number in number_array:
        if ((number % 3 == 0) and (number % 5 == 0)):
            print("BuzzFizz")
        elif (number % 5 == 0):
            print("Buzz")
        elif (number % 3 == 0):
            print("Fizz")
        else:
            print("Not divisible by 3 or 5")

numbers = [15, 12, 32, 38, 45, 85, 83, 19, 100, 71, 48, 18, 30, 52, 60]

divisable_nums(numbers)