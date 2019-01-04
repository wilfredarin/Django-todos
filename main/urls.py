from django.urls import path



#import the update
#made in views

from .views import index, todo_detail, todo_update ,  todo_create
""" **TodoCreateView dropped it and repplad Todo_create """ 
#registering view todo


urlpatterns = [
    #path(route,view,kwarg,name),
    path('',index,name='index'),
    #becoz here path is a empty string 
    #path('',include('main.urls'))] and th
    #is a code from main url 
    #it has " " empty string	
    path('todo/<int:todo_id>/',todo_detail,name='todo_detail'),
    #int type pass a view:todo_detail
	#registerd view here
	#so path has another arguement name=""


#register
	path('todo/',todo_create,name='todo_create') 
    #path('todo/',TodoCreateView.as_view(),name='todo_create') chANGING for class view 
    #for class view there is a method .as_view which has to be called
    ,
    path('todo/<int:todo_id>/todo_update',todo_update,name='todo_update'),
    #lets go to index page make a link pointing to update



	]