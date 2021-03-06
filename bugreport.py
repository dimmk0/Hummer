from datetime import datetime
import sys, tempfile, os, textwrap
from subprocess import call

EDITOR = os.environ.get('EDITOR','vim')

class BugReport:
    """Particular bug report class, contain all mandatory attributes and methods"""
    report_id = 0
    title = ''
    description = ''
    report_status = 'none'
    time_fixed = 0
    assigned_to = ''
  
  
    def __init__(self,opened_by_user,bugreport_id):
        self.report_id = bugreport_id
        self.set_title()
        self.set_description()
        self.report_status = report_status_list[0]
        self.time_open = datetime.now()
        self.opened_by = opened_by_user 
        self.assign_to(opened_by_user)
 
    """Set current bug report status"""   
    def set_status(self, status):
        if status in report_status_list:
            self.report_status = status
    """Assign bug report to some person (assigned to bug creator by default)"""
    def assign_to(self,assigned):
        self.assigned_to = assigned

    """Run editor and save Description of bug"""
    def set_description(self):
         """Enter description/ this will run editor to enter muttiline bug description """
         while True:
             with tempfile.NamedTemporaryFile(suffix=".tmp") as temporary_file:

                 temporary_file.write("")
                 temporary_file.flush()
                 call([EDITOR, temporary_file.name])

                 self.description =  temporary_file.read() 
 
             if len(self.description) == 0:
                 print 'Empty string; please enter description again'
             else:
                 break

    """Set report title"""
    def set_title(self):
         """Enter report title"""
         while True:
             self.title = raw_input("Please, enter bugreport title:")
             if len(self.title) == 0:
                 print 'Empty string; please enter title again'
             else:
                 break
        
    """Add comment"""
    def add_comment(self):
        pass
    def show_report(self):
        os.system('cls') 
        print('_'*100)
        print(self.title)
        print('_'*100)
        print('Opened by: %s	Opened at: %s' % (self.opened_by,self.time_open))
        print('Assigned to: %s	Staus: %s' % (self.assigned_to,self.report_status) )
        print('_'*100)
        print(textwrap.fill(self.description,100))
        print('_'*100)
        print('_'*100)

""" List of possible bug statuses """
report_status_list = ['Open','Assigned','Fixed','Verified','Closed']
