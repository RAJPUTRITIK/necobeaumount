from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry_data/', views.entry_data, name='entry_data'),
    path('wing/', views.wing, name='wing'),
    path('building_a/', views.building_a, name='building_a'),
    path('building_b/', views.building_b, name='building_b'),
    path('floor_room_a/<int:i>', views.floor_room_a, name='floor_room_a'),
    path('floor_room_b/<int:i>', views.floor_room_b, name='floor_room_b'),
    path('building_a_data/<int:room>', views.building_a_data, name='building_a_data'),
    path('building_b_data/<int:room>', views.building_b_data, name='building_b_data'),
    path('update_building_a_data/', views.update_building_a_data, name='update_building_a_data'),
]

