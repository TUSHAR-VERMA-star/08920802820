from django.urls import path, include
from watchlist_app.api import views
from .views import NumbersView

urlpatterns = [
    path('',views.showList),
    path('numbers/', NumbersView.as_view(), name='numbers'),
]

