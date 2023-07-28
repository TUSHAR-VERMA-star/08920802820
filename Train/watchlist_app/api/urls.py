from django.urls import path, include
from watchlist_app.api import views
from .views import CompanyView, TrainListView, TrainListItemView

urlpatterns = [
    path('',views.showList),
    path('train/register', CompanyView.as_view(), name='numbers'),
    path('train/trains', TrainListView.as_view(), name='train-list'),
    path('train/trains/<int:id>', TrainListItemView.as_view(), name='train-list-item')
]

