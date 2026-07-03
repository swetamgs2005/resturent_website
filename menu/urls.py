from django.urls import path
from . import views
from .views import home, place_order


urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu_page, name="menu"),
    path('reservation/', views.reservation, name="reservation"),
    path("login/", views.login_view, name="login"),
    path('order/', place_order, name='place_order'),

]
