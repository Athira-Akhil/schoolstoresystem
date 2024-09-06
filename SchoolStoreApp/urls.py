from . import views
from django.urls import path

app_name='SchoolStoreApp'

urlpatterns = [

    path('',views.index,name='index'),
    path('formnewpage',views.formnewpage,name='formnewpage'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('department',views.AllDepartment,name='AllDepartment'),
    path('<slug:dep_slug>/',views.AllDepartment,name='AllDepartments'),
    path('load-courses', views.load_courses, name='ajax_load_courses'),
    path('submitform',views.submitform,name='submitform'),
    path('stud_add',views.stud_add,name='stud_add'),

]