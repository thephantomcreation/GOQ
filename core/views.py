from django.shortcuts import render

def index(request):
	return render(request, 'core/index.html')

def semester(request):
	return render(request, 'core/semesters.html')

def questions(request):
	return render(request,'core/questions.html')

def search_results(request):
	return render(request, 'core/search_results.html')

def contact_us(request):
	return render(request, 'core/contact_us.html')