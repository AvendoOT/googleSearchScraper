from django.shortcuts import render
from googleSearch import blogspotSearch
from googleSearch import googleSearch
from googleSearch import customSearch


def home(request):
    if request.POST:
        form_data = request.POST.dict()
        google_result = googleSearch.get_searches(form_data.get('search'))
        results = blogspotSearch.getSearches(form_data.get('search'))
        custom = customSearch.get_searches(form_data.get('search'))
        return render(request, '../templates/googleSearchScraperTemplates/home.html',
                      {'results': custom + results + google_result})
    else:
        return render(request, '../templates/googleSearchScraperTemplates/home.html')


def about(request):
    return render(request, '../templates/googleSearchScraperTemplates/about.html')
