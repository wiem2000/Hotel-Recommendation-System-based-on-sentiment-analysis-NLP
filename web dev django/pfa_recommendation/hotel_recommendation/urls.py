from django.urls import path

from hotel_recommendation import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_view, name='login'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('logout/', views.logout_view, name='logout'),
    
   
]