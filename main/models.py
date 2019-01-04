from django.db import models

# Create your models here.
class Todo(models.Model):
	#inherit from models
#field types are mapping to underline table
	title = models.CharField(max_length=225)
	#string field max xhar it can store is 
	due_date = models.DateField()
	done = models.BooleanField(default=False)
	description = models.TextField()
#no need to create id field it happens auto matically	

#after all this do migration
#manage.py makemigrations
#manage.py migrate
#sql client starts 
#python manage.py dbshell
#opens sqlite command
#.table:comand shows tables in it 
#auth : from setting.py authentication
	"""to represet todoy """
	def __str__(self):
		return self.title
		

                                                                                                          