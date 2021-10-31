from django.urls import include, path
from django.contrib import admin
from .views import (ArticleListView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleCreateView
    )

urlpatterns = [
    path("create/", ArticleCreateView.as_view(), name="article_new"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('details/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('', ArticleListView.as_view(), name='article_list'),
]
