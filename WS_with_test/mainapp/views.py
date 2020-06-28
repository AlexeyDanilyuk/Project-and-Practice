from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mainapp.forms import ArmForm
from mainapp.models import Arm


class ArmList(ListView):
    model = Arm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Паспорта АРМ'
        return context


class ArmDelete(DeleteView):
    model = Arm
    success_url = reverse_lazy('mainapp:arm_list')


class ArmCreate(CreateView):
    model = Arm
    success_url = reverse_lazy('mainapp:arm_list')
    form_class = ArmForm


class ArmUpdate(UpdateView):
    model = Arm
    success_url = reverse_lazy('mainapp:arm_list')
    form_class = ArmForm
