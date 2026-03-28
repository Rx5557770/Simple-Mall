import json
from django.http import JsonResponse

class CustomMiddleware:
    def __init__(self, get_response):
        # 一次性设置和初始化
        self.get_response = get_response

    def __call__(self, request):
        # 视图函数执行前的代码
        response = self.get_response(request)
        # 视图函数执行后的代码
        content_type = response.headers.get('Content-Type', '')

        # 1.判断是否是json类型的响应
        if content_type and 'application/json' in content_type:
            # 2.判断响应，并添加一些内容作为格式回复
            data = json.loads(response.content.decode('utf-8'))
            res_code = response.status_code

            if res_code < 400:
                data['code'] = 200 if res_code == 200 else res_code
                data['msg'] = 'success' if data.get('msg') is None else data.get('msg')
            else:
                data['code'] = res_code
                data['msg'] = 'error' if data.get('msg') is None else data.get('msg')
            # 统一返回 200
            return JsonResponse(data, status=200)
        return response