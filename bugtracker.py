import pickle
from  bugreport import BugReport
 
class BugTracker:
    bug_reports = []
    def __init__(self):
        #reports_file = open("database/reports.txt","r")
        pass

    def create_new_report(self):
        #reports_file = open("database/reports.txt","w")

        report_title = raw_input("Please, enter bugreport title:")
        report_desc = raw_input("Please, enter bugreport description:")
   
        report = BugReport(report_title,report_desc)
        self.bug_reports.append(report)
        
    
    def search_reports(self):
        pass
    def list_reports(self):
        for report in self.bug_reports:
            print(report.bug_id,"\t",report.title)
