from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="backend_home"),
    path('blog_new/', views.BlogNewPage.as_view(), name="blog_new"),
    path('blog_list/', views.BlogListPage.as_view(), name="blog_list"),
]
