from django.shortcuts import render
from .models import Search
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
#from django.contrib.auth.models import Search
from .models import Search, Location, Industry
from .filters import SearchFilter

# Create your views here.

# def index(request):
#    return HttpResponse("<h>This is the search homepage</h>")

def index(request):
    all_courses = Search.objects.all()
    context = {
           'all_courses':all_courses
           }
    template = loader.get_template('search/index.html')
    html = ''
    for course in all_courses:
        url = '/search/' + str(course.id) + '/'
        html += '<a href="' + url + '">' + str(course.TITLE) + '</a><br>'

# 1st header but no list
    return render(request, 'search/index.html', context)

# 2nd working list but no header
#     return HttpResponse(html)


def detail(request, search_id):
    try:
        search = Search.objects.get(id=search_id)
    except Search.DoesNotExist:
        raise Http404('This search does not exist')

#    return HttpResponse("<h2> Details for search id:" + str(search_id)+ "</h2>")
    return render(request, 'search/detail.html', {'search':search})

# def search(request):
#     template = loader.get_template('search/index.html')
#     all_courses = Search.objects.all()
#     context = {
#         'all_courses': all_courses
#     }
#     return HttpResponse(template.render(context, request))

def searchlist(request):
    # template = loader.get_template('search/searchlist.html')
    all_courses = Search.objects.all()
    course_filter = SearchFilter(request.GET, queryset=all_courses)
    return render(request, 'search/searchlist.html', {'filter': course_filter})