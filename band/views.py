from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import SignUpForm
from .models import BandMember, Event


def index(request):
    """
    Render the home page of the band app.

    This view function handles requests to the root URL of the band app and renders the 'index.html'
    template. It does not pass any additional context to the template.
    """
    latest_band_member_list = BandMember.objects.order_by('id')
    latest_event_list = Event.objects.order_by('id')[:5]
    context = {
        'latest_event_list': latest_event_list,
        'latest_band_member_list': latest_band_member_list,
    }
    return render(request, 'band/index.html', context)


def event(request, event_id):
    """
    Render the page displaying selected event.

    This view function retrieves one Event information from the database and renders the 'event.html' template,
    passing the event as context.
    """
    selected_event = get_object_or_404(Event, pk=event_id)
    return render(request, 'band/event.html', {'event': selected_event})


def register(request):
    """
    Handle user registration.

    This view function handles both displaying the registration form and processing form submissions.
    - If the request method is POST, it means the form has been submitted. The view validates and saves the form,
      then logs in the newly registered user and redirects them to the home page.
    - If the request method is GET, it means the form should be displayed. A new, empty form is instantiated and
      rendered in the 'register.html' template.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to the home page after successful registration
    else:
        form = SignUpForm()  # Instantiate a new form for GET requests
    return render(request, 'band/register.html', {'form': form})


def user_login(request):
    """
        Render the login page.
        Handles GET requests to display the login form and POST requests to authenticate the user.
        On successful login, redirects to the URL specified in the 'next' parameter or defaults to 'polls:index'.
        """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'index')
            return HttpResponseRedirect(
                reverse(next_url)
            )
    else:
        form = AuthenticationForm()

    return render(request, 'band/login.html', {'form': form})


def authenticate_user(request):
    """
    Handle user authentication (login).

    This view function handles both displaying the login form and processing form submissions.
    - If the request method is POST, it means the form has been submitted. The view validates the form,
      logs in the user, and redirects them to the home page.
    - If the request method is GET, it means the form should be displayed. A new, empty form is instantiated
      and rendered in the 'login.html' template.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in after successful authentication
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()  # Instantiate a new form for GET requests
    return render(request, 'band/login.html', {'form': form})


def sign_out(request):
    print(request.user)
    """
    Log out the user and redirect to the login page.
    """
    logout(request)
    return HttpResponseRedirect(
        reverse('index')
    )
