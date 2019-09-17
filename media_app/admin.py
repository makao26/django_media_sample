
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import Document
from .models import Friend

admin.site.register(Document)
admin.site.register(Friend)
