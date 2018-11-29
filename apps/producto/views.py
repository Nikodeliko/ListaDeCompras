from django.shortcuts import render

# Create your views here.

def producto_add(request):
    context = {}
    if request.method=="POST":
        product_form = ProductForm(request.POST)
        context['product_form'] = product_form
        if product_form .is_valid():
            p = product_form.save()
            return HttpResponseRedirect(reverse('Lista'))
        else:
            return render(request, 'usuario/registro.html', context)
    else:
        product_form= ProductForm()
        context['product_form'] = product_form
        return render(request, 'usuario/registro.html', context)
