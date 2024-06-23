from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .apps import BlogConfig
from pytils.translit import slugify
from django.urls import reverse_lazy
# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'body', 'image_preview', 'is_public', ]
    success_url = reverse_lazy('blog:blog_view')
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Создать блог'
    }

    def form_valid(self, form):
        # получает на вход форму, изменяет в атрибуте slug, сохраняет в БД
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Список блогов',
    }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Детализация блога'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body', 'image_preview', 'is_public', ]
    success_url = reverse_lazy('blog:blog_view')
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Обновление блога'
    }

    def form_valid(self, form):
        # получает на вход форму, изменяет в атрибуте slug, сохраняет в БД
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_view')
