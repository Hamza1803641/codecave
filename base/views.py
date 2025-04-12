from django.shortcuts import render
# Create your views here.

rooms=[
    {'id':1,'name':'Lets Learn python!'},
    {'id':2,'name':'Lets Learn Django!'},
    {'id':3,'name':'Lets Design!'},
    {'id':4,'name':'Lets Learn Java!'},
    {'id':5,'name':'Lets Learn C++!'},
    {'id':6,'name':'Lets Learn C#!'},
]


def home(request):
    return render(request,'base/home.html',{'rooms':rooms})

def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    context={'room':room}         
    return render(request,'base/room.html',context)