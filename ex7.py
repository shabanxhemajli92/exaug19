print("Youre in a dark alley. Where do you go?")
print("(1) left (2) straight (3) right (4) center (5)down")
choice = input("choose: ")

if choice == "1":
   print("u go left and die")
elif choice == "2":
   print("u go straight and there is another crossing")
   #continue tree here
elif choice == "3": 
   print("u go right and theres a wall")
elif choice == "4":
    print("This is an alley where all the bad people hang out")
    print("Type 5 to have another chance")
    choice=input("what would you like to do now: ")
    if choice == 5:
        print("Now you will have a turning point") 
elif choice == "5":
    print("This might just be a turning point")    
else:
   print("u just die for inaction")