from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    student = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    text = db.Column(db.String(700), nullable=False)
    author = db.relationship('User', backref=db.backref('recommendations', lazy='joined'))

    def __repr__(self):
        return f'<Recommendation {self.studentId} - {self.first_name}>' 

    def toDict(self):
        return{
            'id': self.id,
            'author': self.username
        }

