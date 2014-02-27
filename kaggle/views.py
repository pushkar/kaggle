from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from kaggle.models import Student
from django.template import RequestContext, loader

def index(request):
	leaderboard = Student.objects.order_by('score')
	output = ', '.join([p.name for p in leaderboard])
	template = loader.get_template('kaggle/dashboard.html')
	context = RequestContext(request, {
        'leaderboard': leaderboard,
    })
	return HttpResponse(template.render(context))

def cookie(request):
	return HttpResponse("Hellow")

def form(request):
	leaderboard = Student.objects.order_by('score')
	template = loader.get_template('kaggle/form.html')
	context = RequestContext(request, {
        'leaderboard': leaderboard,
    })
	return HttpResponse(template.render(context))

def submit(request):
	s = get_object_or_404(Student, pk=request.POST['student_id'])
	s.score = request.POST['student_score']
	s.save()
	return HttpResponseRedirect(reverse('kaggle:index'))