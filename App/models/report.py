from App.database import db
from datetime import datetime


class Report(db.Model):
    reportId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    details = db.Column(db.String(400), nullable=False)
    date = db.Column(db.String(50),  nullable=False)
    listing = db.relationship('Listing', backref=db.backref('report', lazy='joined'))
    
    def __repr__(self):
        return f'<Report {self.name} {self.type} {self.location} {self.date} {self.details}>' 

    def toDict(self):
        return{
            'id': self.reportId,
            'name': self.name,
            'type': self.type,
            'location': self.location,
            'time': self.time,
            'date': self.date,
            'details': self.details
        }
