from django.shortcuts import render,redirect
from .forms import PaymentForm
from .models import Payment

# Create your views here.
def payment_upload(request):
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment/payment_upload.html', {'form': form})