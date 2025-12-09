# How to find the year is a leap year or not
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")


# finding the giving alphabet is vowel or consonant

alpha = input("Enter an alphabet: ")
vowels = "aeiouAEIOU"
if alpha in vowels:
    print(alpha, "is a vowel.")
else:
    print(alpha, "is a consonant.")

# find the number is even or odd

number =int(input("Enter a Number"))
if number %2==0 :
    print ("it is a even number")
else:
    print ("it is  a Odd Number")




