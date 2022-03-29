from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForms
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForms(request.POST)
        if fm.is_valid():
            messages.success(request, 'user signup successfully')
            fm.save()
    else:
        fm = SignUpForms()
    return render(request, 'app1/index.html', {'form': fm})
