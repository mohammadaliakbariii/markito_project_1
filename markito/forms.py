from .models import Products
from bootstrap_modal_forms.forms import BSModalModelForm

class ProductsModelForm(BSModalModelForm):
    class Meta:
        model = Products
        fields = ['image','store__name','name','category', 'count','buy_price','sell_price','side_costs','is_active']