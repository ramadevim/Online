from django.db import models
from product.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Order {}'.format(self.id)

    class Meta:
        ordering = ['-timestamp', '-updated']

class OrderItem(models.Model):
        order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
        product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return '{}'.format(self.id)

        def get_cost(self):
            return self.price * self.quantity

    # def get_absolute_url(self):
    #     return reverse("orders:detail", kwargs={'order_id': self.order_id})
    #
    # def get_status(self):
    #     if self.status == "refunded":
    #         return "Refunded order"
    #     elif self.status == "shipped":
    #         return "Shipped"
    #     return "Shipping Soon"
    #
    # def update_total(self):
    #     cart_total = self.cart.total
    #     shipping_total = self.shipping_total
    #     new_total = math.fsum([cart_total, shipping_total])
    #     formatted_total = format(new_total, '.2f')
    #     self.total = formatted_total
    #     self.save()
    #     return new_total

#generate the order id
#generate the ordertotal