
#Calculating the cost of awesome shirts

print("Welcome to Awesome Shirts cost calculator")
#Asking for input for trousers and shirts and validating it
number_shirt = 0
number_trouser = 0

while True:
    #Asking for input and checking if it correct
    shirt = input("Please select the type of shirt you want \n1 Polo\n2 t-shirt\n")
    if shirt in [1,2,"1","2"]:
        break
    else:
        print("You have entered an invalid choice, please try again")
        print("Enter digits only")
        continue
while True:
    color_shirt = input("Please select the color for the shirt\n1 green\n2 red\n3 black\n")
    if color_shirt in [1,2,3,"1","2","3"]:
        break
    else:
        print("You have entered an invalid choice, please try again \n")
        print("Enter digits only")
        continue
while True:
    number_shirt = input("Input the number of shirts you would like to buy\n")
    if number_shirt.isnumeric():
        break
    else:
        print("Please input a number")
        continue
while True:
    #Asing for trousers input
    trouser = input("Please select the type of trousers you want\n1 Cargo  \n2 Jeans\n")
    if trouser in [1,2,"1","2"]:
        break
    else:
        print("You have entered an invalid choice, please try again \n")
        print("Enter digits only")
        continue
while True:
    color_trouser = input("Please select the color for the trousers\n1 Brown\n2 red\n3 black\n")
    if color_trouser in [1,2,3,"1","2", "3"]:
        break
    else:
        print("You have entered an invalid choice, please try again \n")
        print("Enter digits only")
        continue
while True:
    number_trouser = input("Input the number of trousers you would like to buy\n")
    if number_trouser.isnumeric():
        break
    else:
        print("Please input a number")
        continue

#Asking the customer if they are student or a senior
while True:
    student = input("Are you a student or senior citizen? \n1 Student \n2 Senior citizen\n")
    if student in [1,2,"1","2"]:
        break
    else:
        print("You have entered an invalid choice, please try again")
        print("Enter digits only")
        continue

shirt_price = 9.99
trouser_price = 15

#discounts for students 
if student in [1,"1"]:
    if int(number_shirt) < 11:
        #Applying student discount 5% 
        shirt_price = shirt_price*0.95
        shirt_total = shirt_price*int(number_shirt)
    else:
        #Applying quantity discount 15% 
        shirt_price = shirt_price*0.85
        shirt_total = shirt_price*int(number_shirt)
    
    if int(number_trouser) <11:
        #Applying student discount 5%
        trouser_price = trouser_price*0.95
        trouser_total = trouser_price*int(number_trouser)
    else:
        #Applying quantity discount 15%
        trouser_price = trouser_price*0.85
        trouser_total = trouser_price*int(number_trouser)
else:
    if int(number_shirt) < 11:
        #Applying senior discount 10% 
        shirt_price = shirt_price*0.9
        shirt_total = shirt_price*int(number_shirt)
    else:
        #Applying quantity discount 15% 
        shirt_price = shirt_price*0.85
        shirt_total = shirt_price*int(number_shirt)
    
    if int(number_trouser) <11:
        #Applying senior discount 10%
        trouser_price = trouser_price*0.90
        trouser_total = trouser_price*int(number_trouser)
    else:
        #Applying quantity discount 15%
        trouser_price = trouser_price*0.85
        trouser_total = trouser_price*int(number_trouser)

#Applying sales tax
before_tax = shirt_total + trouser_total
after_tax =  before_tax*1.13

#Displaying the infomation

shirt_list = []
trouser_list = []
if int(number_shirt) > 0:
    shirt_list.append("Shirts")
    if shirt in [1,"1"]:
        shirt_list.append("Polo")
    else:
        shirt_list.append("T-Shirt")
    if color_shirt in [1,"1"]:
        shirt_list.append("Green")
    elif color_shirt in [2,"2"]:
        shirt_list.append("red")
    else:
        shirt_list.append("Black")
    shirt_list.append(int(number_shirt))
    if student in [1,"1"]:
        if int(number_shirt) < 11 :
            shirt_list.append("5%")
        else:
            shirt_list.append("15%")
    else:
        if int(number_trouser) < 11:
            shirt_list.append("10%")
        else:
            shirt_list.append("15%")
    shirt_list.append(int(shirt_total))

if int(number_trouser) > 0:
    trouser_list.append("Trouser")
    if trouser in [1,"1"]:
        trouser_list.append("Cargo Pants")
    else:
        trouser_list.append("Jeans")
    if color_trouser in [1,"1"]:
        trouser_list.append("Brown")
    elif color_trouser in [2,"2"]:
        trouser_list.append("Red")
    else:
        trouser_list.append("Black")
    trouser_list.append(int(number_trouser))
    if student in [1,"1"]:
        if int(number_trouser) < 11 :
            trouser_list.append("5%")
        else:
            trouser_list.append("15%")
    else:
        if int(number_trouser) < 11:
            trouser_list.append("10%")
        else:
            trouser_list.append("15%")
    trouser_list.append(int(trouser_total))
    

print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Item", "Type", "Color","Number","Disount","Total"))

print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*shirt_list))
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*trouser_list))

print("Total price before tax is: ",int(before_tax))
print("Total price aftere tax is: ", int(after_tax))