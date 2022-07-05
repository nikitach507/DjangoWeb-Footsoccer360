from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import *
from django.http import HttpResponse


def index(request):
    posts = Allnews.objects.all()

    data = {
        'posts': posts,
        'cat_selected': 0,
    }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def show_post(request, post_id):
    return HttpResponse(f"Id-post = {post_id}")


def show_category(request, cat_id):
    posts = Allnews.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    data = {
        'posts': posts,
        'cat_selected': cat_id,
    }

    return render(request, 'main/cat_premierleague.html', data)


def gift_home(request):
    main = Givegift.objects.order_by('-first_name_participant')#[:1]
    return render(request, 'main/gift_info.html', {'main': main})


def gift_form(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Formulář byl špatný'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/gift.html', data)
