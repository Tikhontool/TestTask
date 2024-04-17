from django.apps import AppConfig
from django.core.cache import cache


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):

        cache.set('mykey', [1,2,3])
