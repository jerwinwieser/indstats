from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models.functions import ExtractWeek, ExtractYear
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm

def application_list(request):
	application_list = Application.objects.all().order_by('-submit_date')
	context = {
		'application_list': application_list,
	}
	return render(request, 'core/application_list.html', context)

@login_required
def application_create(request):
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			form.instance.created_by = request.user
			form.save()
			return redirect('application_list')
	else:
		form = ApplicationForm()
	context = {
		'form': form,
	}
	return render(request, 'core/application_create.html', context)

@login_required
def statistics(request):
	application_list = Application.objects.all()
	summary_week = Application.objects \
		.annotate(submit_year=ExtractYear('submit_date'), submit_week=ExtractWeek('submit_date')) \
		.values('submit_year', 'submit_week') \
		.annotate(number_of_applications=Count('submit_week')) \
		.order_by('-submit_year', '-submit_week')
	summary_day = Application.objects \
		.values('submit_date') \
		.annotate(number_of_applications=Count('submit_date')) \
		.order_by('-submit_date')
	summary_approved = Application.objects.filter(approved=True).count()
	summary_approved_not = Application.objects.filter(approved=False).count()
	context = {
		'application_list': application_list,
		'summary_week': summary_week,
		'summary_day': summary_day,
		'summary_approved': summary_approved,
		'summary_approved_not': summary_approved_not,
	}
	return render(request, 'core/statistics.html', context)
