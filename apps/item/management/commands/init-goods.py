from django.core.management import BaseCommand
from apps.item.models import Item, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = [
            {'name': 'app',},
            {'name': 'python'},
        ]
        data = [Category(**i) for i in categories]
        Category.objects.bulk_create(data)
        self.stdout.write('初始化分类成功')

        items = [
            {'name': 'test1', 'price': 0.01, 'return_url': 'http://qq.com/', 'category_id': 1, 'desc': '一段介绍....................'},
            {'name': 'test2', 'price': 0.02, 'return_url': 'http://baidu.com/', 'category_id': 2},
        ]
        data = [Item(**i) for i in items]
        Item.objects.bulk_create(data)
        self.stdout.write('初始化item成功')