from attr import field
from .models import Check_In_Model, Check_Out_Model, User_Data
from django import forms

class CheckInForm(forms.ModelForm):
    class Meta:
        model = Check_In_Model
        fields = '__all__'

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Check_Out_Model
        fields = '__all__'

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User_Data
        fields = "__all__"