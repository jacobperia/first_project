from django.urls import path

from . import views

app_name = 'urlShortener'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:url_link_id>/', views.detail, name='detail'),
    path('shorten/', views.shorten, name='shorten'),
]