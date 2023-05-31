import logging

from fastapi import FastAPI
# from tortoise.contrib.fastapi import register_tortoise

from app.core.exceptions import APIException, on_api_exception
from app.settings.config import settings
from app.settings.log import DEFAULT_LOGGING
from app.applications.convert.routes import router as convertor
from app.applications.media_type.routers import router as media_type


def configure_logging(log_settings: dict = None):
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)


def get_app_list():
    app_list = [f'{settings.APPLICATIONS_MODULE}.{app}.models' for app in settings.APPLICATIONS]
    return app_list


# def get_tortoise_config() -> dict:
#     app_list = get_app_list()
#     config = {
#         'connections': settings.DB_CONNECTIONS,
#         'apps': {
#             'models': {
#                 'models': app_list,
#                 'default_connection': 'default',
#             }
#         }
#     }
#     return config


# TORTOISE_ORM = get_tortoise_config()


# def register_db(app: FastAPI, db_url: str = None):
#     db_url = db_url or settings.DB_URL
#     app_list = get_app_list()
#     register_tortoise(
#         app,
#         db_url=db_url,
#         modules={'models': app_list},
#         generate_schemas=True,
#         add_exception_handlers=True,
#     )


def register_exceptions(app: FastAPI):
    app.add_exception_handler(APIException, on_api_exception)


def register_routers(app: FastAPI):
    app.include_router(convertor, prefix='/convertor')
    app.include_router(media_type, prefix='/type')
    # app.include_router(users_router, prefix='/api/auth/users')
