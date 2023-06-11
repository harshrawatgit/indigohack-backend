from rest_framework.views import APIView
from v1.controller import booking
from rest_framework.response import Response
from rest_framework import status
from v1.controller.booking import CreateBooking, UpdateBooking, DeleteBooking,
                                  GetBookingHandler


class CreateBookingHandler(APIView):
    def post(self, request):
        
        booking_data = booking.CreateBooking(data=request.data).book()
        return Response(booking_data, status=status.HTTP_200_OK)


class UpdateBookingHandler(APIView):
    def post(self, request):
        booking_data = booking.UpdateBooking(data=request.data).book()
        return Response(booking_data, status=status.HTTP_200_OK)


class DeleteBookingHandler(APIView):
    def post(self, request):
        booking_data = booking.DeleteBooking(data=request.data).book()
        return Response(booking_data, status=status.HTTP_200_OK)


class GetBookingHandler(APIView):
    def get(self, request):
        booking_data = booking.GetBooking(data=request.data,
                                          params=request.query_params).book()
        return Response(booking_data, status=status.HTTP_200_OK)