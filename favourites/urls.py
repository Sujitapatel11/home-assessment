from django.urls import path
from .views import FavouriteListView, FavouriteAddView, FavouriteRemoveView

urlpatterns = [
    path('', FavouriteListView.as_view(), name='favourite-list'),
    path('add/', FavouriteAddView.as_view(), name='favourite-add'),
    path('<int:pk>/remove/', FavouriteRemoveView.as_view(), name='favourite-remove'),
]
