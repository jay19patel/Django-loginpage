from.import views
from django.urls import path


urlpatterns = [
    path('', views.Homepage, name="Homepage"),
    path('Loginpage/', views.Loginpage, name="Loginpage"),
    path('Logout/', views.Logout, name="Logout"),
    path('Registrationpage/', views.Registrationpage, name="Registrationpage"),
    path('Test/', views.Test, name="Test"),
  
]