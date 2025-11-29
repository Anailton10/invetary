from django.shortcuts import redirect, render
from django.views import View

from .models import Product


class ProductListView(View):
    def get(self, request):
        product = Product.objects.all()
        # logica para listar produtos
        context = {'products': product}
        return render(request, 'product_list.html', context=context)


class ProductCreateView(View):
    def get(self, request):
        return render(request, 'product_create.html')

    def post(self, request):
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        status = request.POST.get('status') == 'on'

        Product.objects.create(
            name=name,
            quantity=quantity,
            description=description,
            status=status,
        )
        return redirect('products:list')
