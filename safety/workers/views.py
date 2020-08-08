import json

# from django.views import View
# from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import  viewsets

from .models import Worker
from .serializers import WorkerSerializer

# class-based view
# class WorkerListView(View):
#     def get(self, request):
#         workers = Worker.objects.all()
#         print(workers)
        # html = ''
        # for worker in workers:
        #     html += f'<li>{worker.first_name}</li>'
        # worker_list = []
        # for worker in workers:
        #     worker_list.append(worker.first_name)

        # return render(request, 'worker_list.html', {
        #     'workers' : workers
        # })

        # worker_list = []
        # for worker in workers:
        #     d = {
        #         'name' : worker.first_name,
                # 'lastname' : worker.last_name,
                # 'is_availble' : worker.is_availble,
                # 'primary_phone' : worker.primary_phone,
                # 'secondary_phone' : worker.secondary_phone,
                # 'address' : worker.address
            # }
        #     worker_list.append(d)
        # return HttpResponse(
        #     json.dumps(worker_list),
        #     content_type='application/json'
#         # )
# from rest_framework

class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

# class WorkerModelViewSetView(viewsets.ModelViewSet):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer