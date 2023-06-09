from django.shortcuts import render, redirect
from Home.views import Home
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
import json

# Create your views here.
def User_Profile(request):
    """
    Renders the user profile page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered user profile page.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    print(user_profile.email)

    return render(request, 'user.html', context=context)

def Login(request):
    """
    Handles user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    try:
        if request.user.is_authenticated:
            return redirect(Home)

        if request.method == 'POST':
            username = request.POST.get('email', '')
            password = request.POST.get('password', '')
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                print("logged in")
                return redirect(Home)

            else:
                user = UserProfile.objects.get(email=username)
                auth_user = authenticate(username=user.user.username, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    print("logged in")
                    return redirect(Home)
                else:
                    context = {
                        'error': 'Invalid username or password',
                    }
                    print("invalid")
                    return render(request, 'login.html', context)
        else:
            context = {'iserror': False}
            return render(request, 'login.html', context)
    except:
        return redirect(Login)

def Signup(request):
    if request.user.is_authenticated:
        return redirect(Home)

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first', '')
        last_name = request.POST.get('last', '')
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        home_address = request.POST['address']
        phone_number = request.POST['phone']
        try:
            validate_email(email)
        except:
            context = {
                'error': 'Invalid email',
            }
            return render(request, 'signup.html', context)
        if User.objects.filter(username=username).exists():
            context = {
                'error': 'Username already exists',
            }
            return render(request, 'signup.html', context)
        if User.objects.filter(email=email).exists():
            context = {
                'error': 'Email already exists',
            }
            return render(request, 'signup.html', context)
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user_profile = UserProfile(user=user, email=email, latitude=latitude, longitude=longitude, home_address=home_address, phone_number=phone_number)
        user_profile.save()
        user.save()
        context = {
            'user': user,
        }
        return redirect(Login)
    else:
        context = {'iserror': False}
        return render(request, 'signup.html', context)


@login_required
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('Profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form
    }

    return render(request, 'edit_profile.html', context)

def User_Map(request):
    """
    Renders the user map page using leaflet.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered user map page.
    """
    user_profiles = UserProfile.objects.select_related('user').all().values(
        'latitude', 'longitude', 'user__first_name', 'user__last_name', 'user__email',
        'home_address', 'phone_number'
    )
    user_profiles_json = json.dumps(list(user_profiles))
    return render(request, 'map.html', {'user_profiles_json': user_profiles_json})

def signout(request):
    logout(request)
    return redirect(Home)