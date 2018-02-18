from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    todos = db.relationship('Todo', backref='user', lazy='select')

    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id, self.name)
