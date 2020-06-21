from .. import db

class Function(db.Model):
    """ Function Model for storing function related details """
    __tablename__ = "function"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255), unique=True)
    application_public_id = db.Column(db.String(255))
    detail = db.Column(db.String(511))

    def __repr__(self):
        return "<related '{}'="">".format(self.detail)