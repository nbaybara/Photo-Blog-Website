from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import messages

from home.models import Setting, ContactFormMessage, ContactFormu
from post.models import Post


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Post.objects.all()[:]
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'about'}
    return render(request, 'about.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'references'}
    return render(request, 'references.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()   # model ile bağlantı kurulumu
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message successfully send. Thank you.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def gallery(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'gallery'}
    return render(request, 'gallery.html', context)


def blog(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'blog'}
    return render(request, 'blog.html', context)
