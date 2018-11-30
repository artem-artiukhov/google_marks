from django.urls import path
from map.views import CoordinateList, CoordinatesForm

urlpatterns = [
    path('', CoordinateList.as_view(), name='map'),
    path('upload/', CoordinatesForm.as_view(), name='ip_form'),
]