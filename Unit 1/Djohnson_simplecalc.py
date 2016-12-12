num = input("What is the equation:")
op = num[1]
num1 = int(num[0])
num2 = int(num[2])

if op == "+":
    print ("The result is {}".format(num1 + num2))
elif op == "-":
    print ("The result is {}".format(num1 - num2))
elif op == "*":
    print ("The result is {}".format(num1 * num2))
elif op == "/":
    print ("The result is {}".format(num1 / num2))
elif op == "%":
    print ("The result is {}".format(num1 % num2))

    