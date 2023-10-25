from django.shortcuts import render,redirect
from .models import Home,Comment,Aboutme
from django.contrib import messages
from .forms import TodoCreateForm,TodoUpdateForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.template.response import TemplateResponse

def home(request):
    all = Home.objects.all()
    p = Paginator(all, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return render(request,'home.html',{'todos':page_obj})

    

def detail(request,todo_id):
    todo = Home.objects.get(id=todo_id)
    comments = todo.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = todo
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'detail.html',{'todo':todo,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})

@login_required(login_url="home")
def delete(request,todo_id):
    Home.objects.get(id=todo_id).delete()
    messages.success(request,'Todo deleted successfully',extra_tags='success')
    return redirect('home')

@login_required(login_url="home")
def create(request):
    if request.method =='POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Home.objects.create(title=cd['title'],body=cd['body'],created=cd['created'],decriptions=cd['decriptions'],img=cd['img'],author=cd['author'])
            messages.success(request, 'Todo created successfully','success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request,'create.html',{'form':form})

@login_required(login_url="home")
def update(request,todo_id):
    todo = Home.objects.get(id=todo_id)
    if request.method =='POST':
        form = TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your todo updated successfully','success')
            return redirect('details',todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request,'update.html',{'form':form})

def search(request):
    search_post = request.GET.get('search')
    posts = Home.objects.filter(Q(title__icontains=search_post) | Q(body__icontains=search_post))
    return render(request,'search.html',{'posts':posts})

def aboutme(request):
    about = Aboutme.objects.all()
    return render(request,'aboutme.html',{'about':about})

def contactme(request):
    response = TemplateResponse(request,'contactme.html')
    return response