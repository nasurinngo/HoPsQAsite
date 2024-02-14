from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('HoPsapp/', views.ListHoPsView.as_view(), name='list-HoPsapp'),
    path('HoPsapp/<int:pk>/detail/', views.DetailHoPsView.as_view(), name='detail-HoPsapp'),
    path('HoPsapp/create/', views.CreateHoPsView.as_view(), name='create-HoPsapp'),
    path('HoPsapp/<int:pk>/delete/', views.DeleteHoPsView.as_view(), name='delete-HoPsapp'),
    path('HoPsapp/<int:pk>/update/', views.UpdateHoPsView.as_view(), name='update-HoPsapp'),
    path('HoPsapp/<int:HoPsapp_id>/review/', views.CreateReviewView.as_view(), name='review'),
]