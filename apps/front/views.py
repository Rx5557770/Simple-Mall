from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Card
from apps.item.models import Purchase, Category
from apps.trade.models import Order


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Card.objects.all()
        return context


class ItemListView(TemplateView):
    template_name = 'home/item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_show=True)

        if self.request.user.is_authenticated:
            context['purchase'] = list(
                Purchase.objects.filter(user=self.request.user)
                .values_list('item_id', flat=True)
            )
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'home/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        return context