from django.contrib.auth.views import LogoutView
from django.urls import path

from pushes.views import PushesCreateView, UpdateUser, HomeView, UserLoginView, \
    OptionsCreateView, OptionsUpdateView, OptionsDeleteView

app_name = 'pushes'

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update_user/<int:id>', UpdateUser.as_view(), name='update_user'),
    path('create_pushes/', PushesCreateView.as_view(), name='create_pushes'),
    path('option_create/', OptionsCreateView.as_view(), name='options_create'),
    path('option_update/<int:id>', OptionsUpdateView.as_view(), name='options_update'),
    path('option_delete/<int:id>', OptionsDeleteView.as_view(), name='options_delete')

]
