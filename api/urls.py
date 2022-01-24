from django.urls import path

from .views import ImageApiView, ImageDetailApiView

urlpatterns = [
    path('<int:pk>/', ImageDetailApiView.as_view()),
    path('', ImageApiView.as_view()),
]
