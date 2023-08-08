from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models.Products import Car
from .models.savat import Savat
from .models.Category import Categor
from .forms import CarForm, SavatForm, CategorForm

def ItemDelete(request,pk):
    obj= Savat.objects.get(pk=pk)
    obj.delete()
    val = Savat.objects.all()
    return render(request, 'Eshop/savat.html', {'valss': val})



def SearchPage(request):
    valu = request.POST['searchname']
    val2 = Car.objects.all()
    res = []
    for val1 in val2:
        if valu.lower() in str(val1.name).lower() or valu.lower() in str(val1.price):
            res.append(val1)
    return render(request, 'Eshop/search.html', {'val':res})




def AddCardPage(request, pk, category):
    y = Car.objects.get(pk=pk)
    val_in= request.POST["inputname"]
    val = 'Sucsecc'
    x = Savat.objects.all()
    k=True
    for el in x:
        if el.name.name== y.name and el.price== y.price:
            el.count+=int(val_in)
            el.save()
            k=False
            return HttpResponseRedirect(f'/{category}')

    if k:
        Savat.objects.create(name=y, price=y.price, count=val_in)
        return HttpResponseRedirect(f'/{category}')

    return render(request, 'Eshop/add.html',  {'val': val} )


def Categories(request):
    val = Categor.objects.all()
    return  render(request, 'Eshop/home.html', {'vals': val})

# Create your views here.
def AllProduct(request):
    obj = Car.objects.all()
    return render(request,'Eshop/allproduct.html', {"valss":obj})

def CarPage(request, category):
    vals = Car.objects.all()
    val = []
    for el in vals:
        if str(el.category) == category:
            val.append(el)

    return render(request, 'Eshop/car.html', {'val': val, 'category': category})

def CarDetailPage(request,pk):
    obj=Car.objects.get(pk=pk)
    return render(request, 'Eshop/detail.html', {'obj':obj})


def CarDetailDeletePage(request,pk):
    obj = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')
    return render(request, 'Eshop/delete.html')

def CategorCreatePage(request):
    obj = Categor.objects.all()
    context = {'obj':obj}
    form = CategorForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form'] = form
    return render(request, "Eshop/createcategor.html", context)

def CarCreatePage(request):
    context = {}
    form = CarForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, "Eshop/create.html", context)

def CarDetailEditPage(request,pk):
    detail = {}
    obj = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST, request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    detail['form'] = form
    return render(request, 'Eshop/edit.html', detail)


def Savatcha(request):
    val = Savat.objects.all()
    return render(request, 'Eshop/savat.html', {'valss': val})
