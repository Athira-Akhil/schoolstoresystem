from django.contrib import admin
from .models import Department,departmentcourse,StudDetails

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dep_name','slug']
    prepopulated_fields = {'slug':('dep_name',)}
admin.site.register(Department,DepartmentAdmin)
admin.site.register(departmentcourse)
admin.site.register(StudDetails)
