from lib.skelly_hi import skelly_hi
from lib.skelly_bye import skelly_bye
from time import sleep
from lib.models.models import User
# , Directive
import ipdb


class App:
    def __init__(self):
        User.create_table()
        # Review.create_table()
        self.input = None
    
    def run(self):
        print(skelly_hi)
        print("Welcome to the Peaceful Death Planner")
        print("")
        self.main_menu()

    def main_menu(self):
        main_menu_opts = """
        1. Manage User Profile
        2. Set Up Advanced Directives 
        3. Organize Emergency Funds
        4. Handle Digital Legacy
        5. Task Overview
        6. Exit
        """
        # define advanced directive at top of submenu

        print("Please choose an option to opt out of optional suffering:")
        print(main_menu_opts)
        self.input = None

        while self.input not in ["1", "2", "3", "4", "5", "6"]:

            self.input = input(">>> ")

            if self.input == "1":
                self.manage_user()
                sleep(2)
                print(main_menu_opts)
            elif self.input == "2":
                self.advanced_directive_setup() 
                sleep(2)
                print(main_menu_opts)
            elif self.input == "3":
                self.organize_funds()
                sleep(2)
                print(main_menu_opts)
            elif self.input == "4":
                self.handle_digital()
                sleep(2)
                print(main_menu_opts)
            elif self.input == "5":
                self.task_overview() 
                sleep(2)
                print(main_menu_opts)
            if self.input == "6":
                self.exit_program()
            else:
                print("Hey, that's not on the menu! Please choose a number based on the menu options")

    def manage_user(self):
        user_menu_opts = """
        1. Create New Profile
        2. Delete Profiles
        3. View All Profiles
        4. Return to Main Menu
        """
        print(user_menu_opts)
        self.input = None

        while self.input not in ["1", "2", "3", "4"]:
            self.input = input(">>> ")

            if self.input == "1":
                self.new_profile()
            elif self.input == "4":
                self.return_main()
            else:
                print("Please choose a number based on the menu options")   
        
    def advanced_directive_setup(self):
        advanced_directive_opts = """
        1. Create New Directive
        2. Delete Directive
        3. View All Directives
        4. Return to Main Menu
        """
        print(advanced_directive_opts)
        self.input = None

        while self.input not in ["1", "2", "3", "4"]:

            self.input = input(">>> ")

            if self.input == "4":
                self.return_main()
            else:
                print("Please choose a number based on the menu options")          

    def organize_funds(self):
        fund_opts = """
        1. Create Emergency Fund Plan
        2. View Emergency Fund Status
        3. Return to Main Menu
        """
        print(fund_opts)
        self.input = None

        while self.input not in ["1", "2", "3"]:

            self.input = input(">>> ")

            if self.input == "3":
                self.return_main()
            else:
                print("Please choose a number based on the menu options")

    def handle_digital(self):
        digital_opts = """
        1. Declare/Update Very Trusted Person (VTP)
        2. Delete VTP
        3. Return to Main Menu     
        """
        print(digital_opts)
        self.input = None

        while self.input not in ["1", "2", "3"]:

            self.input = input(">>> ")

            if self.input == "3":
                self.return_main()
            else:
                print("Please choose a number based on the menu options")

    def task_overview(self):
        task_opts = """
        1. View All Tasks
        2. Print Checklist
        3. Return to Main Menu
        """
        print(task_opts)
        self.input = None

        while self.input not in ["1", "2", "3"]:

            self.input = input(">>> ")

            if self.input == "3":
                self.return_main()
            else:
                print("Please choose a number based on the menu options")

#THE BASIC NAV FUNCTIONS
    def exit_program(self):
        print(skelly_bye)
        print("   Have fun dying,")
        print("   Goodbye!")
        exit()

    def return_main(self):
        self.input = None
        self.main_menu()

#USER PROFILE FUNCTIONS
    def new_profile(self):
        print("Enter your FIRST name (Use the name that appears on your legal documents):")
        self.input = None
        while not self.input or not (3 <= len(self.input) <= 20):
            self.input = input(">>> ")
            if self.input or not (3 <= len(self.input) <= 20): 
                first_name = self.input
            else:
                print ("Invalid input...")

        print("Enter your LAST name (Use the name that appears on your legal documents):")
        self.input = None
        while not self.input or not (2 <= len(self.input) <= 20):
            self.input = input (f">>> {first_name} ")
            if not self.input == (f">>> {first_name} ") or not (3 <= len(self.input) <= 30): 
                last_name = self.input 
            else: 
                print ("Invalid input...")
        
        new_user = User(first_name = first_name, last_name = last_name)
        new_user.save()

        print(f"A profile has been created for {first_name} {last_name}! You can now create and link Advanced Directives to {first_name}. YAY!")
        
        self.input = None

        print(" ")
        sleep(3)
        self.manage_user()
        