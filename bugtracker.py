import pickle
from  bugreport import BugReport
 
REPORTS_PATH = "./database"

class BugTracker:
    bug_reports = []
    #current_report BugReport

    def __init__(self):
        pass
        self.load_reports()

    def create_new_report(self):

#        report_title = raw_input("Please, enter bugreport title:")
#        report_desc = raw_input("Please, enter bugreport description:")
   
        self.current_report = BugReport("dimm",self.get_next_report_id())
        self.bug_reports.append(self.current_report)
        
        self.save_reports()
    
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
            print report.report_id,"	",report.title,report.description
    def get_next_report_id(self):
        max_report_id = 0
        for report in self.bug_reports:
            if report.report_id > max_report_id:
                max_report_id = report.report_id
        return max_report_id+1

