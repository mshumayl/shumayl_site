from .models import Post, Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
import requests

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    cats = Category.objects.all()
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
        
class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'    

#Functional view and class-based view can co-exist
def CategoryView(request, cats): #Takes in a GET request and a cats from endpoint user
    category_posts = Post.objects.filter(category__iexact=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.replace('-', ' ').title(), 'category_posts': category_posts}) # {} is context dictionary for request item

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
   
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')

# class BlogDetailsView(DetailView):
#     posts = Post.objects.all()
#     template_name = 'blog-single.html'    
#     return render(request, 'blog')