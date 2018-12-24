from django.shortcuts import render, get_object_or_404, redirect
from .models import Computer, Order
from .forms import ComputerForm

from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class ComputerBaseMixin(object):
    model = Computer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(active=True)

    template_name = 'core/list.html'


class ComputerListView(LoginRequiredMixin, ComputerBaseMixin, ListView):
    paginate_by = 5


class ComputerDetailView(ComputerBaseMixin, DetailView):
    template_name = 'core/detail.html'


class CartView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'core/cart.html'

    def get(self, request, *args, **kwargs):
        if 'computer_id' in kwargs:
            return redirect(reverse('core:cart'))
        context = {'orders': Order.objects.filter(user=request.user)}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        p = Computer.objects.get(pk=request.POST['computer_id'])

        if Order.objects.filter(user=request.user, product=request.POST['computer_id']).count() == 0:
            order_obj = Order.objects.create(user=request.user, product=p, count=1)
            order_obj.save()
        else:
            order_obj = Order.objects.get(user=request.user, product=request.POST['computer_id'])
            order_obj.count += 1
            order_obj.save()
        return redirect(request.META['HTTP_REFERER'])


# CreateComputer
# EditComputer
# DeleteComputer

class CreateComputer(LoginRequiredMixin, CreateView):
    form_class = ComputerForm
    success_url = reverse_lazy('core:computer_list')
    template_name = 'core/create.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.slug = slugify(unidecode(form.instance.name))
            return super().form_valid(form)
        return redirect(reverse_lazy('account:login'))


class EditComputer(LoginRequiredMixin, UpdateView):
    model = Computer
    success_url = reverse_lazy('core:computer_list')
    template_name = 'core/edit.html'
    form_class = ComputerForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.slug = slugify(unidecode(form.instance.name))
            return super().form_valid(form)
        return redirect(reverse_lazy('account:login'))


class DeleteComputer(LoginRequiredMixin, DeleteView):
    model = Computer
    success_url = reverse_lazy('core:computer_list')

    # def get_object(self, queryset=None):
    #     obj = super().get_object()
    #     if not obj.customer == self.request.user:
    #         raise Http404
    #     return obj

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return self.post(request, *args, **kwargs)
        raise Http404


def delete_cart(request):
    c = Order.objects.filter(user=request.user)
    c.delete()
    return redirect('core:computer_list')
