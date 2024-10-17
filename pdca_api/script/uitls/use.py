from django.http import JsonResponse
from .decorators import jwt_required  # 假设装饰器在 decorators 模块中

@jwt_required
def my_view(request):
    # 现在可以访问 request.payload 中的 JWT 负载
    return JsonResponse({'message': 'Success', 'payload': request.payload})
