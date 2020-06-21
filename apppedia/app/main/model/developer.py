from .. import db

class Developer(db.Model):
    """ Developer Model for storing developer related details """
    __tablename__ = "developer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255), unique=True, nullable = False)
    name = db.Column(db.String(255))
    country = db.Column(db.String(255))
    address = db.Column(db.String(255))
    web = db.Column(db.String(255))
    rating_total = db.Column(db.String(255))
    rating_average = db.Column(db.String(255))
    install_achieved = db.Column(db.String(255))

    def __repr__(self):
        return "<developer '{}'="">".format(self.name)