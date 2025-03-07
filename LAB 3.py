print("Hello! how are you? Can I know your name?")

name = input("Enter your name:")
print("Hello,"+name,"can you insert any number and I'll say if it's odd or even!")

while True:
    check_number = (int(input("Insert number:")))
    check_number = abs(check_number)
    
    if check_number % 2 == 0:
        print("number", + check_number, "is an even number!")
        
    else:
        print("number", +check_number,"is an odd number!")