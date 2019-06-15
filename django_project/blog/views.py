from django.shortcuts import render
# Create your views here.
posts = [
    {
        'author': 'Manny Aguilar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'dateposted': 'June 11, 1998'

    },
    {
        'author': 'Booger',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'dateposted': 'June 11, 1999'


    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)




def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
