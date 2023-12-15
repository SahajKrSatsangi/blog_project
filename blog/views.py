from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can customize the redirect URL after successful registration
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs, 'user': request.user})

class BlogListCreateView(generics.ListCreateAPIView):
    print(f"Current user: dsfc")
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(f"Current user: {self.request.user}")
        serializer.save(author=self.request.user)

def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Handle form submission for creating a new blog
            pass
        return render(request, 'create_blog.html')
    else:
        return render(request, 'login_required.html')
    
def custom_logout_view(request):
    logout(request)
    return redirect('home')    
    
