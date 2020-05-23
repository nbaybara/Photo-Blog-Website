import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import messages

from home.forms import SearchForm
from home.models import Setting, ContactFormMessage, ContactFormu
from post.models import Post, Category, Comment, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Post.objects.all()[:4]
    dayposts = Post.objects.all()[:4]
    lastposts = Post.objects.all().order_by('-id')[:4]
    randposts = Post.objects.all().order_by('?')[:4]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'dayposts': dayposts,
               'lastposts': lastposts,
               'randposts': randposts,
               }
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'about',
               'category': category,

               }
    return render(request, 'about.html', context)


def references(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'references',
               'category': category}
    return render(request, 'references.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kurulumu
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message successfully send. Thank you.")
            return HttpResponseRedirect('/contact')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)


def gallery(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'gallery', 'category': category}
    return render(request, 'gallery.html', context)


def blog(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'blog', 'category': category}
    return render(request, 'blog.html', context)


def category_posts(request, id, slug):
    posts = Post.objects.filter(category_id=id)
    categorydata = Category.objects.get(pk=id)
    category = Category.objects.all()
    context = {'posts': posts, 'category': category,
               'categorydata': categorydata}
    return render(request, 'posts.html', context)


def post_detail(request, id, slug):
    category = Category.objects.all()
    post=Post.objects.get(pk=id)
    images=Images.objects.filter(post_id=id)
    comments=Comment.objects.filter(post_id=id,status=True)
    context = {'category': category,
               'post': post,
               'image' : images,
               'comments' : comments,
               }
    return render(request, 'post_detail.html', context)

def post_search(request):
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query=form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            post=Post.objects.filter(title__icontains=query) #Select *from product like%query
            context = {'post':post,
                       'category':category,}
            return render(request,'post_search.html',context)

    return  HttpResponseRedirect('/')


def post_search_auto(request):

        if request.is_ajax():
            q = request.GET.get('term', '')
            post = Post.objects.filter(city__icontains=q)
            results = []
            for rs in post:
                post_json = {}
                post_json = rs.title
                results.append(post_json)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)

