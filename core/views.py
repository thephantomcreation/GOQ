from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from .models import * 

def index(request):
	return render(request, 'core/index.html')



class SeeList(ListView):
	'''Views to render SEE '''
	
	queryset = See.objects.all()
	print(queryset)
	template_name = 'core/questions.html'
	context_object_name= 'subjects'


class PlusTwoList(ListView):
	queryset = PlusTwo.objects.all()
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
