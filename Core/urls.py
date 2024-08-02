from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('rooms/', views.rooms, name='rooms'),  # Rooms listing and availability
    path('reserve/', views.reserve, name='reserve'),  # Reservation form
    path('reservations/', views.reservations, name='reservations'),  # User reservations
    path('profile/', views.profile, name='profile'),  # User profile page
    path('reports/', views.reports, name='reports'),  # Reports and analytics (admin only)
]
