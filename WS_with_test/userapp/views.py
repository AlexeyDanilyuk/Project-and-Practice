from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from userapp.forms import WorkUserForm
from userapp.models import WorkUser


class WorkUserList(ListView):
    model = WorkUser

    def get_queryset(self):
        return self.model.objects.all()


class WorkUserDelete(DeleteView):
    model = WorkUser
    success_url = reverse_lazy('userapp:index')


class WorkUserCreate(CreateView):
    model = WorkUser
    success_url = reverse_lazy('userapp:index')
    form_class = WorkUserForm


class WorkUserUpdate(UpdateView):
    model = WorkUser
    success_url = reverse_lazy('userapp:index')
    form_class = WorkUserForm
