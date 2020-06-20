from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile, Setting, FAQ
from post.models import Category, Post, Comment, Images
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import PostForm, PostImageForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile' : profile,
                'category': category, }
    return render(request, 'user_profile.html',context)

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('/user')
    else:
            category = Category.objects.all()
            user_form = UserUpdateForm(instance= request.user)
            profile_form = ProfileUpdateForm(instance=request.user.userprofile)
            context = {'profile_form': profile_form,
                           'user_form':user_form,
                           'category': category, }

            return render(request,'user_update.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was succesfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request,'Please correct the error below.<br>'+ str(form.errors))
            return  HttpResponseRedirect('/user/password')
    else:
     category = Category.objects.all()
     form = PasswordChangeForm(request.user)
     return render(request,'change_password.html',{
         'form':form,'category' : category

     })

@login_required(login_url='/login')
def comments(request):
    category=Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'comments': comments,}
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request,'Comment deleted...')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login')
def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            catid = form.cleaned_data['category']
            data = Post()
            data.category_id = catid.id
            data.title = form.cleaned_data['title']
            data.keyword = form.cleaned_data['keyword']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.detail = form.cleaned_data['detail']
            data.slug = form.cleaned_data['slug']
            data.status = 'New'
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Photo successfully added.")
            return HttpResponseRedirect('/user/post')
        else:
            messages.warning(request, "Please correct the errors: " + str(form.errors))
            return HttpResponseRedirect('/user/addpost')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = PostForm()
        context = {'setting': setting,
                   'category': category,
                   'form': form
                   }
        return render(request, 'user_addpost.html', context)


@login_required(login_url='/login')
def editpost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo başarıyla güncellendi")
            return HttpResponseRedirect('/user/post')
        else:
            messages.warning(request, "Please correct the errors: " + str(form.errors))
            return HttpResponseRedirect('/user/editpost' + str(id))
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = PostForm(instance=post)
        context = {'setting': setting,
                   'category': category,
                   'form': form,
                   }
        return render(request, 'user_addpost.html', context)


@login_required(login_url='/login')
def deletepost(request, id):
    current_user = request.user
    Post.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, "Photo deleted succesfully")
    return HttpResponseRedirect('/user/post')


def imageaddpost(request, id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = PostImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = Images()
            data.title = form.cleaned_data['title']
            data.post_id = id
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, "Resim başarıyla eklendi")
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Form Error : ' + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        setting = Setting.objects.get(pk=1)
        post = Post.objects.get(id=id)
        images = Images.objects.filter(post_id=id)
        form = PostImageForm()
        context = {'setting': setting,
                   'post': post,
                   'images': images,
                   'form': form
                   }
        return render(request, 'post_gallery.html', context)

def post(request):
    category = Category.objects.all()
    current_user = request.user
    posts = Post.objects.filter(user_id=current_user.id, status=True,)
    context = {'post':posts,
                'category': category,
                }
    return render(request, 'user_post.html',context)





