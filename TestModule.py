from Code import *
# Test script for hotel booking system
def test_guest_account_creation():
    guest1 = Guest(1, "Muhammad Ali", "ali@example.com", "1234567890")
    guest2 = Guest(2, "Ahmed", "Ahmed@example.com", "0987654321")

    print("Guest 1 Name:", guest1.get_name())
    print("Guest 1 Email:", guest1.get_email())
    print("Guest 1 Phone Number:", guest2.get_phone())
    print("Guest 2 Name:", guest1.get_name())
    print("Guest 2 Email:", guest1.get_email())
    print("Guest 2 Phone Number:", guest2.get_phone())
    print("*"*20)

def test_search_available_rooms():
    room1 = SingleRoom(101, 100)
    room2 = DoubleRoom(202, 200)

    # Checking initial availability
    print("Room 101 Available:", room1.check_availability())  # True
    print("Room 202 Available:", room2.check_availability())  # True

    # Simulating a reservation
    room1.set_availability(False)

    # Checking availability again
    print("Room 101 Available after booking:", room1.check_availability())  # False
    print("Room 202 Available:", room2.check_availability())  # Still True
    print("*"*20)


def test_make_reservation():
    guest = Guest(1, "Muhammad Ali", "ali@example.com", "1234567890")
    room = SingleRoom(101, 100)
    reservation = Reservation(guest, room, "2024-12-01", "2024-12-05")
    reservation.confirm_reservation()

    print("Reservation Confirmed:", reservation.is_confirmed)
    print("Room Availability After Booking:", room.check_availability())
    print("*"*20)

def test_booking_confirmation_notification():
    reservation = Reservation(Guest(1, "Muhammad Ali", "ali@example.com", "1234567890"),
                              SingleRoom(101, 100),
                              "2024-12-01", "2024-12-05")
    reservation.confirm_reservation()
    print("Booking Confirmation Sent?", "Yes" if reservation.is_confirmed else "No")
    print("*"*20)

def test_invoice_generation():
    guest = Guest(1, "Muhammad Ali", "ali@example.com", "1234567890")
    room = SingleRoom(101, 100)
    reservation = Reservation(guest, room, "2024-12-01", "2024-12-05")
    total = reservation.calculate_total_price()
    print("Total Invoice Amount:", total)
    print("*" * 20)

def test_payment_processing():
    reservation = Reservation(Guest(1, "Muhammad Ali", "ali@example.com", "1234567890"),
                              SingleRoom(101, 100),
                              "2024-12-01", "2024-12-05")
    payment = Payment(reservation, "Credit Card")
    payment.process_payment()
    print("Payment Successful:", payment.is_paid)
    print("*" * 20)

def test_display_reservation_history():
    guest = Guest(1, "Muhammad Ali", "ali@example.com", "1234567890")
    reservation = Reservation(guest,
                              SingleRoom(101, 100), "2024-12-01", "2024-12-05")
    guest.add_reservation_to_history(reservation)
    print("Number of Reservations:", len(guest.get_reservation_history()))
    print("*" * 20)

def test_cancel_reservation():
    guest = Guest(1, "Muhammad Ali", "ali@example.com", "1234567890")
    room = SingleRoom(101, 100)
    reservation = Reservation(guest, room, "2024-12-01", "2024-12-05")
    reservation.confirm_reservation()
    room.set_availability(True)  # Simulating cancellation
    print("Room Available After Cancellation:", room.check_availability())
    print("*" * 20)

test_guest_account_creation()
test_search_available_rooms()
test_make_reservation()
test_booking_confirmation_notification()
test_invoice_generation()
test_payment_processing()
test_display_reservation_history()
test_cancel_reservation()

