from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Board

# Create your views here.

def home(req):
    boards = Board.objects.all()
    return render(req,'home.html',{'boards':boards})

def board_topics(req,board_id):
    
    # board = Board.objects.get(id=board_id)
    board = get_object_or_404(Board,pk=board_id)
    return render(req,'topics.html',{'board':board})



def about(request):
    return HttpResponse('<h1>About</h1>')