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
    template. It passes the list of the latest band members and events as context.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered 'index.html' template with context data.
    :rtype: HttpResponse
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
    Render the page displaying a selected event.

    This view function retrieves one event's information from the database and renders the 'event.html' template,
    passing the event as context.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param event_id: The ID of the event to be displayed.
    :type event_id: int
    :return: Rendered 'event.html' template with event details.
    :rtype: HttpResponse
    """
    selected_event = get_object_or_404(Event, pk=event_id)
    return render(request, 'band/event.html', {'event': selected_event})


def register(request):
    """
    Handle user registration.

    This view function handles both displaying the registration form and processing form submissions.

    If the request method is POST, it validates and saves the form, logs in the user, and redirects to the home page.
    If the request method is GET, it displays a new, empty registration form.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered 'register.html' template with the form.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'band/register.html', {'form': form})


def user_login(request):
    """
    Handle user login.

    This view function displays the login form and processes login form submissions.

    If the request method is POST and the form is valid, the user is authenticated and logged in.
    If the request method is GET, an empty login form is displayed.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered 'login.html' template with the form or redirect to the specified URL on successful login.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'index')
            return HttpResponseRedirect(reverse(next_url))
    else:
        form = AuthenticationForm()

    return render(request, 'band/login.html', {'form': form})


def authenticate_user(request):
    """
    Handle user authentication (login).

    This view function processes both login form display and form submissions.

    If the request method is POST and the form is valid, the user is authenticated, logged in, and redirected to the home page.
    If the request method is GET, an empty login form is displayed.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered 'login.html' template with the form or redirect to the home page on successful login.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'band/login.html', {'form': form})


def sign_out(request):
    """
    Log out the current user and redirect to the index page.

    This view function logs out the current user and then redirects them to the home page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Redirect to the home page.
    :rtype: HttpResponseRedirect
    """
    logout(request)
    return HttpResponseRedirect(reverse('index'))
