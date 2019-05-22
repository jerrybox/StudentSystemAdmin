import time
from django.shortcuts import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    """
    1. 编码过程中何时实用类何时适用对象
    2. 什么功能使用类方法实现，什么功能使用对象方法实现
    """

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        """
        *args: 什么用
        **kwargs: 什么用
        """

        if request.path != reverse('index'):
            return None

        start_time = time.time()
        response = func(request)
        end_time = time.time()
        costed = end_time - start_time
        print('Process view: {:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        """
        中间件在不同阶段处理方法前后，都是使用的同一个对象，否则self.start_time不能使用
        """
        costed = time.time() - self.start_time
        print('request to response cost: {:.2f}s'.format(costed))
        return response
