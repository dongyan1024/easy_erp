from django.urls import path
from . import views
app_name='inventory_manage'
urlpatterns = [
    path('', views.index, name='index'),
    path('types', views.inventory, name='type'),
    path('element/<int:type_id>/', views.element, name='element'),
    path('new_type', views.new_type, name='new_type'),
    path('new_element/<int:type_id>', views.new_element, name='new_element'),
    path('edit_element/<int:element_id>', views.edit_element, name='edit_element'),
    #path('search/', views.My_search, name='My_search'),
]