import pickle
import sys
import os
from  bugreport import BugReport
 
REPORTS_PATH = "./database"

class BugTracker:
    bug_reports = []
    #current_report = 0

    def __init__(self):
        self.username = raw_input("Please enter registered user name:")
        if not self.validate_user(self.username):
            print("User %s is not allowed to use Hummer" % self.username)
            sys.exit()
        
        self.load_reports()

    def create_new_report(self):
        """New incstance of BugReport created and saved to database"""
        self.current_report = BugReport(self.username,self.get_next_report_id())
        self.bug_reports.append(self.current_report)
        
        self.save_reports()
    
    def load_reports(self):
        """Load whole report list from database"""
        with open(REPORTS_PATH+"/reports.bin", "rb") as f:
            if  os.stat(REPORTS_PATH+"/reports.bin").st_size > 10:
                self.bug_reports = pickle.load(f)
            else:
                print (REPORTS_PATH+"/reports.bin is empty, no reports loaded")

    def save_reports(self):
        """Save whole report list to database"""
        with open(REPORTS_PATH+"/reports.bin", "wb") as f:
            pickle.dump(self.bug_reports,f)
        
    def select_report(self,report_id):
        """select some particular report to review and edit it"""
        current_report = 0
        for report in self.bug_reports:
            print("Check report %s" % report.report_id)
            if report.report_id == report_id:
                current_report = report

        if current_report <> 0:
            return current_report
        else:
            print ("Report with id: ",report_id, " not found.")
            return 0 

    def search_reports(self):
        pass
    def list_reports(self):
        """listing of all existing reports in database"""
        for report in self.bug_reports:
            print ('_'*100)    
            print ("%s  %s  %s  %s  %s  %s" % (report.report_id,report.title, report.opened_by, report.assigned_to, report.report_status,report.time_open))
            print ('_'*100)    
    def get_next_report_id(self):
        """Get next available report id"""
        max_report_id = 0
        for report in self.bug_reports:
            if report.report_id > max_report_id:
                max_report_id = report.report_id
        return max_report_id+1
    def validate_user(self,user):
        """Check if user presented in list of regitered users"""
        with open(REPORTS_PATH+"/users", "r") as f:
            users = f.read().splitlines()
        if user in users:
            return True
        else:
            return False

