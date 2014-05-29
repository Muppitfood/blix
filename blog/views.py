from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category
from users.models import User

# Create your views here.


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
        'users': User.objects.all()
    })


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('view_post.html', {
        'post': post,
        'user': get_object_or_404(User, id=post.user_id)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })