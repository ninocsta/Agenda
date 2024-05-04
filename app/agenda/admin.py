from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Client, Service, Events, Profissional


# Re-register UserAdmin
admin.site.register(Client)
admin.site.register(Profissional)
admin.site.register(Service)
admin.site.register(Events)