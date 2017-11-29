from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Post

# Create your views here.

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    time = instance.timestamp
    context = {
        "time": time,
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
        ).distinct()
    context = {
        "object_list": queryset,
        }
    return render(request, "post_list.html", context)

def post_contact(request):
    queryset = Post.objects.order_by('-timestamp')[:7]
    context = {
        "object_list": queryset,
        }
    return render(request, "contact.html", context)