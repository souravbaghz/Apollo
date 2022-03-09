from django.shortcuts import render

# Create your views here.
import os
from django.http import FileResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def GetExpFromServerToAgent(request):
    if request.method != "GET":
        return HttpResponse(status=403)
    else:
        filename = request.GET.get("filepname")
        filename = os.getcwd() + "/static/DownloadExploits/%s"%filename
        try:
            response = FileResponse(open(filename, 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
            return response
        except Exception as exception:
            print(exception)
            return HttpResponse(status=404)

