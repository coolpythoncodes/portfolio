from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Jobs


# Create your views here.


class JobsListView(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name='home.html'
    queryset = Jobs.objects.order_by('-upload_date')



class JobsDeleteView(LoginRequiredMixin, DeleteView):
    model = Jobs
    template_name = 'delete_job.html'
    success_url = reverse_lazy('home')
    login_urls = 'login'



class JobsCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['image']
    template_name = "new_job.html"
    success_url = reverse_lazy('home')
    login_urls = 'login'


class JobsUpdateView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['image']
    template_name = "change_job.html"
    success_url = reverse_lazy('home')
    login_urls = 'login'





