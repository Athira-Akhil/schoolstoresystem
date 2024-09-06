from django import forms
from . models import StudDetails,departmentcourse
class StudForm(forms.ModelForm):
    class Meta:
        model=StudDetails
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = departmentcourse.objects.none()
        if 'dep_name' in self.data:
            try:
                dep_name_id =int(self.data.get('dep_name'))
                self.fields['course'].queryset = departmentcourse.objects.filter(dep_name_id=dep_name_id).all()
            except (ValueError, TypeError):
                pass




