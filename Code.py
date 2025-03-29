# Base room class representing common room properties
from datetime import datetime
class Room:
    def __init__(self, room_number, room_type, price, amenities=None):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.amenities = amenities or []
        self.is_available = True
        self.current_reservation = None

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, room_number):
        self.room_number = room_number

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_amenities(self):
        return self.amenities

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def check_availability(self):
        return self.is_available

    def set_availability(self, status):
        self.is_available = status

    def get_current_reservation(self):
        return self.current_reservation

    def set_current_reservation(self, reservation):
        self.current_reservation = reservation


# Single Room with specific single room attributes
class SingleRoom(Room):
    def __init__(self, room_number, price, bed_count=1, bed_type="standard"):
        super().__init__(room_number, "Single", price)
        self.bed_count = bed_count
        self.bed_type = bed_type

    def get_bed_count(self):
        return self.bed_count

    def set_bed_count(self, bed_count):
        self.bed_count = bed_count

    def get_bed_type(self):
        return self.bed_type

    def set_bed_type(self, bed_type):
        self.bed_type = bed_type


# Double Room with specific double room attributes
class DoubleRoom(Room):
    def __init__(self, room_number, price, has_connecting_door=False, has_twin_beds=False):
        super().__init__(room_number, "Double", price)
        self.has_connecting_door = has_connecting_door
        self.has_twin_beds = has_twin_beds

    def check_connecting_door(self):
        return self.has_connecting_door

    def set_connecting_door(self, status):
        self.has_connecting_door = status

    def check_twin_beds(self):
        return self.has_twin_beds

    def set_twin_beds(self, status):
        self.has_twin_beds = status


# Suite Room with specific suite room attributes
class SuiteRoom(Room):
    def __init__(self, room_number, price, living_room_size=0, additional_amenities_count=0):
        super().__init__(room_number, "Suite", price)
        self.living_room_size = living_room_size
        self.additional_amenities_count = additional_amenities_count

    def get_living_room_size(self):
        return self.living_room_size

    def set_living_room_size(self, size):
        self.living_room_size = size

    def get_additional_amenities_count(self):
        return self.additional_amenities_count

    def set_additional_amenities_count(self, count):
        self.additional_amenities_count = count


# User class for managing user information
class User:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone


# Guest class with loyalty program features
class Guest(User):
    def __init__(self, id, name, email, phone, loyalty_status=""):
        super().__init__(id, name, email, phone)
        self.loyalty_points = 0
        self.loyalty_status = loyalty_status
        self.reservation_history = []

    def add_loyalty_points(self, points):
        self.loyalty_points += points

    def redeem_loyalty_points(self, points):
        if points <= self.loyalty_points:
            self.loyalty_points -= points
            return True
        return False

    def get_loyalty_points(self):
        return self.loyalty_points

    def get_loyalty_status(self):
        return self.loyalty_status

    def set_loyalty_status(self, status):
        self.loyalty_status = status

    def add_reservation_to_history(self, reservation):
        self.reservation_history.append(reservation)

    def get_reservation_history(self):
        return self.reservation_history


# Reservation class to manage booking details
class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = 0
        self.is_confirmed = False

    def get_guest(self):
        return self.guest
    def set_guest(self, guest):
        self.guest = guest
    def get_room(self):
        return self.room
    def set_room(self, room):
        self.room = room
    def get_check_in_date(self):
        return self.check_in_date
    def set_check_in_date(self, date):
        self.check_in_date = date
    def get_check_out_date(self):
        return self.check_out_date
    def set_check_out_date(self, date):
        self.check_out_date = date

    def calculate_total_price(self):
        date_format = "%Y-%m-%d"  # Adjust format if necessary
        try:
            check_in = datetime.strptime(self.check_in_date, date_format)
            check_out = datetime.strptime(self.check_out_date, date_format)

            if check_out <= check_in:
                return 0  # Ensure no negative or zero-night stays

            nights = (check_out - check_in).days
            self.total_price = self.room.get_price() * nights
            return self.total_price
        except ValueError:
            return 0  # Handle invalid date format

    def confirm_reservation(self):
        self.is_confirmed = True
        self.room.set_availability(False)
        self.guest.add_reservation_to_history(self)
        return self


# Payment class to handle transaction details
class Payment:
    def __init__(self, reservation, payment_method):
        self.reservation = reservation
        self.payment_method = payment_method
        self.amount = reservation.calculate_total_price()
        self.is_paid = False

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, method):
        self.payment_method = method
    def process_payment(self):
        self.is_paid = True
        return self.is_paid


# Service Request class for guest services
class ServiceRequest:
    def __init__(self, guest, request_type, details):
        self.guest = guest
        self.request_type = request_type
        self.details = details
        self.is_processed = False

    def get_guest(self):
        return self.guest

    def set_guest(self, guest):
        self.guest = guest

    def get_request_type(self):
        return self.request_type

    def set_request_type(self, request_type):
        self.request_type = request_type

    def get_details(self):
        return self.details

    def set_details(self, details):
        self.details = details

    def is_processed(self):
        return self.processed

    def mark_as_processed(self):
        self.is_processed = True
        return self.is_processed