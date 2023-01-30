from django.urls import path

from .views import my_view

from .views import (
    AboutPageView,
    HomePageView,
    SnackListView,
    SnackDetailView,
    SnackUpdateView,
    SnackCreateView,
    SnackDeleteView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('snacks/', SnackListView.as_view(), name='list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='update'),
    # path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('create/', my_view, name='create'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='delete'),
]
