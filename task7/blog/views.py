from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):

    posts = Post.objects.filter(
        status='published'
    ).order_by('-published_date')

    context = {
        'posts': posts,
        'page_title': 'Latest Blog Posts'
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):

    post = get_object_or_404(
        Post,
        pk=pk,
        status='published'
    )

    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )