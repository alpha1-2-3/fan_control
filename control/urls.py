from django.urls import path
from .views import set_speed, home  # Import home view

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('set_speed/', set_speed, name='set_speed'),
]
