from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag_view'),
    path('add/<item_id>', views.add_item, name='add_item'),
    path('update/<item_id>/', views.update_item, name='update_item'),
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
]
