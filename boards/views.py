from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Board,Topic,Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

def home(req):
    boards = Board.objects.all()
    return render(req,'home.html',{'boards':boards})

def board_topics(req,board_id):
    
    # board = Board.objects.get(id=board_id)
    board = get_object_or_404(Board,pk=board_id)
    return render(req,'topics.html',{'board':board})


@login_required
def new_topic(req,board_id):
    board = get_object_or_404(Board,pk=board_id)
    
    if req.method == 'POST':
        subject = req.POST['subject']
        message = req.POST['message']
        # user = User.objects.first()
        
        topic = Topic.objects.create(
            subject=subject,
            board=board,
            created_by=req.user,
        )
        
        post = Post.objects.create(
            message=message,
            topic = topic,
            created_by = req.user
        )
        
        return redirect('board_topics',board_id=board.pk)
    
    return render(req,'new_topic.html',{'board':board})


def topic_posts(req,board_id,topic_id):
    topic = get_object_or_404(Topic,board__pk=board_id,pk=topic_id)
    
    return render(req,'topic_posts.html',{'topic':topic})
    
        
@login_required
def reply_topic(req,board_id,topic_id):
    
    topic = get_object_or_404(Topic,board__pk=board_id,pk=topic_id)
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = req.user
            post.save()
            return redirect('topic_posts',board_id=board_id,topic_id=topic_id)
    else:
        form = PostForm()
    return render(req,'reply_topic.html',{'topic':topic,'form':form})

def about(request):
    return HttpResponse('<h1>About</h1>')