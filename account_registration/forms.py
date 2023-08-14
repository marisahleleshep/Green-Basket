from django import forms
from .models import New_user

class AccountForm(forms.ModelForm):
    class Meta:
        model = New_user
        fields = "__all__"