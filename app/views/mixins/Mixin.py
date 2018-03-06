from django.views.generic.base import ContextMixin


class FocusMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        return super(FocusMixin, self).get_context_data(**kwargs)