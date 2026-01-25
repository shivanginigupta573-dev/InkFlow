from django.urls import path
from . import views

urlpatterns = [
    # The Hero Landing Page (index.html)
    path('', views.home, name='home'),  

    # The Explore Page (post_list.html)
    path('explore/', views.post_list, name='post_list'),

    # Post Management
    path('write/', views.post_create, name='post_create'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    #for reading posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    #about apge
    path('about/', views.about, name='about_us'),
]
