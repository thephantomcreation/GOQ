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




#TODO: Redutant remove and think for next solution for Bachelors 

# CSIT Section starts here
class Csit1List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'First')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit2List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Second')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit3List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Third')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit4List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Fourth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit5List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Fifth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit6List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Sixth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit7List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Seventh')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class Csit8List(ListView):
	queryset = Bachelors.objects.filter(faculty = "CSIT").filter(semester = 'Eighth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
#CSIT ends here 


#BIM Starts Here
class BIM1List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'First')
	template_name = 'core/questions.html'
	context_object_name= 'subjects' 

class BIM2List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Second')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BIM3List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Third')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BIM4List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Fourth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BIM5List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Fifth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BIM6List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Sixth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
class BIM7List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Seventh')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
class BIM8List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BIM").filter(semester = 'Eighth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
#BIM ends here 


#BHM starts here 
class BHM1List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'First')
	template_name = 'core/questions.html'
	context_object_name= 'subjects' 

class BHM2List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Second')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BHM3List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Third')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BHM4List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Fourth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BHM5List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Fifth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BHM6List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Sixth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
class BHM7List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Seventh')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
class BHM8List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BHM").filter(semester = 'Eighth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
#BHM ends here 

class BCA1List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'First')
	template_name = 'core/questions.html'
	context_object_name= 'subjects' 

class BCA2List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Second')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BCA3List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Third')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BCA4List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Fourth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BCA5List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Fifth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'

class BCA6List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Sixth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
class BCA7List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Seventh')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
class BCA8List(ListView):
	queryset = Bachelors.objects.filter(faculty = "BCA").filter(semester = 'Eighth')
	template_name = 'core/questions.html'
	context_object_name= 'subjects'
#BCA ends here 