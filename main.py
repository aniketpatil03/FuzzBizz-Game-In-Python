# Fuzz-Bizz game in which kids say fizz if no div by 3 & buzz if div by
# 5 and if div by both then say BuzzFizz

numbers = input")


for numbers in range(1, 101):
    if (numbers % 3) == 0 and (numbers % 5) != 0:
        print("Fizz", "\n")

    elif (numbers % 3) != 0 and (numbers % 5) == 0:
        print("Buzz", "\n")

    elif (numbers % 3) == 0 and (numbers % 5) == 0:
        print("FizzBuzz", "\n")

    else:
        print(numbers, "\n")
