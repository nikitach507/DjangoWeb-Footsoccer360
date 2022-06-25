from django.shortcuts import render, redirect
from .models import Articles
from .models import Premierleague, Laliga, Seriaa, Ligamistru
from .models import Newtransfers
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')#[:1]
    return render(request, 'news/news_home.html', {'news': news})


def news_pl(request):
    news = Premierleague.objects.order_by('-date')#[:1]
    return render(request, 'news/news_premierleague.html', {'news': news})


def news_ll(request):
    news = Laliga.objects.order_by('-date')#[:1]
    return render(request, 'news/news_laliga.html', {'news': news})


def news_sa(request):
    news = Seriaa.objects.order_by('-date')#[:1]
    return render(request, 'news/news_seriaa.html', {'news': news})


def news_lm(request):
    news = Ligamistru.objects.order_by('-date')#[:1]
    return render(request, 'news/news_ligamistru.html', {'news': news})


def news_transfers(request):
    news = Newtransfers.objects.order_by('-first_name_transfer')#[:1]
    return render(request, 'news/news_transfers.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
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
        'error': error
    }
    return render(request, 'news/create.html', data)