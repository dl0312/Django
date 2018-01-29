from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	selected_post = get_object_or_404(Post, pk=pk)
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
	return render(request, 'blog/post_detail.html', {'posts':posts, 'selected_post':selected_post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.is_public = True
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
    	return redirect(post)

    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		post.delete()
		return redirect('post_list')
	return render(request, 'blog/post_confirm_delete.html', {'post': post})

@login_required
def comment_new(request,pk):
	if request.method == "POST":
		form = CommentForm(request.POST or None)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.objects.get(pk=pk)
			comment.author = request.user
			comment.save()
			return redirect('post_detail',pk)
	else:
		form = CommentForm()
	return render(request, 'blog/post_form.html', {'form': form})

@login_required
def comment_edit(request,post_pk,pk):
	comment = Comment.objects.get(pk=pk)
	if comment.author != request.user:
		return redirect(comment.post)

	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.objects.get(pk=post_pk)
			comment.save()
			return redirect(comment.post)
	else:
		form = CommentForm(instance=comment)
	return render(request, 'blog/post_form.html', {'form': form})

@login_required
def comment_delete(request,post_pk,pk):
	comment = Comment.objects.get(pk=pk)
	if request.method == "POST":
		comment.delete()
		return redirect(comment.post)
	return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})