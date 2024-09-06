from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import StudForm
from . models import Department,departmentcourse

# Create your views here.
def formnewpage(request):
    return render(request,'newpage.html')
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username = request.POST['user_name']
        pswd = request.POST['psw']
        pswrepeat = request.POST['psw-repeat']
        if pswd==pswrepeat:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This Username already exists")
                return redirect(reverse('SchoolStoreApp:register'))
            else:
                user = User.objects.create_user(username=username,password=pswd)
                user.save();
                return redirect(reverse('SchoolStoreApp:login'))
        else:
            messages.info(request,"Password not matching")
            return redirect(reverse('SchoolStoreApp:register'))
            return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(reverse("SchoolStoreApp:formnewpage"))
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/')
    return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def submitform(request):
    form=StudForm()
    if request.method=="POST":
        form=StudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request submitted successfully.')
            return redirect(reverse('SchoolStoreApp:submitform'))
    return render(request,'form.html',{'form': form})

def AllDepartment(request, dep_slug=None):
    dep_page=None
    departments=None
    if dep_slug!=None:
        dep_page=get_object_or_404(Department,slug=dep_slug)
        departments=Department.objects.all().filter(dep_name=dep_page)
    return render(request, "department.html", {'department':dep_page,'departments': departments})

def load_courses(request):
    dep_name_id = request.GET.get('dep_name_id')
    courses = departmentcourse.objects.filter(dep_name_id=dep_name_id).all()
    # print(list(courses.values('id', 'name')))
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})

def stud_add(request):
    form1 = StudForm()
    if request.method == 'POST':
        form1 = StudForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Request submitted successfully.')
            return redirect('stud_add')
    return render(request, 'form.html', {'form1': form1})