from django.urls import path
from . import views
from .views import postListView , postDetailView , postCreateView , postUpdateView , postDeleteView

urlpatterns=[
     path('',views.index,name='index'),

     path('about/',views.about,name='about'),
     path('home',postListView.as_view(),name='home'),
     path('post/new',postCreateView.as_view(),name='post_create'),
     path('post/<int:pk>',postDetailView.as_view(),name='post_detail'),
     path('post/<int:pk>/update',postUpdateView.as_view(),name='post_update'),
     path('post/<int:pk>/delete',postDeleteView.as_view(),name='post_delete')


]