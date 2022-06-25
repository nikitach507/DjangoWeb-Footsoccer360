from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('premierleague', views.news_pl, name='news_pl'),
    path('laliga', views.news_ll, name='news_ll'),
    path('seriaa', views.news_sa, name='news_sa'),
    path('transfers', views.news_transfers, name='news_transfers'),
    path('ligamistru', views.news_lm, name='news_lm'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]