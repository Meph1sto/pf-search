from django.shortcuts import render
from .models import Search
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
#from django.contrib.auth.models import Search
from .models import Search, Location, Industry
from .filters import SearchFilter
from .forms import SearchFilterForm

# Create your views here.

def index(request):
    all_courses = Search.objects.all()[:5]
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

def detail(request, search_id):
    try:
        search = Search.objects.get(id=search_id)
    except Search.DoesNotExist:
        raise Http404('This search does not exist')

#    return HttpResponse("<h2> Details for search id:" + str(search_id)+ "</h2>")
    return render(request, 'search/detail.html', {'search':search})


def searchlist(request):
    # template = loader.get_template('search/searchlist.html')
    all_courses = Search.objects.all()
    # all_courses = Search.objects.exclude(id>10)
    course_filter = SearchFilter(request.GET, queryset=all_courses)
    return render(request, 'search/searchlist.html', {'filter': course_filter})


def searchtree(request):
    qs = Search.objects.all()
    form = SearchFilterForm(data=request.GET)
    facets = {
        "selected": {},
        "categories": {
            "Level": Search.objects.all(),
            "Subject": Search.objects.all(),
            "University": Search.objects.all(),
            "County": Search.objects.all(),
            "Country": Search.objects.all(),
        },
    }

    if form.is_valid():
        level = form.cleaned_data["level"]
        if level:
            facets["selected"]["Level"] = level
            qs = qs.filter(levels=level).distinct()

        TITLE = form.cleaned_data["TITLE"]
        if TITLE:
            facets["selected"]["Subject"] = TITLE
            qs = qs.filter(TITLEs=TITLE).distinct()

        UNI_NAME = form.cleaned_data["UNI_NAME"]
        if UNI_NAME:
            facets["selected"]["University"] = UNI_NAME
            qs = qs.filter(UNI_NAMEs=UNI_NAME).distinct()

        county = form.cleaned_data["county"]
        if county:
            facets["selected"]["County"] = county
            qs = qs.filter(countys=county).distinct()

        country = form.cleaned_data["country"]
        if country:
            facets["selected"]["Country"] = county
            qs = qs.filter(countrys=country).distinct()

    context = {
        "form": form,
        "facets": facets,
        "object_list": qs,
        }
    return render(request, "search/searchtree.html", context)
