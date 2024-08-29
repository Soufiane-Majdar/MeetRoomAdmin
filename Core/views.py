from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Reservation, BeverageOrder, Notification, Report, User
from .forms import ReservationForm, BeverageOrderForm, RoomForm
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Home page view
def home(request):
    rooms = Room.objects.all()
    return render(request, 'core/home.html', {'rooms': rooms})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Room CRUD views
@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'core/room_list.html', {'rooms': rooms})

@login_required
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'core/room_detail.html', {'room': room})

@login_required
def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'core/room_form.html', {'form': form})

@login_required
def room_update(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'core/room_form.html', {'form': form})

@login_required
def room_delete(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('room_list')

# Reservation Views
@login_required
def reservation_list(request):
    # Incorrect usage
    reservations = Reservation.objects.filter(user=request.user.username)
    
    # Correct usage
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'core/reservation_list.html', {'reservations': reservations})
    
@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'core/reservation_form.html', {'form': form})

@login_required
def reservation_cancel(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    reservation.status = 'cancelled'
    reservation.save()
    return redirect('reservation_list')

# BeverageOrder Views
@login_required
def beverage_order_list(request):
    orders = BeverageOrder.objects.filter(reservation__user=request.user)
    return render(request, 'core/beverage_order_list.html', {'orders': orders})

@login_required
def beverage_order_create(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        form = BeverageOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.reservation = reservation
            order.save()
            return redirect('beverage_order_list')
    else:
        form = BeverageOrderForm()
    return render(request, 'core/beverage_order_form.html', {'form': form})

@login_required
def beverage_order_complete(request, order_id):
    order = get_object_or_404(BeverageOrder, id=order_id, reservation__user=request.user)
    order.status = 'completed'
    order.save()
    return redirect('beverage_order_list')

# Notification views
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return render(request, 'core/notifications.html', {'notifications': notifications})

# Report view (Admin)
@login_required
def report_list(request):
    if request.user.role != 'admin':
        return HttpResponse("Unauthorized", status=401)
    reports = Report.objects.all()
    return render(request, 'core/report_list.html', {'reports': reports})
