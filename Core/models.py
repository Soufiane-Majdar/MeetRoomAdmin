from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',  # Add related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions_set',  # Add related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username




class Room(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    amenities = models.TextField(help_text="List of amenities separated by commas.")

    def __str__(self):
        return self.name





class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room.name} reserved by {self.user.username} on {self.start_time}"




class BeverageOrder(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    items = models.TextField(help_text="List of ordered items separated by commas.")

    def __str__(self):
        return f"Beverage order for {self.reservation.room.name} reserved by {self.reservation.user.username}"



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} at {self.sent_at}"




class Report(models.Model):
    generated_at = models.DateTimeField(auto_now_add=True)
    report_data = models.TextField(help_text="JSON or text-based report data")

    def __str__(self):
        return f"Report generated at {self.generated_at}"
