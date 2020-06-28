from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from judapp.forms import JudSiteForm
from judapp.models import JudSite


class JudSiteList(ListView):
    model = JudSite

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список судебных участков'
        return context


class JudSiteDelete(DeleteView):
    model = JudSite
    success_url = reverse_lazy('judapp:index')


class JudSiteCreate(CreateView):
    model = JudSite
    success_url = reverse_lazy('judapp:index')
    form_class = JudSiteForm


class JudSiteUpdate(UpdateView):
    model = JudSite
    success_url = reverse_lazy('judapp:index')
    form_class = JudSiteForm
