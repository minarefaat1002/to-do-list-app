from django.urls import path
from . import views
urlpatterns = [
    path('',views.all,name="all"),
    path('all',views.all,name="all"),
    path('active',views.active,name='active'),
    path('completed',views.completed,name='completed'),
    path('task-create/',views.TaskCreate.as_view(),name='task-create'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name="task-detail"),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name="task-delete"),
    ]