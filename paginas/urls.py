from django.urls import path

from .views import homePageView, sobreView

urlpatterns = [
    path('', homePageView, name='home'),
    path('sobre', sobreView, name='sobre')
]