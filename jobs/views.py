from django.views.generic import ListView
from .models import Jobs

# Create your views here.


class JobsListView(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name='home.html'
    queryset = Jobs.objects.order_by('-upload_date')
