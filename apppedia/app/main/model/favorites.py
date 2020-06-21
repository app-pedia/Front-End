from .. import db

class Favorites(db.Model):
    """ Favorites Model for storing favorites related details """
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255), unique=True)
    user_email = db.Column(db.String(255))
    application_public_id = db.Column(db.String(255))
    application_name = db.Column(db.String(255))
    application_category = db.Column(db.String(255))
    application_rating_average = db.Column(db.String(255))
    application_image_logo = db.Column(db.String(255))
    application_price = db.Column(db.String(255))

    def __repr__(self):
        return "<favorites '{}'="">".format(self.application_price)