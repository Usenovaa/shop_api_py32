from django.urls import path
from .views import RegisterView, ActivateView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivateView.as_view(), name='activate')
]