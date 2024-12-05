from lib.skelly_hi import skelly_hi
from lib.skelly_bye import skelly_bye


class App:
    def __init__(self):
        # Book.create_table()
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

        while self.input not in ["1", "2", "3", "4", "5", "6"]:

            self.input = input(">>> ")

            if self.input == "1":
                self.manage_user()
                sleep(2)
                print(printed_options)
            elif self.input == "2":
                self.advanced_directive_setup() 
                sleep(2)
                print(printed_options)
            elif self.input == "3":
                self.organize_funds()
                sleep(2)
                print(printed_options)
            elif self.input == "4":
                self.handle_digital()
                sleep(2)
                print(printed_options)
            elif self.input == "5":
                self.task_overview() 
                sleep(2)
                print(printed_options)
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

    def advanced_directive_setup(self):
        advanced_directive_opts = """
        1. Create New Directive
        2. Delete Directive
        3. View All Directives
        4. Find Directive by Representative Name
        5. Return to Main Menu
        """
        print(advanced_directive_opts)

    def organize_funds(self):
        fund_opts = """
        1. Create Emergency Fund Plan
        2. View Emergency Fund Status
        3. Return to Main Menu
        """
        print(fund_opts)

    def handle_digital(self):
        digital_opts = """
        1. Declare/Update Very Trusted Person (VTP)
        2. Delete VTP
        3. Return to Main Menu     
        """
        print(digital_opts)

    def task_overview(self):
        task_opts = """
        1. View All Tasks
        2. Print Checklist
        3. Return to Main Menu
        """
        print(task_opts)

    def exit_program(self):
        print(skelly_bye)
        print("   Have fun dying,")
        print("   Goodbye!")
        exit()
