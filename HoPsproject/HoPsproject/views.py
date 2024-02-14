from django.http import HttpResponse
from django.views.generic import TemplateView

def indexfunc(request):
    responseobject = HttpResponse('hello world')
    return responseobject

class indexClass(TemplateView):
    template_name = 'index.html'