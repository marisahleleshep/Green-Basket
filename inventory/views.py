from .forms import ProductUploadForm
from .models import Product

from django.shortcuts import render,redirect
# from django.shortcuts import render,redirect

# Create your views here.
def product_upload_view(request):
    if request.method == "POST":
        form= ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('product_list')


    else:
        form = ProductUploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})


def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products":products})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_description.html", {"product":product})



def product_update_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return render(request, "inventory/product_not_found.html")

    if request.method == "POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_description_view", id=product.id)
    else:
        form = ProductUploadForm(instance=product)

    # Render the template with the form
    return render(request, "inventory/edit_product.html", {"form": form})
    
def delete_product(request, id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect("products_list_view")