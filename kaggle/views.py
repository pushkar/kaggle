from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from kaggle.models import Student, Pages
from django.template import RequestContext, loader

def index(request):
	display = "signin"
	template = loader.get_template('kaggle/signin.html')
	context = RequestContext(request, {
	    'display': display
	})
	return HttpResponse(template.render(context))

def signin(request):
	try:
		s = Student.objects.get(handle=request.POST['handle_id'])
	except:
		s = Student(handle=request.POST['handle_id'])
		s.save()
	request.session['handle_id'] = s.handle
	return HttpResponseRedirect(reverse('kaggle:form'))

def logout(request):
	try:
		del request.session['handle_id']
	except KeyError:
		pass
	return HttpResponseRedirect(reverse('kaggle:index'))

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

	handle = request.session['handle_id']
	pages = Pages.objects.order_by('order')
	template = loader.get_template('kaggle/dashboard.html')
	context = RequestContext(request, {
		'handle': handle,
		'pages': pages,
        'leaderboard': leaderboard,
        'display': display
    })
	return HttpResponse(template.render(context))

def form(request):
	display = "form"
	leaderboard = Student.objects.order_by('score')
	pages = Pages.objects.order_by('order')
	template = loader.get_template('kaggle/dashboard.html')
	context = RequestContext(request, {
		'pages': pages,
		'leaderboard': leaderboard,
        'display': display,
    })
	return HttpResponse(template.render(context))

def page_view(request, page_id):
	display = "page"
	pages = Pages.objects.order_by('order')
	page = Pages.objects.get(handle=page_id)
	template = loader.get_template('kaggle/dashboard.html')
	context = RequestContext(request, {
		'page' : page,
		'pages': pages,
        'display': display,
    })
	return HttpResponse(template.render(context))

def submit(request):
	s = get_object_or_404(Student, pk=request.POST['student_id'])
	s.score = request.POST['student_score']
	s.save()
	return HttpResponseRedirect(reverse('kaggle:leaderboard'))

def set_cookie(request):
	response = HttpResponse("Hello, This is the Set Cookie Page")
	response.set_cookie('logged_in_status', 'logged in')
	return response

def show_cookie(request):
	return HttpResponse("Cookie is " + request.COOKIES.get('logged_in_status') )
