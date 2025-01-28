from hotel import guests
from hotel import payments
from hotel import reservations
from hotel import rooms

import asyncio
from datetime import datetime

async def main():
    guest_manager = guests.GuestManager()
    reservations_manager = reservations.ReservationManager()
    rooms_manager = rooms.RoomManager()

    # Creamos un set de habitaciones 
    r1 = rooms.Room(100, 'Economy', 59.99,2)
    r2 = rooms.Room(101, 'Economy', 59.99,2)
    s1 = rooms.Room(200, 'Suite', 290.0, 4)
    s2 = rooms.Room(201, 'Suite', 300.0, 5, False)

    # Los agregamos al manager de la clase
    rooms_manager.add_room(r1)
    rooms_manager.add_room(r2)
    rooms_manager.add_room(s1)
    rooms_manager.add_room(s2)

    # Creamos un set de huéspedes
    h1 = guests.Guest("George", "Michaels", 3309, "george@michaels.com")
    h2 = guests.Guest("Martha", "Masters", 3310, "martha@masters.com")
    
    # Los agregamos al manager de la clase 
    guest_manager.add_guest(h1)
    guest_manager.add_guest(h2)

    # Simulamos un reserva
    if rooms_manager.check_availability(r1.number):
        res1 = reservations.Reservation(h1.name, r1.number, 3404, datetime.now(), datetime.now())
        reservations_manager.add_reservation(res1)

        await payments.process_payment(h1.name, r1.price)
    else:
        print(f"The room {r1.number} is not available!")

    if rooms_manager.check_availability(s2.number):
        res2 = reservations.Reservation(h2.name, s2.number, 3404, datetime.now(), datetime.now())
        reservations_manager.add_reservation(res2)

        await payments.process_payment(h2.name, s2.price)
    else:
        print(f"The room {s2.number} is not available!")


if __name__ == '__main__':
    asyncio.run(main())