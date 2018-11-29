from django.shortcuts import render

# Create your views here.

"""def tienda_add(request):
    context = {}
    if request.method=="POST":
        tienda_form = TiendaForm(request.POST)
        context['tienda_form'] = tienda_form
        if tienda_form.is_valid():
            self.nombre = self.nombre.lower()
            u = tienda_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'usuario/registro.html', context)
    else:
        tienda_form= TiendaForm()
        context['tienda_form'] = tienda_form
        return render(request, 'usuario/registro.html', context)
"""
