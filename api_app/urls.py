from django.urls import path
from .views import CartItemViews, SendYourQueriesViews


urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('queries-items/', SendYourQueriesViews.as_view()),
    path('queries-items/<int:id>', SendYourQueriesViews.as_view()),
]
