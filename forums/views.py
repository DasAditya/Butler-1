from django.shortcuts import render, get_object_or_404
from .models import Post, Topic


# Create your views here.

def index(request):
    topics = Topic.objects.all()
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    context = {'base_template': base,
               'topics': topics}
    return render(request, 'forums/forum.html', context)


def add_topic(request):
    topic = request.POST['topic']
    category = request.POST['category']
    a = Topic()
    a.title = topic
    a.category = category
    a.user = request.user
    a.save()
    return index(request)


def add_post(request, pk):
    post = request.POST['post']
    topic = get_object_or_404(Topic, pk=pk)
    a = Post()
    a.user = request.user
    a.topic = topic
    a.msg = post
    a.save()
    topic.no_of_posts += 1
    topic.save()
    return index(request)