from App.models import listing, User, Report
from App.database import db

def list_report(report, user):
    user.listing.append(report)
    db.session.add(newListing)
    db.session.commit()