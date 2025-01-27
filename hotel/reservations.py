# Reservas: Creación y cancelación de reservas de habitaciones.

from collections import defaultdict # gestionar las reservas
from datetime import datetime       # gestionar check_in y check_out en formato fecha

class Reservation:
    
    def __init__(self, guest_name, room_number:int, reservation_id: int, check_in, check_out):
        self.guest_name = guest_name
        self.room_number = room_number
        self.reservation_id = reservation_id
        self.check_in = check_in
        self.check_out = check_out
        self.reservation_id = reservation_id

class ReservationManager:
    """Allows to control and operate Reservation class"""

    def __init__(self):
        self.reservations = defaultdict(list)

    def add_reservation(self, reservation:Reservation):
        """Allows to add a reservation to the reservation collection"""
        self.reservations[reservation.room_number].append(reservation)
        print(f"Reservation for room {reservation.room_number} for {reservation.guest_name} created!")

    def cancel_reservation(self, reservation_id):
        """Allows to remove a reservtion from the list with a given reservation_id"""
        for reservations in self.reservations.items():
            for r in reservations[1]:
                if r.reservation_id == reservation_id:
                    print(f"Reservation #{reservation_id} cancelled!")
        
        print(f"We couldn't find a reservation #{reservation_id}, therefore couldn't be cancelled! Check your res# and try again") 

if __name__ == '__main__':
    # Testing module
    res1 = Reservation('George', 123, 33453, 'Monday', 'Friday')
    res2 = Reservation('Jennifer', 233, 44533, 'Saturday', 'Sunday')
    resManager = ReservationManager()

    resManager.add_reservation(res1)
    resManager.add_reservation(res2)

    resManager.cancel_reservation(33453)
        