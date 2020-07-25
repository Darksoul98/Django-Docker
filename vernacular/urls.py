from django.urls import path, include
from . import views

urlpatterns = [
    path("finite/", views.finitevalues.as_view(), name="finite"),
    path("numeric/", views.numeric.as_view(), name="numeric"),

]