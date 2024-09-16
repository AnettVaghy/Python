name = input("tipe your name")
print("wellcome", name, "to your adventure")
answer = input("You are on a dirt road, you can go left or right. Where you want to go? ")
if answer == "left":
    print("you are done")
elif answer == "right":
    
    answer = input("you come to ariver. You can walk around it or you can swim. What will you do? ")

    if answer == "swim":
        print("you swim across and you are eaten by an aligator")
    elif answer == "walk":
        print("you walked a lot and you got lost")
    else:   
         print("your choice is not an option")
else:
    print("your choice is not an option")