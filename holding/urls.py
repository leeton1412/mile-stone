from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag_view'),
    path('add/<item_id>', views.add_item, name='add_item'),
]
