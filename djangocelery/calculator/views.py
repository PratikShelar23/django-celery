from django.http import JsonResponse
from .tasks import add, subtract
from celery.result import AsyncResult
from djangocelery import celery_app 

def calculate(request):
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    operation = request.GET.get('op', 'add')

    if operation == 'add':
        result = add.delay(num1, num2)
    else:
        result = subtract.delay(num1, num2)

    return JsonResponse({"task_id": result.id, "status": "Processing"})

def get_result(request):
    task_id = request.GET.get("task_id")
    result = AsyncResult(task_id, app=celery_app)

    return JsonResponse({
        "task_id": task_id,
        "status": result.status,
        "result": result.result
    })
