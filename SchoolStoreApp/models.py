from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    dep_description=models.TextField(blank=True)

    class Meta:
        ordering=('dep_name',)
        verbose_name='department'
        verbose_name_plural='departments'
    def get_url(self):
        return reverse('SchoolStoreApp:AllDepartments',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.dep_name)
class departmentcourse(models.Model):
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    course=models.CharField(max_length=250,unique=True)
    def __str__(self):
        return '{}'.format(self.course)

class StudDetails(models.Model):
    stud_name=models.CharField(max_length=100)
    stud_dob=models.DateField()
    stud_age=models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    )
    stud_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    stud_phno=models.CharField(max_length=10,unique=True)
    stud_email=models.EmailField(unique=True)
    stud_address=models.CharField(max_length=250)
    dep_name=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    course=models.ForeignKey(departmentcourse,on_delete=models.SET_NULL,null=True)
    Purposes = (
        ('E', 'Enquiry'),
        ('P', 'Place Order'),
        ('R', 'Return')
    )
    purpose = models.CharField(max_length=1, choices=Purposes)
    Notebook=models.BooleanField(default=False)
    Pen=models.BooleanField(default=False)
    Exam_Papers=models.BooleanField(default=False)
    def __str__(self):
        return '{}'.format(self.stud_name)






