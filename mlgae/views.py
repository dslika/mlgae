import django
import rest_framework
from django.http import HttpResponse


def home(request):
    # return HttpResponse("I'm a module, using %s" % settings.SETTINGS_MODULE)
    return HttpResponse(
        " Django: %s / REST framework: %s" % (django.get_version(), rest_framework.VERSION)
    )
