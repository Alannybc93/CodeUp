from django.contrib import admin
from .models import User, Trail, Exercise, Achievement
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Trail)
admin.site.register(Exercise)
admin.site.register(Achievement)
