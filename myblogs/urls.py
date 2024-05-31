from django.urls import path
from .import views
from .import auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('writeBlog/', views.writeBlog, name='writeBlog'),
    path('yourBlog/<str:pk>/', views.yourBlog, name='yourBlog'),
    path('editBlog/<str:pk>/', views.editBlog, name='editBlog'),
    path('deleteBlog/<str:pk>/', views.deleteBlog, name='deleteBlog'),
    path('deleteComment/<str:pk>/', views.deleteComment, name='deleteComment'),
    path('blogfeed/', views.blogfeed, name='blogfeed'),

    # authentcation views
    path('loginUser/', auth_views.loginUser, name='loginUser'),
    path('logoutUser/', auth_views.logoutUser, name='logoutUser'),
    path('registerUser/', auth_views.registerUser, name='registerUser')
]