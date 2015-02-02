from django.db import models


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    retail_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_level = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name


class Platform(TimeStampedModel):
    name = models.CharField(max_length=200)
    transaction_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    incude_shipping_in_transaction_cost = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ShippingLocation(TimeStampedModel):
    name = models.CharField(max_length=200)
    shipping_charge = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name + " - " + str(self.shipping_charge)


class SoldItem(TimeStampedModel):
    product = models.ForeignKey(Product)
    platform = models.ForeignKey(Platform)
    shipping_location = models.ForeignKey(ShippingLocation, null=True)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=7, decimal_places=2)
    sold_date = models.DateTimeField()

    def __str__(self):
        return self.product.name

    def profit(self):
        if(self.platform.incude_shipping_in_transaction_cost):
            transaction_cost = (self.sale_price + self.shipping_location.shipping_charge) * (self.platform.transaction_cost / 100)
        else:
            transaction_cost = (self.sale_price) * (self.platform.transaction_cost / 100)
        
        return "{0:.2f}".format(self.sale_price + self.shipping_location.shipping_charge - self.product.cost - self.shipping_cost - transaction_cost)


class Overhead(TimeStampedModel):

    BUSINESS = 'BU'
    PRODUCT = 'PR'

    OVERHEAD_TYPE_CHOICES = (
        (BUSINESS, 'Business'),
        (PRODUCT, 'Product'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    overhead_type = models.CharField(
        max_length=2,
        choices=OVERHEAD_TYPE_CHOICES,
        default=PRODUCT
    )
    date = models.DateTimeField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
