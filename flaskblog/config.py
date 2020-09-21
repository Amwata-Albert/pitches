import os
class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jim:12139@localhost/trialpitch'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mutahijames0@gmail.com'
    MAIL_PASSWORD = '12139Lenana'
    UPLOADED_PHOTOS_DEST = 'app/static/photos' 

class ProdConfig(Config) :
  '''
  Production configuration child class
  
  Args: 
    config : The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")   


class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jim:12139@localhost/trialpitch'


class DevConfig(Config) :
  '''
  Development configuration child class 
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jim:12139@localhost/trialpitch'
  DEBUG = True #enable debug mode in my app 

config_options = {
  'development' : DevConfig,
  'production' : ProdConfig,
  'test':TestConfig
}