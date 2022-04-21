from main import db,bcrypt,loggin_manager
from flask_login import UserMixin

@loggin_manager.user_loader
def load_user(user_id):
    return 

class User(db.Document, UserMixin):
    username = db.StringField(required = True, unique = True,  
    nullable = False, min_length = 2, max_length =30)
    
    email_address = db.StringField(required = True, unique = True,  nullable = False, min_length = 2, max_length =30)
    
    password_hash= db.StringField(required = True, nullable = False, max_length =60)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


