from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, get_object_or_404
from django.views import View
from django.utils import timezone

from apps.trade.models import Item, Order
from apps.item.models import Purchase

from utils.Pay import VPay, generate_out_trade_no

vpay = VPay()

class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)

        if Purchase.objects.filter(user=request.user, item=item).exists():
            return JsonResponse({
                'code': 400,
                'msg': '该商品已购买，无法重复购买'
            })

        # 随机生成订单
        trade_id = generate_out_trade_no()

        data = {
            'trade_id': trade_id,
            'amount': item.price,
            'payment': Order.Payment.alipay,
            'item': item,
            'user': request.user,
        }
        order = Order.objects.create(**data)

        try:
            # 获取云订单
            order_id = vpay.generate_orderId(payId=trade_id, type=2, price=item.price)
            order.order_id = order_id
            order.save()
            # 返回支付url
            pay_url = vpay.get_payUrl(orderId=order_id)
            return redirect(pay_url)
        except Exception as e:
            return HttpResponse('订单创建失败')


class PayBackView(View):
    def get(self, request):
        sign = request.GET.get('sign')
        params = {
            'payId': request.GET.get('payId'),
            'param': request.GET.get('param'),
            'type': request.GET.get('type'),
            'price': request.GET.get('price'),
            'reallyPrice': request.GET.get('reallyPrice'),
        }
        verify = vpay.sign_verify(params, sign)
        if not verify:
            return HttpResponse('请求不合法', status=400)
        # 获取订单信息
        try:
            order = Order.objects.get(trade_id=params.get('payId'))
            # 如果已经是购买成功状态则不做改变
            if order.status != Order.Status.success:
                order.status = Order.Status.success
                order.pay_time = timezone.now()
                order.save()
            # 设置关联，防止一个用户多次购买同一产品
            Purchase.objects.get_or_create(user=order.user, item=order.item)

        except Exception as e:
            print(e)
            return HttpResponse('回调失败')
        return redirect('home:profile')