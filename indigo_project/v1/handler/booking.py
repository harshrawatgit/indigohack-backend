from rest_framework.views import APIView
from v1.controller import booking
from rest_framework.response import Response
from rest_framework import status
from v1.controller.booking import CreateBooking, UpdateBooking, DeleteBooking,
                                  GetBookingHandler


class CreateBookingHandler(APIView):
    def post(self, request):
        validator = BookFlightSerializer(data=request.data)
        success = validator.is_valid(raise_exception=True)
        validated_data = validator.validated_data
        booking_data = booking.CreateBooking(data=validated_data).book()
        return Response(booking_data, status=status.HTTP_200_OK)


class UpdateBookingHandler(APIView):
    def post(self, request):
        validator = BookFlightSerializer(data=request.data)
        success = validator.is_valid(raise_exception=True)
        validated_data = validator.validated_data
        booking_data = booking.UpdateBooking(data=validated_data).book()
        return Response(booking_data, status=status.HTTP_200_OK)


class DeleteBookingHandler(APIView):
    def post(self, request):
        validator = BookFlightSerializer(data=request.data)
        success = validator.is_valid(raise_exception=True)
        validated_data = validator.validated_data
        booking_data = booking.DeleteBooking(data=validated_data).book()
        return Response(booking_data, status=status.HTTP_200_OK)


class GetBookingHandler(APIView):
    def get(self, request):
        booking_data = booking.GetBooking(data=request.data,
                                          params=request.query_params).book()
        
        return Response(booking_data, status=status.HTTP_200_OK)
