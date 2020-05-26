from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import UserProfile
from post.models import Category, Post


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    #return HttpResponse(profile)
    sliderdata = Post.objects.all()[:4]
    context = {'profile' : profile,
               'sliderdata': sliderdata,
                'category': category, }
    return render(request, 'user_profile.html',context)
