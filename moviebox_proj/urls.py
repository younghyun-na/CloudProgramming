from django.contrib import admin
from django.urls import path, include
from moviebox_app import views
from accounts import views as accounts_views
from review import views as review_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('detail/<str:movie_id>', views.detail, name="detail"),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('add/', review_views.PostCreate.as_view(), name='post_form'),
    path('reviews/', review_views.PostList.as_view()),
    # path('reviews/<int:pk>/', review_views.PostDetail.as_view(), name='post_detail'),
    # path('reviews/update/<int:pk>/', review_views.PostUpdate.as_view(), name='update_post'),

]
