from django.shortcuts import render
from board.models import Board
# Create your views here.
def home(request):
    return render(request, "home.html")

def board(request):
    rsBoard = Board.objects.all()
    return render(request, "board_list.html", {'rsBoard': rsBoard})