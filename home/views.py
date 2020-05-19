from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import messages

from home.models import Setting, ContactFormMessage, ContactFormu
from post.models import Post, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Post.objects.all()[:4]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
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
    context = {'setting': setting, 'form': form,'category': category}
    return render(request, 'contact.html', context)


def gallery(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'gallery','category': category}
    return render(request, 'gallery.html', context)


def blog(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'blog','category': category}
    return render(request, 'blog.html', context)
