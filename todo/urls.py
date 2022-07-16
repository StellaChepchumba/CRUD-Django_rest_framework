from django.urls import path
from .views import TodoAPIView

urlpatterns = [
        path('todo', TodoAPIView.as_view()),
        path('todo/<str:pk>', TodoAPIView.as_view()) # to capture our ids
    ]

