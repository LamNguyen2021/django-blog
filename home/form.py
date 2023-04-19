from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
  username = forms.CharField(label="username", max_length=30)
  email = forms.EmailField(label="email")
  password1 = forms.CharField(label="password", widget=forms.PasswordInput())
  password2 = forms.CharField(label="password again", widget=forms.PasswordInput())
  
  def clean_password2(self):
    # neu nguoi dung da nhap password 1 roi thi...
    if "password1" in self.cleaned_data:
      password1 = self.cleaned_data["password1"] # lay du lieu password1 ra
      password2 = self.cleaned_data["password2"] # lay du lieu password2 ra
      
      if password1 == password2:
        return password2
    raise forms.ValidationError("invalid password")
  
  def clean_username(self):
    username = self.cleaned_data["username"]
    if not re.search(r'^\w+$', username):
      raise forms.ValidationError("username has special characters")
    # kiem tra username co trung khong
    try:
      User.objects.get(username=username)
    except ObjectDoesNotExist:
      raise forms.ValidationError("account exists")
    return username
  
  def save(self):
    username = self.cleaned_data["username"]
    password = self.cleaned_data["password1"]
    email = self.cleaned_data["email"]
    User.objects.create_user(username=username, email=email, password=password)