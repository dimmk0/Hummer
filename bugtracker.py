import pickle
from  bugreport import BugReport
 
REPORTS_PATH = "./database"

class BugTracker:
    bug_reports = []
    #current_report BugReport

    def __init__(self):
        self.load_reports()

    def create_new_report(self):

        report_title = raw_input("Please, enter bugreport title:")
        report_desc = raw_input("Please, enter bugreport description:")
   
        self.current_report = BugReport(report_title,report_desc)
        self.bug_reports.append(self.current_report)
        
        save_reports()
    
    def load_reports(self):
        with open(REPORTS_PATH+"/reports.bin", "rb") as f:
            self.bug_reports = pickle.load(f)

    def save_reports(self):
        with open(REPORTS_PATH+"/reports.bin", "wb") as f:
            pickle.dump(self.bug_reports,f)
        
    def select_report(self):
        pass    
    def search_reports(self):
        pass
    def list_reports(self):
        for report in self.bug_reports:
            print(report.bug_id,"\t",report.title)
