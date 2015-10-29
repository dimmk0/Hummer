from bugtracker import BugTracker
import sys
class Menu:
    """Display menu and respond choises when run"""
    def __init__(self):
        self.BT = BugTracker()
        self.choises = {
                   1: self.show_reports,
                   2: self.search_reports,
                   3: self.add_report,
                   4: self.show_report,
                   5: self.quit 
                   }
    def display_menu(self):
        print("""
***Hummer bugtracker***

      MENU

1. Show all bugreports.
2. Search bugreports.
3. Add bugreport.
4. Show report.
5. Quit
""")
   
    def run(self):
        while True:
            self.display_menu()
            choise = input("Enter an option: ")
            action = self.choises.get(choise)
            #print action
            if action:
                 action()
            else:
                 print("{0} is not valid choise".format(choise))  

    def show_reports(self):
        self.BT.list_reports() 
    def search_reports(self):
        self.BT.search_reports()
    def add_report(self):
        self.BT.create_new_report()
    def edit_report(self):
        pass
    def show_report(self):
        report_id = input("Enter Report Id: ")
        try:
            report_id = int(report_id)
        except ValueError:
            print("That's not a valid report id!")
        
        report = self.BT.select_report(report_id)
        if report != 0: 
            report.show_report()
        else:
            print("No valid report found.")

    def quit(self):
        print("Thank you for using Hummer!")
        sys.exit(0) 
