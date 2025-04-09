from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Board,Topic,Post
from django.contrib.auth.models import User

# Create your views here.

def home(req):
    boards = Board.objects.all()
    return render(req,'home.html',{'boards':boards})

def board_topics(req,board_id):
    
    # board = Board.objects.get(id=board_id)
    board = get_object_or_404(Board,pk=board_id)
    return render(req,'topics.html',{'board':board})



def new_topic(req,board_id):
    board = get_object_or_404(Board,pk=board_id)
    
    if req.method == 'POST':
        subject = req.POST['subject']
        message = req.POST['message']
        user = User.objects.first()
        
        topic = Topic.objects.create(
            subject=subject,
            board=board,
            created_by=user,
        )
        
        post = Post.objects.create(
            message=message,
            topic = topic,
            created_by = user
        )
        return redirect('board_topics',board_id=board.pk)
    
    
    return render(req,'new_topic.html',{'board':board})


def about(request):
    return HttpResponse('<h1>About</h1>')