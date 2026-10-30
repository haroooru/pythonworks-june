
from django.contrib import admin

# Original code preserved for reference
# from django.contrib import admin
#
# Register your models here.

from movies.models import Movie

# Register your models here.
admin.site.register(Movie)
