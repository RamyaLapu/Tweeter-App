from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')
        Tweet.objects.create(user=request.user, content=content, image=image)
        return redirect('home')
    return render(request, 'create_tweet.html')

@login_required
def edit_tweet(request, id):
    tweet = get_object_or_404(Tweet, id=id, user=request.user)
    if request.method == 'POST':
        tweet.content = request.POST['content']
        if request.FILES.get('image'):
            tweet.image = request.FILES.get('image')
        tweet.save()
        return redirect('home')
    return render(request, 'edit_tweet.html', {'tweet': tweet})

@login_required
def delete_tweet(request, id):
    tweet = get_object_or_404(Tweet, id=id, user=request.user)
    tweet.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
