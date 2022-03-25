from django.urls import path

from .views import CardAPIView

urlpatterns = [
    path('cards/', CardAPIView.as_view()),
]