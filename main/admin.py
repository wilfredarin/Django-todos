from django.contrib import admin

# Register your models here.
from .models import Todo


# changing this  adding new class
#admin.site.register(Todo)




#the model u want to register
#main app listed

class Todoadmin(admin.ModelAdmin):
	""" 
	ModelAdminused toctomise how ur model is used to display in admin
	geting more things dislayed in admin
	to display a table in admin
	list setting in class which is list_display"""

	list_display = ('title','due_date','done')
	#add some filtering functionalit list_filter :allow users to filter by
	list_filter = ('done','due_date')
	#oredering field order in descending so - sign
	oredering = ('-due_date',)#tuple so coma at the end


admin.site.register(Todo,Todoadmin)
