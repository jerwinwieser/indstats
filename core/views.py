from django.shortcuts import render

def application_list(request):
	return render(request, 'core/application_list.html')

def statistics(request):
	return render(request, 'core/statistics.html')
