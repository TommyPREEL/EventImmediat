from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from EventImmediatApp.models import Events, EventsParticipants
from EventImmediatApp.forms import EventCreationForm


# Create your views here.

# Function to render the home page
def home(request):
    active_page = 'home'
    return render(request, 'EventImmediatApp/home.html', {'active_page': active_page})

# Function to render the list of events
# If the user is logged in, check if the user has already joined the event
def events_list(request):
    active_page = 'events'
    events = Events.objects.all().order_by('-date_creation')
    if request.user.is_authenticated:
        for event in events:
            if EventsParticipants.objects.filter(event=event, user=request.user).exists():
                event.is_joined = True
    return render(request, 'EventImmediatApp/events_list.html', {'events':events, 'active_page': active_page})

# Function to render the event creation form
def events_create(request):
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
        active_page = 'events'
        if request.method == 'POST':
            form = EventCreationForm(request.POST)
            if form.is_valid():
                final_form = form.save(commit=False)
                final_form.creator_id = request.user.id
                form.save()
                return redirect('EventImmediatApp:events_list')
        else:
            form = EventCreationForm()
        return render(request, 'EventImmediatApp/events_create.html', {'form': form, 'active_page': active_page})
    else:
        return redirect(request, 'EventImmediatApp:events_list')

def events_details(request, id):
    active_page = 'events'
    event = get_object_or_404(Events, id_events=id)
    if request.user.is_authenticated:
        is_participant = EventsParticipants.objects.filter(event=event, user=request.user).exists()
        if request.user.is_superuser or (request.user == event.creator):
            participants = EventsParticipants.objects.filter(event=event).order_by('-user')
        else:
            participants = None
        return render(request, 'EventImmediatApp/events_details.html', {'event': event, 'participants': participants, 'is_participant': is_participant, 'active_page': active_page })
    else:
        return render(request, 'EventImmediatApp/events_details.html', {'event': event, 'active_page': active_page})

def events_delete(request, id):
    event = get_object_or_404(Events, id_events=id)
    if request.user.is_authenticated and ((request.user.is_staff and request.user.id == event.creator_id) or request.user.is_superuser):
        event.delete()
    return redirect('EventImmediatApp:events_list')

def events_edit(request, id):
    active_page = 'events'
    event = get_object_or_404(Events, id_events=id)
    if (request.user.is_staff and request.user.id == event.creator_id) or request.user.is_superuser:
        if request.method == 'POST':
            form = EventCreationForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('EventImmediatApp:events_details', id)
        else:
            form = EventCreationForm(instance=event)
        return render(request, 'EventImmediatApp/events_edit.html', {'form': form, 'active_page': active_page, 'event': event})
    else:
        return redirect('EventImmediatApp:events_list')
    
def events_join(request, id):
    event = get_object_or_404(Events, id_events=id)
    is_participant = EventsParticipants.objects.filter(event=event, user=request.user).exists()
    if not is_participant:
        EventsParticipants.objects.create(event=event, user=request.user)
    return redirect('EventImmediatApp:events_details', id)

def events_me(request):
    active_page = 'my_events'
    events_participants = EventsParticipants.objects.filter(user=request.user).order_by('-event')
    return render(request, 'EventImmediatApp/events_me.html', {'events_participants':events_participants, 'active_page': active_page})

def events_cancel(request, id):
    event_participant = get_object_or_404(EventsParticipants, event_id=id, user_id=request.user)
    event_participant.delete()
    return redirect('EventImmediatApp:events_details', id)


def register(request):
    if not request.user.is_authenticated: 
        active_page = 'sign_in'
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('EventImmediatApp:events_list')
            else:
                return render(request, 'EventImmediatApp/register.html', {'form': form, 'active_page': active_page})
        else:
            form = RegisterForm()
        return render(request, 'EventImmediatApp/register.html', {'form':form, 'active_page': active_page})
    else:
        return redirect('EventImmediatApp:events_list')

def connection(request):
    if not request.user.is_authenticated: 
        active_page = 'log_in'
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("EventImmediatApp:events_list")
            else:
                return render(request, 'EventImmediatApp/login.html', {'form': form, 'error': "Bad credentials.", 'active_page': active_page})
        else:
            form = AuthenticationForm()
            return render(request, 'EventImmediatApp/login.html', {'form': form, 'active_page': active_page})
    else:
        return redirect('EventImmediatApp:events_list')
    
def disconnection(request):
    if request.user.is_authenticated: 
        logout(request)
    return redirect("EventImmediatApp:events_list")