from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Avg
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import HoPs, Review
from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE
# Create your views here.

class ListHoPsView(LoginRequiredMixin, ListView):
    template_name = 'HoPsapp/index.html' # HoPsapp_listからindexに変更
    model = HoPs
    paginate_by = ITEM_PER_PAGE

class DetailHoPsView(LoginRequiredMixin, DetailView):
    template_name = 'HoPsapp/HoPsapp_detail.html'
    model = HoPs

class CreateHoPsView(LoginRequiredMixin, CreateView):
    template_name = 'HoPsapp/HoPsapp_create.html'
    model = HoPs
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-HoPsapp')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteHoPsView(LoginRequiredMixin, DeleteView):
    template_name = 'HoPsapp/HoPsapp_confirm_delete.html'
    model = HoPs
    success_url = reverse_lazy('list-HoPsapp')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdateHoPsView(LoginRequiredMixin, UpdateView):
    model = HoPs
    fields = ('title', 'text', 'category', 'thumbnail')
    template_name = 'HoPsapp/HoPsapp_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-HoPsapp', kwargs={'pk': self.object.id})

def index_view(request):
    object_list = HoPs.objects.order_by('-id') #左のとこ、HoPsapp_list？ object_list？
    ranking_list = HoPs.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    
    paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    return render(
        request, 
        'HoPsapp/index.html',
        {'object_list': object_list, 'ranking_list': ranking_list, 'page_obj':page_obj },
    )

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('HoPsapp', 'title', 'text', 'rate')
    template_name = 'HoPsapp/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['HoPsapp'] = HoPs.objects.get(pk=self.kwargs['HoPsapp_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-HoPsapp', kwargs={'pk': self.object.HoPsapp.id})