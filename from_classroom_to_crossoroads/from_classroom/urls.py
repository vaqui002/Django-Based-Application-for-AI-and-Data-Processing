from django.contrib import admin
from django.urls import path
from career_counseling import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Predict_dropouts', views.predict_dropouts, name='predict_dropouts'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),

    # Authentication pages
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # Blog pages
    path('blog/', views.blog_view, name='blog'),
    path('blog/create/', views.create_blog_view, name='create_blog'),
    path('blog/delete/<int:post_id>/', views.delete_blog_view, name='delete_blog'),
    path('blog/like/<int:post_id>/', views.like_blog_view, name='like_blog'),
    path('blog/comment/<int:post_id>/', views.add_comment_view, name='add_comment'),

    # Dropout Analysis
    path('dropout_analysis/', views.dropout_analysis_view, name='dropout_analysis'),

    # Admin Dashboard
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),

    # Blog deletion
    path('blog/delete/<int:post_id>/', views.delete_blog_view, name='delete_blog'),

    # Dropout Result Page
    path('dropout_analysis/result/', views.predict_dropouts, name='dropout_result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
