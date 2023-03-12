import os


class Settings:
    VERSION = '0.0.1'
    APP_TITLE = 'APP NAME'
    PROJECT_NAME = 'PROJECT NAME'
    APP_DESCRIPTION = 'APP DESCRIPTION'

    SERVER_HOST = 'localhost'

    DEBUG = True

    APPLICATIONS = [
        'here pas our app from `applications` folder'
    ]

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(BASE_DIR, "app/logs")
    TEMP_FOLDER = f"{BASE_DIR}/temp/" 
    
    
    DB_URL = 'our db url'
    DB_CONNECTIONS = {
            'default': {
                'engine': '',
                'db_url': DB_URL,
                'credentials': {
                    'host': '',
                    'port': '',
                    'user': '',
                    'password': '',
                    'database': '',
                }
            },
        }

    APPLICATIONS_MODULE = 'app.applications'


settings = Settings()
