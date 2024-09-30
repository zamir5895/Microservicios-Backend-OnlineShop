class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@localhost:3306/administrador"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "mysecretkey"
