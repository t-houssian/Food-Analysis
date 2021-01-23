# Create your views here.
from bokeh.embed import server_document

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required


@never_cache
@login_required(login_url="/login")
def data(request: HttpRequest) -> HttpResponse:
    param = server_document(request.build_absolute_uri())
    return render(request, "data.html", dict(select=param))
