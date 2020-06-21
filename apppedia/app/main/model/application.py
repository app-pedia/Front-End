from .. import db

class Application(db.Model):
    """ Application Model for storing application related details """
    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    public_id = db.Column(db.String(255), unique=True, nullable = False)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    developer_name = db.Column(db.String(255))
    developer_public_id = db.Column(db.String(255))

    rating_total = db.Column(db.String(255))
    rating_average = db.Column(db.String(255))
    rating_five = db.Column(db.String(255))
    rating_four = db.Column(db.String(255))
    rating_three = db.Column(db.String(255))
    rating_two = db.Column(db.String(255))
    rating_one = db.Column(db.String(255))

    install = db.Column(db.String(255))
    install_link = db.Column(db.String(255))

    image_logo = db.Column(db.String(255))

    price = db.Column(db.String(255))
    update_date = db.Column(db.String(255))
    size = db.Column(db.String(255))
    version_current = db.Column(db.String(255))
    version_needs = db.Column(db.String(255))
    contents_grade = db.Column(db.String(255))
    interaction = db.Column(db.String(255))
    in_app_products = db.Column(db.String(255))

    related_name = db.Column(db.String(255))
    related_link = db.Column(db.String(255))

    def __repr__(self):
        return "<application '{}'="">".format(self.description)