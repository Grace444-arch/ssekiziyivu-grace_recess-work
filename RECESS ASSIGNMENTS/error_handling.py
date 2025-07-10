print("_______Dividing program_______")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

while num1==0 or num2==0:
    print("Zero is not a valid number!!!")
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    
print(f"Answer:{num1/num2}")    
