from App.database import db


class Report(db.Model):
    studentid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    phonenum = db.Column(db.String(120), nullable=False)
    listing = db.relationship('Listing', backref=db.backref('report', lazy='joined'))
    
    def __repr__(self):
        return f'<Report {self.type} {self.location} {self.time} {self.name} {self.date}>' 

    def toDict(self):
        return{
            'id': self.studentid,
            'type': self.type,
            'location': self.location,
            'time': self.time,
            'name': self.name,
            'date': self.date,
            'phonenum':self.phonenum
            
        }
