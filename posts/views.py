from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 1. LANDING PAGE (Hero Section with Waves)
def home(request):
    """
    Renders the beautiful landing page with the frozen waves.
    Does not show posts here to keep the UI clean.
    """
    return render(request, 'index.html')

# 2. EXPLORE PAGE (All Posts List)
def post_list(request):
    # 1. Define the categories here so the template can use them
    categories = ['All', 'Articles', 'Poems', 'Stories']
    
    active_category = request.GET.get('category', 'All')
    
    if active_category and active_category != 'All':
        posts = Post.objects.filter(category=active_category).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
        
    context = {
        'posts': posts, 
        'categories': categories, # Now 'categories' is available in the HTML
        'active_category': active_category
    }
    return render(request, 'post_list.html', context)

# 3. CREATE POST
@login_required 
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # Success message MUST come before the redirect
            messages.success(request, "Your story has been published to the garden! ✨") 
            return redirect('post_list') 
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

# 4. EDIT POST
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save() 
            # Success message MUST come before the redirect
            messages.success(request, "Changes saved successfully. ✅")
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

# 5. DELETE POST
@login_required
def post_delete(request, post_id):
    """
    Handles post deletion after a confirmation step.
    """
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})
def post_detail(request, post_id):
    # Retrieve the specific post or show 404 if not found
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
def about(request):
    return render(request, 'about.html')