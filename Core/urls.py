from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('rooms/add/', views.room_create, name='room_create'),
    path('rooms/<int:room_id>/edit/', views.room_update, name='room_update'),
    path('rooms/<int:room_id>/delete/', views.room_delete, name='room_delete'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.reservation_create, name='reservation_create'),
    path('reservations/<int:reservation_id>/cancel/', views.reservation_cancel, name='reservation_cancel'),
    path('beverage-orders/', views.beverage_order_list, name='beverage_order_list'),
    path('beverage-orders/add/<int:reservation_id>/', views.beverage_order_create, name='beverage_order_create'),
    path('beverage-orders/<int:order_id>/complete/', views.beverage_order_complete, name='beverage_order_complete'),
    path('notifications/', views.notifications, name='notifications'),
    path('reports/', views.report_list, name='report_list'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
]
