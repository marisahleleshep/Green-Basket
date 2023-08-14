from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import New_user

def upload_account_registrations(request):
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account_registration_list')
    else:
        form = AccountForm()
    return render(request, 'account_registration/account_upload.html', {'form': form})

def account_registrations_list(request):
    new_users = New_user.objects.all()
    return render(request, "account_registration/account_list.html", {"new_users": new_users})

def account_registrations_details(request, id):
    new_user = New_user.objects.get(id=id)
    return render(request, "account_registration/account_detail.html", {"account_registration": new_user})

def edit_account_registrations_view(request, id):
    account_registration = New_user.objects.get(id=id)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account_registration)
        if form.is_valid():
            form.save()
            return redirect('account_registration_detail_view', id=account_registration.id)
   