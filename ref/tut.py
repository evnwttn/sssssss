
# age = 20
# first_name = "ned"
# is_online = False

# name = input("What is your name? ")
# print("Hello " + name)

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# input returns a string ie. "1982" vs 1982

# int() - 9
# float() - 9.99 (floating point number)
# bool() - converting value to boolean
# str() - converting value to string

# current_year = 2022

# birth_year = input("Enter your birth year: ")
# age = current_year - int(birth_year)
# print(age)

# first_number = input("Enter the first number: ")
# second_number = input("Enter the second number ")
# sum = (float(first_number) + float(second_number))
# print("The sum is " + str(sum))

# first_number = float(input("Enter the first number: "))
# second_number = float(input("Enter the second number: "))
# sum = first_number + second_number
# print(sum)

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# name = "Evan Watton"

# evan watton
# 012345678910

# print(name.find("van W"))
#
# will return 1
# case sensitive, will return -1 if does not exist

# print(name.replace("a", "4").replace("o", "0"))

# print("van" in name)
# returns boolean if true

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# arithmetic operators

# / - returns floating point number (ie. 3.3333333334)
# // - returns whole int number (ie. 3)
# % mod operator returns remainder of division (ie. 10 % 3 = 1)
# ** exponent operator (ie. 10 ** 3 = 1000)

# x = 10
# x = x + 3

# print(x)

# x = 10
# x += 3
# augmented assignment operator
# (-= += *=)

# print(x)

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# comparison operators

# x = 3 > 2
# print(x)
# returns bool as true

# x = 3 == 2 equality operator
# returns bool as false

# x = 3 != 2 inequality operator
# returns bool as true

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# logical operators
# and // or // not

# price = 10
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)

# not - inverse operator

# price = 5
# print(not price > 10)
# returns true

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# if statements

# temperature = -5

# if temperature >= 30:
#     print("it's a hot day, damn")
# elif temperature >= 20 and temperature < 30:
#     print("it's a ok out there")
# elif temperature >= 10:
#     print("it's a lil chilly my guy")
# elif temperature < 10:
#     print("well blessid christ")
# print("done")

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# exercise

# weight = input("Weight: ")
# unit = input("(K)g or (L)bs: ")

# if unit.upper() == "K":
#     converted_weight = (float(weight) / 0.453592)
#     print("Weight in lbs: " + str(converted_weight))
# elif unit.upper() == "L":
#     converted_weight = (float(weight) * 0.453592)
#     print("Weight in kgs: " + str(converted_weight))
# else:
#     print("Please enter a valid unit")

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# while loops

# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# lists

# names = ["Katie", "Evan", "Otis", "Gord", "Janet"]
# names[0] = "KT"
# first_three = names[0:3]
# print(first_three)

# list methods

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(0, 6)
# numbers.remove(3)
# numbers.clear()
# print(1 in numbers)  # returns bool
# print(len(numbers))

# print(numbers)

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# for loops

# numbers = [1, 2, 3, 4, 5]

# for item in numbers:
#     print(item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# range()

# numbers = range(5)
# for number in numbers:
#     print(number)

# numbers = range(5, 10)
# for number in numbers:
#     print(number)  # 5 ---> 9

# numbers = range(5, 10, 2)  # start, finish, step
# for number in numbers:
#     print(number)  # 5, 7, 9

# /////////////////////////////////////////////
# /////////////////////////////////////////////

# tuples
# immutable lists

# numbers = (1, 2, 3)
# parenthesis
# numbers[0] = 10 throws error

# numbers = (1, 2, 3, 3, 3, 3)
# print(numbers.count(3)) # returns 4
