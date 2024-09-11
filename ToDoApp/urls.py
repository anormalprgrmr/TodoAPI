from django.urls import path
from .views import getMyTodoView

urlpatterns = [
    path('', getMyTodoView.as_view()),
]