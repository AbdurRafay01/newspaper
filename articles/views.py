from re import template
from django.contrib.auth.mixins import LoginRequiredMixin #for login checks
from django.core.checks import model_checks
from django.db.models import fields
from django.forms import forms
from django.shortcuts import render
from django.utils.translation import deactivate
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django import forms
# Create your views here.

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article_list'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


# EDITING generic class based views

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'body')
    template_name = "article_new.html"
    login_url = "login" # the mixing redirects the user to login page if user attempts to access create article page from search bar

    def form_valid(self, form):
        form.instance.author = self.request.user
        print("Checking user : ",self.request.user)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')