from django.shortcuts import render,redirect

from .forms import OrderForm
from .models import Order

# Create your views here.


def upload_order(request):                      
    #the request represents a http request
    if request.method == 'POST':
        uploaded_order = request.FILES["image"]
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    return render(request, "order/upload_order.html", {"form": form})

def order_list(request):
    order = Order.objects.all()
    return render (request, "order/order_list.html", {"orders":order})

# def order_detail(request,id):
#     order=Order.objects.get(id=id)
#     return render(request,"order/order_detail.html", {"order":order})

# def edit_order_view(request,id):
#      order=Order.objects.get(id=id)
#      if request.method=='POST':
#       form=OrderForm(request.POST,instance=Order)
#       if form.is_valid():
#          form.save()
#       return redirect("order_detail_view",id=Order.id )   
#      else:
#         form=OrderForm(instance=order)
#         return render (request,"edit/edit_order.html",{"form":form})