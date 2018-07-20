from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/<int:report_id>',views.report_details, name='details')
]
