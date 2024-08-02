from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Home page view
def home(request):
    return render(request, 'core/home.html')

# Rooms listing and availability view
@login_required
def rooms(request):
    # Logic to get available rooms
    return render(request, 'core/rooms.html')

# Reservation form view
@login_required
def reserve(request):
    if request.method == 'POST':
        # Logic to handle reservation submission
        pass
    return render(request, 'core/reserve.html')

# User reservations view
@login_required
def reservations(request):
    # Logic to get user's reservations
    return render(request, 'core/reservations.html')

# User profile page view
@login_required
def profile(request):
    if request.method == 'POST':
        # Logic to update profile
        pass
    return render(request, 'core/profile.html')

# Reports and analytics view (admin only)
@staff_member_required
def reports(request):
    # Logic to generate reports
    return render(request, 'core/reports.html')
