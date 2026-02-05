from django.contrib import admin
from profiles_api import models

# Admin paneline modelleri kaydediyorum ki
# localhost:8000/admin adresinden verileri görebileyim.

admin.site.register(models.UserProfile) # Kullanıcıları yönetmek için
admin.site.register(models.Document)    # Dökümanları görmek/silmek için
