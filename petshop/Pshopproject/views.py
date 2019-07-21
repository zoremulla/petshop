from django.shortcuts import render, redirect
from .models import pets
from .forms import Petsform
# Create your views here.

def pets_list(request):
    context = {
        "pets_l":pets.objects.filter(available=True)
    }
    return render(request, "list.html", context)


def pets_details(request, pets_id):
    context = {
        "pets_d":pets.objects.get(id=pets_id)
    }
    return render(request, 'detail.html', context)

def pets_create(request):
    form = Petsform()
    form.fields['available'].widget.attrs['readonly'] = True #   to make the field 'available readonly'
     #  myform.fields['status'].widget.attrs['disabled'] = True # radio / checkbox
    if request.method == "POST":
        form = Petsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pets_update(request, pets_id):
    pet=pets.objects.get(id=pets_id)
    form=Petsform(instance=pet)
    if request.method == "POST":
        form = Petsform(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets-details', pet.id)
    context = {
        "form":form,
        'pet':pet,
    }
    return render(request, 'update.html', context)

def pets_delete(request, pets_id):
    pets_obj = pets.objects.get(id=pets_id)
    pets_obj.delete()
    return redirect('pets-list')
