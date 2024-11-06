from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.home, name = 'home'),
    path('', views.tweet_list, name = 'tweet_list'),
    path('create/', views.create_tweet, name = 'create_tweet'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name = 'edit_tweet'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name = 'delete_tweet'),
    path('accounts/register/', views.register, name = 'register'),
    path('accounts/profile/', views.profile_view, name='profile'),
] 