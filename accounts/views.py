from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model


# Create your views here.

def register(request):
    message = ''
    if request.method == "POST":
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        full_name = request.POST['full_name']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        if CustomUser.objects.filter(email=email) or CustomUser.objects.filter(phone_number=phone_number):
            message = 'this username or email is already exit please choose another please'
            return render(request, 'accounts/register.html', context={'message': message})

        if password != password2:
            message = 'passwords are not match!!!'
            return render(request, 'accounts/register.html', context={'message': message})

        newuser = CustomUser.objects.create_user(email=email, phone_number=phone_number, full_name=full_name,
                                                 password=password)
        newuser.full_name = full_name
        newuser.is_active = False
        newuser.save()
        # to get the domain of the current site
        current_site = get_current_site(request)
        mail_subject = 'Activation link has been sent to your email id'
        message = render_to_string('accounts/email_template.html', {
            'user': newuser,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
            'token': account_activation_token.make_token(newuser),
        })
        to_email = email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        message = 'Please confirm your email address to complete the registration'

        return render(request, 'markito/home.html', context={
            'message': message
        })
    else:
        return render(request, 'accounts/register.html', context={"message": message})


def login(request):
    message = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)

        else:
            message = 'your email or password is wrong!!!'
    return redirect('markito:home')


def log_out(request):
    logout(request)
    return redirect("markito:home")


def activate(request, uidb64, token):
    message = ''
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
