from bugtracker import BugTracker

class Menu:
    """Display menu and respond choises when run"""
    def __init__(self)
        self.BT = BugTracker()
        self.choises = {
                   "1": self.show_reports,
                   "2": self.search_reports,
                   "3": self.add_report,
                   "4": self.edit_report,
                   "5": self.qiut
                   }
    def display_menu(self):
        print("""
***Hummer bugtracker***

      MENU

1. Show all bugreports.
2. Search bugreports.
3. Add bugreport.
4. Modify bugreport
5. Quit
""")
   
   def run(self):
       while True:
           self.display_menu()
           choise = input("Enter an option: ")
           action = self.choises.get(choise)
           if action:
                action()
           else:
                print("{0}is not valid choise".format(choise))  

