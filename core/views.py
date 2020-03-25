from django.shortcuts import render

def index(request):
	return render(request, 'core/index.html')

def semester(request):
	return render(request, 'core/semesters.html')

def questions(request):
	return render(request,'core/questions.html')