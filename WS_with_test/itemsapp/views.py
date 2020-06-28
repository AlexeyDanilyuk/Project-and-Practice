from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from itemsapp.forms import MonitorForm, SysBlockForm, PrinterForm, ScannerForm, UpsForm
from itemsapp.models import Monitor, Printer, SysBlock, Scanner, Ups
from mainapp.models import Arm


class SysBlockList(ListView):
    model = SysBlock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Системные блоки'
        return context


class SysBlockDelete(DeleteView):
    model = SysBlock
    success_url = reverse_lazy('itemsapp:sysblocks')


class SysBlockCreate(CreateView):
    model = SysBlock
    success_url = reverse_lazy('itemsapp:sysblocks')
    form_class = SysBlockForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        SysBlockFormSet = inlineformset_factory(SysBlock, Arm, form=SysBlockForm, extra=1)

        formset = None
        if self.request.method == 'POST':
            formset = SysBlockFormSet(self.request.POST, self.request.FILES)
        data['sysblockitem'] = formset

        return data


class SysBlockUpdate(UpdateView):
    model = SysBlock
    success_url = reverse_lazy('itemsapp:sysblocks')
    form_class = SysBlockForm


class MonitorList(ListView):
    model = Monitor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мониторы'
        return context


class MonitorDelete(DeleteView):
    model = Monitor
    success_url = reverse_lazy('itemsapp:monitors')


class MonitorCreate(CreateView):
    model = Monitor
    success_url = reverse_lazy('itemsapp:monitors')
    form_class = MonitorForm


class MonitorUpdate(UpdateView):
    model = Monitor
    success_url = reverse_lazy('itemsapp:monitors')
    form_class = MonitorForm


class PrinterList(ListView):
    model = Printer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Принтеры'
        return context


class PrinterDelete(DeleteView):
    model = Printer
    success_url = reverse_lazy('itemsapp:printers')


class PrinterCreate(CreateView):
    model = Printer
    success_url = reverse_lazy('itemsapp:printers')
    form_class = PrinterForm


class PrinterUpdate(UpdateView):
    model = Printer
    success_url = reverse_lazy('itemsapp:printers')
    form_class = PrinterForm


class ScannerList(ListView):
    model = Scanner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сканеры'
        return context


class ScannerDelete(DeleteView):
    model = Scanner
    success_url = reverse_lazy('itemsapp:scanners')


class ScannerCreate(CreateView):
    model = Scanner
    success_url = reverse_lazy('itemsapp:scanners')
    form_class = ScannerForm


class ScannerUpdate(UpdateView):
    model = Scanner
    success_url = reverse_lazy('itemsapp:scanners')
    form_class = ScannerForm


class UpsList(ListView):
    model = Ups

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ИБП'
        return context


class UpsDelete(DeleteView):
    model = Ups
    success_url = reverse_lazy('itemsapp:ups')


class UpsCreate(CreateView):
    model = Ups
    success_url = reverse_lazy('itemsapp:ups')
    form_class = UpsForm


class UpsUpdate(UpdateView):
    model = Ups
    success_url = reverse_lazy('itemsapp:ups')
    form_class = UpsForm
