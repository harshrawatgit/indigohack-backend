from models import Booking


class CreateBooking:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    def book(self):
        data = {
            "user_id": self.data.get("user_id"),
            "source": self.data.get("source"),
            "destination": self.data.get("destination"),
            "booking_on": self.data.get("booking_on"),
            "price": self.data.get("price"),
        }
        obj = Booking.objects.create(**data)
        return {"booking_id": obj.id}


class UpdateBooking:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    def book(self):
        booking_id = self.data.get("booking_id")
        data = {
            "source": self.data.get("source"),
            "destination": self.data.get("destination"),
            "booking_on": self.data.get("booking_on"),
            "price": self.data.get("price"),
        }
        obj = Booking.objects.filter(id=booking_id).update(**data)
        return {"booking_id": obj.id}
        

class DeleteBooking:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    def book(self):
        booking_id = self.data.get("booking_id")
        data = {
            "active": 0
        }
        obj = Booking.objects.filter(id=booking_id).update(**data)
        return {"booking_id": obj.id}


class GetBooking:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    def book(self):
        obj_list = Booking.objects.all()
        serialized_data = ListBookingsSerializer(obj_list, many=True).data
        return {"booking_list": serialized_data}
        
