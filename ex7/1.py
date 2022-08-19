print("Youre in a dark alley. Where do you go?")
print("(1) left (2) straight (3) right (4) down")
choice = input("choose: ")
choice_1=str("u go left and die")
choice_2=str("u go straight and there is another crossing")
choice_3=str("u go right and theres a wall ")

if choice == "1":
   print("u go left and die")
elif choice == "2":
   print("u go straight and there is another crossing")
   #continue tree here
elif choice == "3": 
    print("u go right and theres a wall"+ "and " + " Now you will have another choice")
    

    choice=input("what step would you like to go back to: ")
    if choice=="1":
            print(choice_1)
    elif choice=="2":
            print(choice_2)

elif choice == "4": 
    print("you are doomed my fried"+" Now you will have another choice")
    

    choice=input("what step would you like to go back to: ")
    if choice=="1":
            print(choice_1)
    elif choice=="2":
            print(choice_2) 
    elif choice=="3":
        print(choice_3)                   
      
else:
    print("u just die for inaction")
