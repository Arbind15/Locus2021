from django.contrib import admin
from .models import userProfile, hospitalProfile,adminProfile, hospitalStatus,userStatus

admin.site.register(userProfile)
admin.site.register(hospitalProfile)
admin.site.register(adminProfile)
admin.site.register(hospitalStatus)
admin.site.register(userStatus)