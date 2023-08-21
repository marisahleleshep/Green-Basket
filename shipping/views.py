from django.shortcuts import render,redirect
from .forms import ShippingForm
from .models import Shipping

# Create your views here.
def shipping_upload(request):
    if request.method == "POST":
        form = ShippingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shipping_list')
    else:
        form = ShippingForm()
    return render(request, 'shipping/shipping_upload.html', {'form': form})