from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from web.models import Profile
from django.core.mail import EmailMessage
from django.contrib import messages
import string
import random
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required()
@csrf_exempt
def password(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.user)
        if not u.check_password(request.POST['password']):
            messages.error(request, "Wrong password!")
            return render(request, 'password_change.html')

        u.set_password(request.POST['new_password'])
        u.save()
        messages.success(request, "Your password has been changed!")
        logout(request)

    return redirect('/')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        user_password = request.POST['password']

        user = authenticate(username=username, password=user_password)
        if user is None:
            messages.error(request, "Wrong login data!")
            return redirect('/')

        if not user.is_active:
            messages.error(request, "Your account has been blocked!")
            return redirect('/')

        auth_login(request, user)
        return render(request, 'dashboard.html')

    return redirect('/')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@csrf_exempt
def retrieve_password(request):
    if request.method == 'POST':
        username = request.POST['username-modal']
        email = request.POST['email-modal']
        user = User.objects.get(username=username)

        if user is None or email != user.email:
            return JsonResponse({'message': 'Wrong data!', 'type': 'bad'}, safe=False)

        try:
            new_password = id_generator()
            user.set_password(new_password)
            user.save()
            msg = EmailMessage('Password Retrieve from somadev.pl (Do not reply!)',
                               new_password, to=[user.email])
            msg.send()
        except Exception as e:
            return JsonResponse({'message': 'Something goes wrong, try again or contact admin!', 'type': 'bad'},
                                safe=False)

        return JsonResponse({'message': 'New password has been sent to your email!', 'type': 'good'}, safe=False)


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':

        username = request.POST['user']
        user_password = request.POST['password']
        user_password2 = request.POST['password2']

        print(username)

        if user_password != user_password2:
            messages.error(request, "Password should be the same!")
            return redirect('/signup')

        print(User.objects.all())

        if User.objects.filter(username=username).exists():
            messages.error(request, "This user already exists!")
            return redirect('/signup')

        try:
            user = User.objects.create_user(username=username, password=user_password)
            user.is_superuser = False
            user.is_staff = False
            user.save()
        except:
            messages.error(request, "Something went wrong!")
            return redirect('/signup')

        u = authenticate(username=username, password=user_password)
        auth_login(request, u)
        return render(request, 'dashboard.html')

    return redirect('/signup')