from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from pushes.forms import CustomUserForm, PushesForm, MyForm, OptionsForm
from pushes.models import CustomUser, Options, Pushes

# Create your views here.
from pushes import tasks


class HomeView(ListView):
    model = Pushes
    template_name = 'adminlte/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-create_date')


class UpdateUser(UpdateView):
    form_class = CustomUserForm
    template_name = 'registration/update_user.html'
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(CustomUser, id=id_)


class PushesCreateView(SuccessMessageMixin, CreateView):
    form_class = PushesForm
    template_name = 'adminlte/pages/edit.html'
    success_message = 'Pushes successfully create'

    def get_success_url(self):
        return '/'


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = MyForm

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)


class OptionsCreateView(CreateView):
    form_class = OptionsForm
    template_name = 'options_page/create_options.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_options'] = Options.objects.all()
        return context

    def get_success_url(self):
        return '/option_create'


class OptionsUpdateView(UpdateView):
    form_class = OptionsForm
    template_name = 'options_page/update_options.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Options, id=id_)

    def get_success_url(self):
        return '/option_create'


class OptionsDeleteView(DeleteView):
    template_name = 'options_page/delete_options.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Options, id=id_)

    def get_success_url(self):
        return '/option_create'
