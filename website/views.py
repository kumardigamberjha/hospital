from django.shortcuts import render
from .models import Check_In_Model, Check_Out_Model, User_Data
from .forms import AddUserForm, CheckInForm, CheckOutForm

def index(request):
    checked_in = Check_In_Model.objects.all()
    checked_out = Check_Out_Model.objects.all()

    context = {'checked_in':checked_in, 'checked_out': checked_out}
    return render(request, 'website/index.html', context)

def Check_In(request):
    checked_in = Check_In_Model.objects.all()

    form = CheckInForm()
    if request.method == "POST":
        form = CheckInForm(request.POST)
        
        if form.is_valid():
                form.save()

    context = {'form': form,'checked_in':checked_in}
    return render(request, 'website/check-in.html', context)

def Check_Out(request):
    checked_out = Check_Out_Model.objects.all()

    form = CheckOutForm()
    if request.method == "POST":
        form = CheckOutForm(request.POST)
        
        if form.is_valid():
                form.save()

    context = {'form': form, 'checked_out': checked_out}
    return render(request, 'website/check-out.html', context)

def AddUser(request):
    user = User_Data.objects.all()
    form = AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST)
        
        if form.is_valid():
                form.save()

    context = {'form': form, 'user': user}

    return render(request, 'website/add-user.html', context)