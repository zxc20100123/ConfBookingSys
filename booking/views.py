import datetime

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import SignupForm, SigninForm, SearchForm
from .models import Employee, Room, RoomBooked


# Create your views here.
@login_required(login_url='/signin/')
def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            avarooms = Room.objects.exclude(Q(cap__lt=int(form.data['hc']))
                                            | (Q(room__bookedDate=form.cleaned_data['date'])
                                               & Q(room__bookedHour=form.data['hour'])))
            request.session['bookdate'] = form.cleaned_data['date'].strftime("%Y-%m-%d")
            request.session['bookhour'] = form.data['hour']
            if not avarooms.exists():
                messages.error(request, "No room available at the time you selected..")
            return render(request, 'index.html', {'form': form, 'avarooms': avarooms})
        else:
            messages.error(request, 'Date must not be in the past')
            print(form.errors.as_data())
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='/signin/')
def booking(request, pk):
    room = Room.objects.get(pk=pk)
    date = datetime.datetime.strptime(request.session['bookdate'], "%Y-%m-%d").date()
    RoomBooked.objects.create(user=request.user, room=room, bookedDate=date, bookedHour=request.session['bookhour'])

    return redirect('history')


@login_required(login_url='/signin/')
def history(request):
    user = request.user
    today = datetime.datetime.today().date()
    rooms = RoomBooked.objects.filter(user=user, bookedDate__gte=today).order_by('bookedDate', 'bookedHour')

    return render(request, 'history.html', {'bookedrooms': rooms})


@login_required(login_url='/signin/')
def cancel(request, pk):
    room = RoomBooked.objects.get(pk=pk)
    room.delete()

    return redirect('history')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = User.objects.create_user(username=username, password=password, email=email)
            try:
                tempID = Employee.objects.order_by('id')[0].id
            except:
                tempID = 0
            employee = Employee(user=user, employeeID=tempID + 1)
            employee.save()

            return redirect('/signin/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('/home/')
            else:
                return render(request, 'signin.html', {'form': form, 'message': 'Wrong password, please try again'})
    else:
        if request.user.is_authenticated:
            return redirect('/home/')
        else:
            form = SigninForm()

    return render(request, 'signin.html', {'form': form})


@login_required(login_url='/signin/')
def signout(request):
    auth.logout(request)
    return redirect('/signin/')
