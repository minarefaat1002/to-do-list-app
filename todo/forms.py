from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','completed']

    def __init__(self,*args,**kwargs):
        super(TaskForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control','id':'form2','type':'text'})
        self.fields['completed'].widget.attrs.update({'class':''})