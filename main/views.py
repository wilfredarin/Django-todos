from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from datetime import datetime,timedelta
#lets import 404
from django.http import Http404
from .models import Todo
#to load template
from django.template import loader
from .forms import TodoForm



#import msging framework
from django.contrib import messages

""" django allows class based view and it's better than functions so lets import it"""
from django .views.generic import CreateView , UpdateView


#for url to get from function
from django.urls import reverse_lazy


# Create your views here

def index(request):
	"""template = loader.get_template('main/index.html')
	context = { 'today':datetime.now()}
	return HttpResponse(template.render(context,request))
	#render(context:dictionary,request)

"""
	todos = Todo.objects.all()
	
	context = { 'todos':todos,
	'today':datetime.now() + timedelta(hours=5.5),#fixed gmt bug added timedelta
	'app_name':"super todos"}
	return render(request, 'main/index.html',context=context)
	
"""
pass url in urls.py 
which is passed to viev then u'lll be
able to see it in django view

we'll alow user to pass todo id in url 
then in view w'll fetch it

display detail of one todo
to 
we'll 
"""
def todo_detail(request,todo_id):

	todo = get_object_or_404(Todo, pk=todo_id)


	"""another way without shortcut
	try:
		todo=Todo.objects.get(pk=todo_id)
	#pk primary key
	#get the id of the object
	except Todo.DoesNotExist:
		raise Http404("Wilfredarin | Todo with id :{} doesn't exist".format(todo_id))
	"""
	
	#class name ,id
	todo=get_object_or_404(Todo,pk=todo_id)
	context = {
	'todo' : todo
	}
	#request should be first argument in ur view
	return render(request,"main/todo_detail.html",context=context)
	#request, template name, context object
	#this rendersin todo_detail template










""" NameofmodelCreateView() 
class TodoCreateView(CreateView):
	"""    """
	model = Todo
	form_class = TodoForm
	template_name = 'main/todo.html'
	succes_url = reverse_lazy('index')         #where to redirect users

	







"""








"""
form api



"""
def todo_create(request):
	"""
	request
	check get/post?
	data -post object in 
	post-redirect-get pattern

	return a redirect: simple str returned by server
	which directs to aother page
	after succesfull request
	redirect to other page
	to prevent it from submitting again

	get method used to go to other page


	"""
	if request.method=="POST":
		form=TodoForm(request.POST)
		#request.post is a dictionary containig the form
		if form.is_valid():
			form.save()
			#as this is model form saves directly
			#adding a message
			messages.success(request,"The todo was created successfully")
			return redirect('index')
			#redirect takes name of the view u want to redirect to
		else:
			return render(request,'main/todo.html',{'form':form})
		#pass form object error dictionary of form(context)
	else:
	#if request is get method
	#initialise a empty form
	#
		return render(request,'main/todo.html',{'form':TodoForm})

#lets register it in url form




#lets create a view which can update todo

def todo_update(request,todo_id):
	"""
it takes request and todo_id as arguement

grab the todo from todo_id
and check the method
instance is the object u want to update
if u pass the instance it will update the prev one
update that instance
and if u dont 
it will make a new one



	"""

	todo=get_object_or_404(Todo,pk=todo_id)
	if request.method=="POST":
		form=TodoForm(request.POST,instance=todo)
		if form.is_valid():
			form.save()
			##adding a msg of success:request object is the first argument and the string the second
			messages.success(request,"The todo was updated successfully")
			return redirect('index')
		return render(request,'main/todo.html',{'form':form})
	#if get method
	return render(request,'main/todo.html',{'form':TodoForm(instance=todo)})
#so when get request form populated with data of tha instance
#lets register view in url.py












