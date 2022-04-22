from App.models import Report
from App.database import db

def make_report(type, location, time, name, date, phonenum):
    newreport = Report(type=type, location=location, time=time, name=name, date=date, phonenum=phonenum)
    db.session.add(newreport)
    db.session.commit()

def get_all_reports():
    return Report.query.all()
