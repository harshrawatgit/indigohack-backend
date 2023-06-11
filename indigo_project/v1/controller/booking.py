import models

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
       

class DeleteBooking:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    def book(self):
        booking_id =self.data.get("booking_id")


class GetBooking:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    def book(self):

        
