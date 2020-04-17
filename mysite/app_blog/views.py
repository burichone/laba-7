from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


# Create your views here.
