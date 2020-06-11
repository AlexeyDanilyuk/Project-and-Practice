from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from jobapp.forms import JobTitleForm
from jobapp.models import JobTitle


class JobTitleList(ListView):
    model = JobTitle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список должностей'
        return context


class JobTitleDelete(DeleteView):
    model = JobTitle
    success_url = reverse_lazy('jobapp:index')


class JobTitleCreate(CreateView):
    model = JobTitle
    success_url = reverse_lazy('jobapp:index')
    form_class = JobTitleForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(data)
        return data


class JobTitleUpdate(UpdateView):
    model = JobTitle
    success_url = reverse_lazy('jobapp:index')
    form_class = JobTitleForm
