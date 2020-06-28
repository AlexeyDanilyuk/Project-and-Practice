from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.forms import UserLoginForm, UserRegisterForm, UserEditForm, UserProfileEditForm
from authapp.models import User
from worksite import settings


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main:arm_list'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'вход в систему',
        'form': form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:arm_list'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                print('--- Сообщение подтверждения отправлено ---')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('--- Ошибка отправки сообщения ---')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context)


@login_required
def edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
    context = {
        'title': 'редактирование',
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'authapp/edit.html', context)


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        kwargs={
            'email': user.email,
            'activation_key': user.activation_key
        })

    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на сайте ' \
              f'{settings.DOMAIN_NAME} перейдите по ссылке: \n' \
              f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER,
                     [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            print(f'--- Ошибка активации учетной записи: {user} ---')
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'--- Ошибка активации учетной записи : {e.args} ---')
        return HttpResponseRedirect(reverse('main:arm_list'))
