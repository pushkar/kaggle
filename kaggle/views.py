from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from kaggle.models import Student
from django.template import RequestContext, loader

def leaderboard(request, order_by):
	display = "leaderboard"
	if order_by == "name":
		leaderboard = Student.objects.order_by('name')
	elif order_by == "location":
		leaderboard = Student.objects.order_by('location')
	elif order_by == "last":
		leaderboard = Student.objects.order_by('last_time')
	else:
		leaderboard = Student.objects.order_by('score')
	output = ', '.join([p.name for p in leaderboard])
	template = loader.get_template('kaggle/dashboard.html')
	context = RequestContext(request, {
        'leaderboard': leaderboard,
        'display': display
    })
	return HttpResponse(template.render(context))

def form(request):
	display = "form"
	leaderboard = Student.objects.order_by('score')
	template = loader.get_template('kaggle/dashboard.html')
	context = RequestContext(request, {
		'leaderboard': leaderboard,
        'display': display,
    })
	return HttpResponse(template.render(context))

def submit(request):
	s = get_object_or_404(Student, pk=request.POST['student_id'])
	s.score = request.POST['student_score']
	s.save()
	return HttpResponseRedirect(reverse('kaggle:leaderboard'))

def cookie(request):
	return HttpResponse("Hello, Cookie Page")