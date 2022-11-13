
# Imports
from django.contrib import admin
from app.models import User, Film, Review, Grade, Actor, Director, Studio, Award

# Register models
admin.site.register(User)
admin.site.register(Award)
admin.site.register(Studio)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(Grade)
admin.site.register(Review)
