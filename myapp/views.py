from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    #pegando itens do template
    item_list = Item.objects.all()
    #criando contexto
    context = {
        'item_list': item_list
    }
    #passando o objeto para render method com o template
    return render(request, "myapp/index.html", context)

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item' : item
    }
    return render(request, 'myapp/detail.html', context)
    
def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":    
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context = {
        'form': form
    }
    return render(request, 'myapp/item-form.html', context)
