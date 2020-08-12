from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
    	import users.signals #users = (app name)    [import 'app_name.filename']
