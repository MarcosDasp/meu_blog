from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('-data_publicacao')  # Posts mais recentes primeiro
    return render(request, 'blog/index.html', {'posts': posts})

@login_required
def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Atribui o autor do post ao usuário logado
            post.save()
            return redirect('index')  # Redireciona para a página inicial (ou onde você preferir)
    else:
        form = PostForm()
    
    return render(request, 'blog/criar_post.html', {'form': form})