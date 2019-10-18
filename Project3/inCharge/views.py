from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inCharge.forms import InChargeForm
from inCharge.models import InCharge

# Create your views here.
class InChargeList(ListView):
    model = InCharge
    template_name = 'inCharge/inCharge_list.html'
    paginate_by = 3


class InChargeCreate(CreateView):
    model = InCharge
    form_class = InChargeForm
    template_name = 'inCharge/inCharge_form.html'
    success_url = reverse_lazy('inCharge:inCharge_list')

class InChargeUpdate(UpdateView):
    model = InCharge
    form_class = InChargeForm
    template_name = 'inCharge/inCharge_form.html'
    success_url = reverse_lazy('inCharge:inCharge_list')

class InChargeDelete(DeleteView):
    model = InCharge
    form_class = InChargeForm
    template_name = 'inCharge/inCharge_delete.html'
    success_url = reverse_lazy('inCharge:inCharge_list')