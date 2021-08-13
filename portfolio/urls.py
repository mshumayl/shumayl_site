from django.urls import path 
# from . import views 
from .views import BlogView, ArticleDetailsView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
from . import views


urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    path('', BlogView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name="article-details"),
    path('add-post/', AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('add-category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>', CategoryView, name="category")
    
    # path('', views.home, name="home"),
    # path('blog/<int:pk>', BlogDetailsView.as_view(), name="blog-single")
]