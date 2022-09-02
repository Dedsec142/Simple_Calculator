print("SIMPLE CALCULATOR PROGRAM")

print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Mod ")
ans=input("Enter Choice : ")

print("\n")
if ans == '1' :
    input1=int(input("Enter First Number : "))
    input2 = int(input("Enter Second number Number : "))
    sum=int(input1+input2)
    print("Sum is : " , sum)

elif ans == '2' :
    input1=int(input("Enter First Number : "))
    input2 = int(input("Enter Second number Number : "))
    diff=int(input1-input2)
    print("Difference is : " , diff)

elif ans == '3' :
    input1=int(input("Enter First Number : "))
    input2 = int(input("Enter Second number Number : "))
    mul=int(input1*input2)
    print("Multiplication of numbers is : " , mul)

elif ans == '4' :
    input1=int(input("Enter First Number : "))
    input2 = int(input("Enter Second number Number : "))
    div=float(input1/input2)
    print("Division of Numbers is : " , div)

elif ans == '5' :
    input1=int(input("Enter First Number : "))
    input2 = int(input("Enter Second number Number : "))
    sum=int(input1%input2)
    print("Remainder is : " , sum)

else :
    print("Wrong Input")
    exit(0)
