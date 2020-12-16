from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now Logged out')
        return redirect('index')


def register(request):
    if request.method == 'POST':

        # get form values:
        first_name = request.POST.get('first_name', 'default value')
        last_name = request.POST.get('last_name', 'default value')
        username = request.POST.get('username', 'default value')
        email = request.POST.get('email', 'default value')
        password = request.POST.get('password', 'default value')

        password2 = request.POST.get('password2', 'default value')

        # check if passwords match
        if password == password2:
            # check usename
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is already Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is already used')
                    return redirect('register')
                else:
                    # go for the user registration
                    user = User.objects.create_user(first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    email=email,
                                                    password=password)
                    # login afte registration
                    # auth.login(request, user)
                    # message.success(request, "You are now logged in")
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, "You are now registered and can log in")
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
