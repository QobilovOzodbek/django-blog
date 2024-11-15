from django.urls import *
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]