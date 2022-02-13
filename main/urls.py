from django.urls import path 

from . import views 


urlpatterns = [
    path('astore_list/', views.AStoreListView.as_view(), name='astore_list'),
    path('create_visit/', views.CreateVisitView.as_view(), name='create_visit'),
]
