from django.contrib import admin
from pushes.models import Pushes, Options, CustomUser

# Register your models here.
admin.site.register(Pushes)
admin.site.register(Options)
admin.site.register(CustomUser)
