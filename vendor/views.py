from django.shortcuts import render,redirect
from .forms import VendorForm
from .models import Vendor

# Create your views here.
def upload_vendor_registrations(request):
    if request.method == "POST":
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor_registration_list')
    else:
        form = VendorForm()
    return render(request, 'vendor/vendor_upload.html', {'form': form})