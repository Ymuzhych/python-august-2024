tip = int(input("Enter tip amount: "))
    
    if tip_percentage == 15:
       print ("Standard")
    elif tip_percentage == 18:
       print ("Good")
    elif tip_percentage == 20:
        print("Great")
    elif tip_percentage > 20:
       print ("My Hero")
    else:
        return "No specific category for this tip percentage."
