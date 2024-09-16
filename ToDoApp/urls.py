from django.urls import path
from .views import getMyTodoView , CreateTodoView , EditTodoView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('', getMyTodoView.as_view()),
    path('newtodo/', CreateTodoView.as_view()),
    path('edittodo/<int:id>', EditTodoView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]