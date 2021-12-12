from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
	class Meta:
		model = TodoModel
		fields = ['task', 'deadline', 'note']
		widgets = {'task':forms.Textarea(attrs={'rows':5, 'cols':50, 'style':'resize:none;'}),
			   'deadline':forms.Textarea(attrs={'rows':2, 'cols':50, 'style':'resize:none;'}),
			   'note':forms.Textarea(attrs={'rows':3, 'cols':50, 'style':'resize:none;'}) }