from .celery import app as celery_app
from core import app

celery = app
__all__ = ("celery_app",)