import os
import re


class Main:
    def display_main_menu(self):
        self.go_to_menu()

    def go_to_menu(self):
        menu = '''
        WELCOME TO ONWARD HOSPITAL
        1 -> Register
        2 -> Login
        3 -> Logout
        '''
        print(menu)
        self.input_menu()

    def input_menu(self):
        choice = input("Select a number if you would like to register or login to logout?")
        match(choice[0]):
            case '1': self.register()
            case '2': self.login()
            case '3': self.log_out()
            case _: print("Invalid input try again")
        self.go_to_menu()

    def register(self):
        pass

    def login(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        patient_id = input("Enter your ID: ")
        name = first_name + " " + last_name
        if self.validate_name(name) and self.validate_id:
            self.access_dashboard()
        else:
            print("Invalid login details entered")
            self.login()

    def validate_name(self, name):
        pass

    def validate_id(self, id):
        pass

    def log_out(self):
        quit()

    def access_dashboard(self):
        login = '''
        WELCOME TO ONWARD HOSPITAL
        1. Book a specialist
        2. View appointment schedules
        3. Get your ID
        4. Logout
        '''


