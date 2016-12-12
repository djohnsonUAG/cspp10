word = input("Enter a word:")
number = input("Enter a number:")
if int(number) == 1:
    print("1 "+ word)
elif word[-2:] == "fe":
    print(number + word[:-2]+ "ves")
elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
    print(number + word + "s")
elif word[-1:] == "y":
    print(number + word[:-1]+ "ies")
elif word[-2:] == "sh" or word[-2:] == "ch":
    print(number + word + "es")
else:
    print(number + word + "s")
