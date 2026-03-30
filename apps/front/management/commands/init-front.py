from django.core.management import BaseCommand
from apps.front.models import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        Home.objects.create(web_title='悟空资源库', content='我们提供精选的互联网资源，收集不易，还望收藏本站。PS:互联网产品仅供学习交流。')

        cards = [
            {'title': '极速发货', 'content': '下单后极速处理，确保您第一时间收到订单。'},
            {'title': '品质保证', 'content': '严格筛选供应商，每一件商品都经过严格的质量检测。'},
            {'title': '贴心客服', 'content': '7x24 小时在线客服，随时为您解答购物过程中的疑问。'},
        ]

        data = [Card(**i) for i in cards]
        Card.objects.bulk_create(data)
        self.stdout.write('初始化网站标题和卡片成功')