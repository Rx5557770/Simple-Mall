from rest_framework.views import exception_handler
from rest_framework.response import Response

from .settings import logger
def CustomExceptionHandler(exc, context):
    response = exception_handler(exc, context)

    # drf的错误
    if response:
        msg = {'data': response.data}
        logger.error(exc)
        return Response(msg, status=400)
    else:
        # Python错误
        logger.exception(exc)
        return Response({'msg': '系统出错'}, status=431)