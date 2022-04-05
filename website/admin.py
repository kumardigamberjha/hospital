from django.contrib import admin

from .models import User_Data, Check_In_Model, Check_Out_Model

admin.site.register(User_Data)
admin.site.register(Check_In_Model)
admin.site.register(Check_Out_Model)
