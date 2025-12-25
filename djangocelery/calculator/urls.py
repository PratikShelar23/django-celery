from django.urls import path
from .views import calculate,get_result

urlpatterns = [
    path('calc/', calculate),
    path('result/', get_result),
]
