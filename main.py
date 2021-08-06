# Fuzz-Bizz game in which kids say fizz if no div by 3 & buzz if div by
# 5 and if div by both then say BuzzFizz

user_input = int(input("Enter the No:"))


for numbers in range(user_input):
    if (numbers % 3) == 0 and (numbers % 5) != 0:
        print("Fizz", "\n")

    elif (numbers % 3) != 0 and (numbers % 5) == 0:
        print("Buzz", "\n")

    elif (numbers % 3) == 0 and (numbers % 5) == 0:
        print("FizzBuzz", "\n")

    else:
        print(numbers, "\n")
