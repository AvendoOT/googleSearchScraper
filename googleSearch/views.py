from django.shortcuts import render
from googleSearch import search


def home(request):
    if request.POST:
        form_data = request.POST.dict()
        results = search.getSearches(form_data.get('search'))
        return render(request, '../templates/googleSearchScraperTemplates/home.html',
                      {'results': results})
    else:
        return render(request, '../templates/googleSearchScraperTemplates/home.html')


def about(request):
    return render(request, '../templates/googleSearchScraperTemplates/about.html')
