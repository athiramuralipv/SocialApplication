from django.contrib import admin
from django.urls import path
from api import views

urlpatterns=[
    path("admin/",admin.site.urls),
    path("blogs/",views.BlogListView.as_view()),
    path("blogs/<int:postId>",views.BlogDetailView.as_view())
]