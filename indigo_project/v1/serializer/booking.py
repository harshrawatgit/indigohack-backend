from rest_framework import serializers


class CreateBookingSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    source = serializers.CharField(max_length=255, allow_null=False,
                                   allow_blank=False, required=True)
    destination = serializers.CharField(max_length=255, allow_null=False,
                                        allow_blank=False, required=True)
    booking_on = serializers.DateTimeField(required=True)
    price = serializers.IntegerField(required=True)


class UpdateBookingSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField(required=True)
    source = serializers.CharField(max_length=255, allow_null=False,
                                   allow_blank=False, required=False)
    destination = serializers.CharField(max_length=255, allow_null=False,
                                        allow_blank=False, required=False)
    booking_on = serializers.DateTimeField(required=False)
    price = serializers.IntegerField(required=False)


class DeleteSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField(required=True)


class GetBookingSerializer(serializers.Serializer):
    
    def to_representation(self, booking_obj):
        data = {
            "booking_id": booking_obj.id,
            "created": booking_obj.created,
            "updated": booking_obj.updated,
            "booking_on": booking_obj. booking_on,
            "user_id": booking_obj.user_id,
            "source": booking_obj.source,
            "destination": booking_obj.destination,
            "price": booking_obj.price
        }
        return data