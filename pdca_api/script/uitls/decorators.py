from functools import wraps
from django.http import JsonResponse
from .utils import AppTokenService, InvalidJWTPayload, InvalidJWTSign  # 假设你的 JWTUtil 和异常在 utils 模块中


def jwt_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)

        token = auth_header[len('Bearer '):]
        try:
            payload = AppTokenService.get_payload(token)
            request.payload = payload  # 将解码后的负载存储到请求对象中
        except InvalidJWTSign as e:
            return JsonResponse({'error': str(e)}, status=401)
        except InvalidJWTPayload:
            return JsonResponse({'error': 'Invalid JWT payload'}, status=400)

        return func(request, *args, **kwargs)

    return wrapper
