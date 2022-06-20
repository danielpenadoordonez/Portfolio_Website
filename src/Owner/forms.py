from django import forms
from .models import Owner

# class OwnerForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField(widget=forms.EmailInput)

#     class Meta:
#         model = Owner
#         fields = [
#             "userName",
#             "password",
#             "name",
#             "lastName",
#             "email",
#             "description"
#         ]
