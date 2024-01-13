from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path('edit/<str:title>/', views.edit, name='edit'),
    path("random_entry/", views.random_entry, name="random_entry")
    
]

