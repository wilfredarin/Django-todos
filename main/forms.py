from django import forms
from datetime import date
from .models import Todo

"""got to django website and look for 
form field

form to process data

title
due date
description
done

form takes dictionary
methods
form.is_valid()->t/f
django will make:dictionary:cleaned_data
form.cleaned_data->create new todos


in shell------- type

from main.models import Todo
Todo.object.create(**data)
keyword arguement
form.as_p()
gives all field as para

form.as_table()
form.save()
"""
#class TodoForm(forms.Form):
class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ('title','due_date','description','done') #'__all__'
		#maps models

#to change the labels of the form dictionries label key of dict field name u want to change
		labels= { 'done':'is this task done?'}
# help text dictioary
		help_text = {'due_date':'Date when this task is expected to be done.'}
#change the widget also












#******************adding validation on the form**************************
#coustom validation
#add a valid to field or form
#restrict user to 5 words on todo title
#by convention
# clean_nameoffield for validation



	def clean_title(self):
		word_len=5   #max no of words in title
		"""clean data dictionary populated                                """
		title=self.cleaned_data['title']

		words=title.split(' ')#words
		if len(words)>word_len:
			raise forms.ValidationError('The title should be not more than '+str(word_len)+' words')
		return title
		#
	#lets make for due date

	def clean_due_date(self):
		due_date  = self.cleaned_data['due_date']

		if due_date < date.today():
			raise forms.ValidationError('Due date can not be in past')
		return due_date 








	"""title=forms.CharField(max_length=255)
	description=forms.CharField()
	#done=forms.DateField()
	#no need 8:15 lec14
	due_date = forms.DateField()

	"""



