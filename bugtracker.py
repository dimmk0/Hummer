import pickle
from  bugreport import BugReport
 
REPORTS_PATH = "./database"

class BugTracker:
    bug_reports = []
    #current_report BugReport

    def __init__(self):
        self.load_reports()

    def create_new_report(self):
        """New incstance of BugReport created and daved to database"""
        self.current_report = BugReport("dimm",self.get_next_report_id())
        self.bug_reports.append(self.current_report)
        
        self.save_reports()
    
    def load_reports(self):
        """Load whole report list from database"""
        with open(REPORTS_PATH+"/reports.bin", "rb") as f:
            self.bug_reports = pickle.load(f)

    def save_reports(self):
        """Save whole report list to database"""
        with open(REPORTS_PATH+"/reports.bin", "wb") as f:
            pickle.dump(self.bug_reports,f)
        
#    def select_report(self):
#        """select some particular report to review and edit it"""
#        pass    
    def search_reports(self):
        pass
    def list_reports(self):
        """listing of all existing reports in database"""
        for report in self.bug_reports:
            print report.report_id,"	",report.title,report.description
    
    def get_next_report_id(self):
        """Get next available report id"""
        max_report_id = 0
        for report in self.bug_reports:
            if report.report_id > max_report_id:
                max_report_id = report.report_id
        return max_report_id+1

