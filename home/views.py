from django.shortcuts import render
from .form import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
  return render(request, "pages/home.html")

def contact(request):
  return render(request, "pages/contact.html")

def register(request):
  form = RegistrationForm()
  context = {
    "form": form
  }
  if request.method == "POST":
    form = RegistrationForm(request.POST) # dua du lieu nguoi dung nhap vao bien form
    if form.is_valid:
      form.save()
      return HttpResponseRedirect("/")
  return render(request, "pages/register.html", context)