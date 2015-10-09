
class BugReport:
    """Particular bug report class, contain all mandatory attributes and methods"""
    bug_id = 0
    time_open = 0
    bug_status = ''
    opened_by = ''
    time_fixed = ''
    assigned_to = ''
    crated_by = ''
    descripotion = ''
    title = ''
    def __init__(self,report_title,report_description):
        self.title = report_title
        self.descripotion = report_description
        #time_open = now
        #crated_by = who 
    """Set current bug report status"""   
    def set_status(self, status):
        pass
    """Assign bog report to some person( assigted to bug creator by default)"""
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

