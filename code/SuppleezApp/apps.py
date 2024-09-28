from django.apps import AppConfig


class SuppleezappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SuppleezApp'
	
    def ready(self):
        import SuppleezApp.signals 
