from django.contrib import admin

# Register your models here.

from .models import Breed
from .models import Cat

admin.site.register(Breed)
admin.site.register(Cat)