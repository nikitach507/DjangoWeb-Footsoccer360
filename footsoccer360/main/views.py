from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Givegift

def index(request):
    return render(request, 'main/index.html')


def gift_home(request):
    main = Givegift.objects.order_by('-first_name_participant')#[:1]
    return render(request, 'main/gift_info.html', {'main': main})


def about(request):
    return render(request, 'main/about.html')


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
