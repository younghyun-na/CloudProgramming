from django.contrib import admin
from django.urls import path, include
from moviebox_app import views
from accounts import views as accounts_views
from board import views as board_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('detail/<str:movie_id>', views.detail, name="detail"),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),

    path('posts/', board_views.postlist, name='post_list'),
    path('posts/add', board_views.addpost, name='post_form'),
    path('posts/<int:post_id>', board_views.postdetail, name='post_detail'),
    path('posts/<int:post_id>/modify', board_views.postmodify, name='post_modify'),
    path('posts/<int:post_id>/delete', board_views.postdelete, name='post_delete'),
]

