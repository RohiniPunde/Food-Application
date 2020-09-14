from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm


def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list ,

    }
    return render(request,'index.html',context)

def item(request):

    return HttpResponse("This is new item")

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={'item':item ,}

    return render(request,'detail.html',context)

def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'item_form.html',{'form':form})

def update(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None ,instance=item)

    if form.is_valid() :
        form.save()
        return redirect('food:index')

    return render(request,'item_form.html',{'form':form,'item':item})


def item_delete(request,id):
    item=Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'item_delete.html',{'item':item})