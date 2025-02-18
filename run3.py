# from flask_migrate import Migrate
from os import environ
from sys import exit
from config import config_dict
from app import create_app, db

get_config_mode = environ.get('APPSEED_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid APPSEED_CONFIG_MODE environment variable entry.')




app = create_app(config_mode) 

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=9900)
