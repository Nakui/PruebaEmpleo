from inCharge.views import InChargeList, InChargeCreate, InChargeUpdate, InChargeDelete
from django.urls import path

app_name = 'inCharge'

urlpatterns = [
    path('', InChargeList.as_view(), name='inCharge_list'),
    path('create/', InChargeCreate.as_view(), name='inCharge_create'),
    path('update/<int:pk>', InChargeUpdate.as_view(), name='inCharge_update'),
    path('delete/<int:pk>', InChargeDelete.as_view(), name='inCharge_delete'),
]