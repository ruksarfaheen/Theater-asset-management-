from theatre import user  

def main():
    print("\nHello Welcome!")

    
    User = user("SLN", "Sangam circle", "Digital projector for screening", 3, "Regular upkeep of theater",
                 "dolby 7.1", "CCTV Surveillance",250, "XXX available")

    while True:
        user_type = int(input("\nAre you a customer or a manager?\nIf customer enter 1\nIf manager enter 2:\n "))

        if user_type == 1:
            User.display_details()

        elif user_type == 2:
            User.display_details()
            changes=int(input("\nSelect option\n1.Modify Details\n2.Add Details\n3.Delete Details\n4.None\nEnter the the option:"))
            
            if changes==1:
                modify = int(input("\nDo you want to modify details? \nIf yes enter 1\nIf no enter 2:\n "))

                if modify == 1:
                    attempts = 3
                    Password = 1234
                    for i in range(attempts):
                        password = int(input("Enter password:"))

                        if password == Password:
                            while True:
                                update_detail(User)
                                more_updates = input("\nDo you want to update more details? (yes/no): ").lower()
                                if more_updates != 'yes':
                                    break

                            print("\nUpdated Theatre Details Successfully:")
                            User.display_details()
                            break

                        else:
                            print("Wrong password. Try again:")

                    else:
                        print("Sorry. Access denied.")

                else:
                    print("Thank you")  
            
            elif changes==2:
                add=int(input("\nDo you want to add details? \nIf yes enter 1\nIf no enter 2:\n "))
                if add==1:
                    while True:
                        add_details(User)
                        add_more=input("\nDo you want to add more details?(yes/no):").lower()
                        if add_more=="yes":
                            continue
                        print("\n new details are added successfully:")
                        User.display_details()
                        break
                    
                else:
                    print("thank you")
                    
            elif changes==3:
                delete=int(input("\nDo you want to delete any details? \nIf yes enter 1\nIf no enter 2:\n "))
                if delete==1:
                    lock=1234
                    Lock=int(input("Enter password:"))
                    if Lock==lock:
                        while True:
                            delete_details(User)
                            more_deletes=input("\nDo you want to delete more details? (yes/no):").lower()
                            if more_deletes=="yes":
                                continue
                            print("\n Entered Details are deleted successfully.")
                            
                            break
                        
                    else:
                        print("Wrong password")
                else:
                   print("Thank you")
            elif changes==4:
                print("OK.Thank you.")
            else:
                print("Not found.")
                                                                                                                                                         

        else:
            print("Invalid User")

        exit_option = input("\nEnter 'exit' to quit or press 1 to continue: ").lower()
        if exit_option == 'exit':
            break


def update_detail(user_details):
    print("\nUpdate Theatre Details:")
    choice = input("Which detail would you like to modify? (name/location/projector/screens/sound/seats/status): ")
    if choice == 'name':
        user_details.set_name(input("Enter new theatre name: "))
    elif choice == 'location':
        user_details.set_location(input("Enter new location: "))
    elif choice == 'projector':
        user_details.set_projector(input("Enter new projector type: "))
    elif choice == 'screen':
        user_details.set_num_screen(int(input("Enter new number of screens: ")))
    elif choice == 'sound':
        user_details.set_sound(input("Enter new sound system details: "))
    elif choice == 'seats':
        user_details.set_seats(int(input("Enter new number of seats available: ")))
    elif choice == 'status':
        user_details.set_status(input("Enter new status: "))
    else:
        print("Invalid choice!")
        
def add_details(user_details):
    print("\nAdd new details:")
    detail=input("Which detail would you like to add?\n(parking/food counter):\n")
    if detail=="parking":
        user_details.add_parking(input("Enter details about parking:"))
    elif detail=="food counter":
        user_details.add_food(input("Enter details about food counter:"))
    else:
        print("no such detail")
        
def delete_details(user_details):
    print("\nDelete details")
    delete=input("Which detail would you like to delete?\n(name/location/projector/screens/sound/seats/status): ")
    if delete=="name":
        user_details.set_name(" ")
        print("\nTheatre name deleted successfully.")
    elif delete=="location":
        user_details.set_location(" ")
        print("\nLocation deleted successfully.")
    elif delete=="projector":
        user_details.set_projector(" ")
        print("\nProjector deleted successfully")
    elif delete=="screen":
        user_details.set_num_screen(0)
        print("\nscreens deleted successfully.")
    elif delete=="sound":
        user_details.set_sound(" ")
        print("\nsound deleted successfully.")
    elif delete=="cleaning":
        user_details.set_cleaning(" ")
        print("\n cleaning deleted successfully.")
    elif delete=="seats":
        user_details.set_seats(0)
        print("\nseats deleted successfully.")
    elif delete=="security":
        user_details.set_security(" ")
        print("\nsecurity deleted successfully.")
    elif delete=="status":
        user_details.set_status(" ")
        print("\nstatus deleted successfully.")
    else:
        print("\nNo such detail")
    
    
if __name__== "_main_":
    main()