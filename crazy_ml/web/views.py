from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        return dashboard(request)

    return render(request, 'index.html')


@login_required()
@csrf_exempt
def dashboard(request):
    if request.user.last_login is None:
        return info(request)
    return render(request, 'dashboard.html', {})


@login_required()
@csrf_exempt
def descriptions(request):
    return render(request, 'descriptions.html', {'descriptions': Description.objects.filter(author=request.user)})


@login_required()
@csrf_exempt
def info(request):
    return render(request, 'questionnaire.html')


@login_required()
@csrf_exempt
def change_password(request):
    return render(request, 'password_change.html')


