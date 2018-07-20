from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import utils
from .forms import UploadReportForm
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UploadReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            utils.parse_xml_to_db(form.instance)
            return redirect('details',report_id=form.instance.id)
    else:
        form = UploadReportForm()
    return render(request, 'upload.html', {
        'form': form
    })

def report_details(request,report_id):
    if request.method == "GET":
        report_details = utils.get_report_details(report_id)
        summary = utils.get_summary(report_id)
        return render(request,'report.html',{"report_details" : report_details,"summary":summary})

def history(request):
    if request.method == "GET":
        history = utils.get_history()
        return render(request,'history.html',{"history" : history})
