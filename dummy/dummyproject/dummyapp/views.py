from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MvieForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    return render(request,'index.html',{'movie':movie})

def detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        year = request.POST.get('year',)
        desc = request.POST.get('desc',)
        img = request.FILES['img']
        movie = Movie(name=name,year=year,desc=desc,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MvieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')