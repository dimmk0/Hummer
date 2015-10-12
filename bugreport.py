
import sys, tempfile, os
from subprocess import call

EDITOR = os.environ.get('EDITOR','vim')

class BugReport:
    """Particular bug report class, contain all mandatory attributes and methods"""
    report_id = 0
    time_open = 0
    report_status = 'none'
    opened_by = ''
    time_fixed = ''
    assigned_to = ''
    crated_by = ''
    description = ''
    title = ''
  
    def __init__(self,report_id=1):
         """Enter report title"""
         while True:
             self.title = raw_input("Please, enter bugreport title:")
             if len(self.title) == 0:
                 print 'Empty string; please enter title again'
             else:
                 break
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

        #self.report_status = report_status_list[0]
        #time_open = now
        #crated_by = who 
    """Set current bug report status"""   
    def set_status(self, status):
        if status in report_status_list:
            self.report_status = status
    """Assign bug report to some person (assigned to bug creator by default)"""
    def assign_to(self):
        pass
    """Run editor and save Description of bug"""
    def set_description(self):
        pass
    """Set report title"""
    def set_title(self):
        pass
    """Add comment"""
    def add_comment(self):
        pass


report_status_list = ['Open','Assigned','Fixed','Verified']
