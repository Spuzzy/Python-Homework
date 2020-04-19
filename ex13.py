from sys import argv

input1 = input("Give me the first var: ")
input2 = input("Give me the second var: ")
input3 = input("Give me the third var: ")

script, var1, var2, var3 = argv

print("The script is called:", script)
print("Your first variable is: ", var1)
print("Your first variable is: ", var2)
print("Your third variable is: ", var3)
print("The first input is ", input1)
print("The second input is ", input2)
print("The third input is ", input3)
