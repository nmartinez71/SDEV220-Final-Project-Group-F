from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ManyToManyField(Category, related_name='food_items')  # Many-to-many relationship with Category
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # ForeignKey to link FoodItem
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date/time

    def __str__(self):
        return f'Order of {self.food_item.name} x {self.quantity} - Total: ${self.total_price} - Created at: {self.created_at}'



class OrderModel(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order for {self.customer_name}"
