from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models import listing

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    listing = db.relationship('Listing', backref=db.backref('user', lazy='joined'))
    is_active = db.Column(db.Boolean, default=False, nullable=False)

    def _init_(self, username, password):
        self.username = username
        self.set_password(password)
        self.email = email

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def is_authenticated(self):
        return True;

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)