from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
   # path('<int:question_id>/', views.detail, name='detail'),
    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('addpost/', views.addpost, name='addpost'),
    path('post/', views.post, name='post'),
    path('editpost/<int:id>', views.editpost, name='editpost'),
    path('deletepost/<int:id>', views.deletepost, name='deletepost'),
    path('imageaddpost/<int:id>', views.imageaddpost, name='imageaddpost')


]