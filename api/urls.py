from django.urls import path
from .views import ShortUrlCreateView

from . import views

urlpatterns = [
    path('shortUrl/', ShortUrlCreateView.as_view(), name='short_url_create_view'),
]