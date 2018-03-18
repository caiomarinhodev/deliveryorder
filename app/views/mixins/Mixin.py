from django.views.generic.base import ContextMixin

from app.models import Pedido


class FocusMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        return super(FocusMixin, self).get_context_data(**kwargs)


class LojaFocusMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        try:
            if 'pedido' in self.request.session:
                print(self.request.session['pedido'])
                kwargs['pedido_obj'] = Pedido.objects.get(id=self.request.session['pedido'])
        except (Exception,):
            pass
        return super(LojaFocusMixin, self).get_context_data(**kwargs)
