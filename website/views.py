from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'website/index.html')


def sign_in(request):
    if request.method == 'GET':
        view_context = {'data_login_url': request._current_scheme_host + request.path
                        }
        return render(request, 'website/signIn.html', view_context)

    if request.method == 'POST':
        pass


def paraPartial(request):
    return render(request, 'website/para.html')
