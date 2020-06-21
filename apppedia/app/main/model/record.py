from .. import db
import datetime

class Record(db.Model):
    """ Record Model for storing record related details """
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255), unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    user_email = db.Column(db.String(255))
    content = db.Column(db.String(255))

    def __repr__(self):
        return "<record '{}'="">".format(self.content)