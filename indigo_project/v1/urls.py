from django.urls import path
from v1.handler.booking import CreateBookingHandler, UpdateBookingHandler, DeleteBookingHandler, GetBookingHandler


 
urlpatterns = [
    #   path("user/add", .as_view(), name='create user'),
      path("booking/add", CreateBookingHandler.as_view(), name='create booking')
      path("booking/update", UpdateBookingHandler.as_view(), name='update booking')
      path("booking/remove", DeleteBookingHandler.as_view(), name='delete booking')
      path("booking/fetch", GetBookingHandler.as_view(), name='get booking')
]