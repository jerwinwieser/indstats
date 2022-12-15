from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models.functions import ExtractWeek, ExtractYear
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm

def application_list(request):
	application_list = Application.objects.all().order_by('-submitdate')
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
		.annotate(week=ExtractWeek('submitdate'), year=ExtractYear('submitdate')) \
		.values('year', 'week') \
		.annotate(number_of_applications=Count('week')) \
		.order_by('-year', '-week')
	summary_day = Application.objects \
		.values('submitdate') \
		.annotate(number_of_applications=Count('submitdate')) \
		.order_by('-submitdate')
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
