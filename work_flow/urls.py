from django.urls import path
from . import views
app_name = 'work_flow'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('<int:E_O_id>', views.detials, name='detials'),
    path('new_element/', views.new_element, name='new_element'),
    path('new_step/<int:element_id>/', views.new_step, name='new_step'),

    path('edit_working/<int:element_id>/', views.edit_working, name='edit_working'),
    path('edit_step/<int:step_id>', views.edit_step, name='edit_step'),
]