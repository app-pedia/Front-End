from .. import db

class Contact(db.Model):
    """ Contact Model for storing contact related details """
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255), unique=True)
    user_email = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.String(4095))

    def __repr__(self):
        return "<contact '{}'="">".format(self.content)