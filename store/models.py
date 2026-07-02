from django.db import models
from PIL import Image
import uuid




# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, default='Nigeria')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=250,
        default='',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='uploads/product/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            if img.width > 300 or img.height > 300:
                output_size = (320, 240)
                img.thumbnail(output_size)
                img.save(self.image.path)


    
class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)
    
    @property
    def sub_total(self):
        return sum(item.sub_total for item in self.orderitem_set.all())

    @property
    def discount_amount(self):
        return (self.sub_total * self.discount) / 100

    @property
    def grand_total(self):
        return self.sub_total - self.discount_amount


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    @property
    def sub_total(self):
        return self.product.price * self.quantity
    
    def ___unicode_(self):
        return self.product.name

