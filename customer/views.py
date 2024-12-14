from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import FoodItem, Order, Category

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class MenuView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'appetizers': [
                {"name": "Spring Rolls", "price": 5},
                {"name": "Garlic Bread", "price": 4}
            ],
            'main_courses': [
                {"name": "Spaghetti Bolognese", "price": 12},
                {"name": "Chicken Curry", "price": 10},
                {"name": "Filet mignon", "price": 22},
                {"name": "Special Cheeseburger", "price": 11}
            ],
            'desserts': [
                {"name": "Cheesecake", "price": 6},
                {"name": "Chocolate Cake", "price": 5},
                {"name": "Ice Cream", "price": 4}
            ],
            'drinks': [
                {"name": "Coffee", "price": 2},
                {"name": "Tea", "price": 2},
                {"name": "Soda", "price": 2}
            ]
        }
        return render(request, 'customer/menu.html', context)
    


class OrderNowView(View):
    def post(self, request, *args, **kwargs):
        # Handle form submission
        food_item_id = request.POST.get('food_item_id')
        quantity = request.POST.get('quantity')

        if food_item_id and quantity:
            food_item = FoodItem.objects.get(id=food_item_id)
            total_price = food_item.price * int(quantity)

            # Create a new order
            Order.objects.create(
                food_item=food_item,
                quantity=int(quantity),
                total_price=total_price
            )

            # Redirect after order creation
            return redirect('order_success')  # Update this as necessary

        # In case of an invalid form submission, you can redirect or return the same form with error messages
        return redirect('menu')  # Or show an error message

    def get(self, request, *args, **kwargs):
        # If the page is being accessed via GET (for initial form load)
        available_items = FoodItem.objects.all()
        return render(request, 'order_confirmation.html', {'available_items': available_items})
