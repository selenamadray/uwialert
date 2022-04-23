from App.database import db

class Listing(db.Model):
    listingId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    reportId = db.Column(db.Integer, db.ForeignKey('report.reportId'))

def __init__(self, userId, reportId):
        self.userId = userId
        self.reportId = reportId

def __repr__(self):
    return f'<listing {self.listingId} - {self.report.type} - listed by {self.user.username}>'

def toDict(self):
    return{
         'listingID': self.listingId,
         'userId': self.userId,
         'reportId':self.reportId,
    }
