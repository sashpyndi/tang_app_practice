from database import db

class Task(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    description = db.Column("description", db.String(2000))
    status = db.Column("status", db.String(50))

    def __init__(self, title, description,status):
        self.title = title
        self.description = description
        self.status = status

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email