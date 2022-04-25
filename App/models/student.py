from App.database import db

class Student(db.Model):
    studentId = db.Column(db.String, primary_key=True)
    first_name =  db.Column(db.String(120), nullable=False)
    last_name =  db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Student {self.studentId} - {self.first_name}>' 

    def toDict(self):
        return{
            'sudent_id': self.studentId,
            'first_name': self.first_name,
            'last_name':self.last_name,
            'email': self.email
        }