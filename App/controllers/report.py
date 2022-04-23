from App.models import Report
from App.database import db

def make_report(name, type, location, date, details):
    newreport = Report(name=name, type=type, location=location, date=date, details=details)
    db.session.add(newreport)
    db.session.commit()

def get_all_reports():
    return Report.query.all()
