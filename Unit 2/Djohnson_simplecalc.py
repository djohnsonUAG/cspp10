c = input("enter a three digit equation: ")

digit_one = int(c[0])
operator = c[1]
digit_two = int(c[2])


if operator == "+":
    result = digit_two + digit_one
    print("The result is {}.".format(digit_one+digit_two))
elif operator == "-":
    result = digit_two - digit_one
    print ("The result is {}.".format(digit_one-digit_two))
elif operator == "*":
     result = digit_two * digit_one
     print ("The result is {}.".format(digit_one*digit_two))
elif operator == "/":
     result = digit_two / digit_one
     print ("The result is {}.".format(digit_two/digit_one))
elif operator == "%":
     result = digit_two % digit_one
     print ("The result is {}.".format(digit_one%digit_two))