
import config
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # ...
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))
    # When this property is set, the setter method will call Werkzeug’s
    # generate_password_hash() function and write the result to the password_hash field.
    # Attempting to read the password property will return an error, as clearly the original
    # password cannot be recovered once hashed.
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)