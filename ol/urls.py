from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("dishes/", views.dishes, name = "dishes"),
    path("dish/<int:dish_id>/", views.dish_components, name="dish_components")
]