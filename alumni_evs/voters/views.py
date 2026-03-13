from django.shortcuts import render
from .csv_importer import import_voters

def upload_voters(request):

    if request.method == "POST":

        csv_file = request.FILES["file"]

        count = import_voters(csv_file)

        return render(request,"admin/upload_success.html",{"count":count})

    return render(request,"admin/upload_voters.html")