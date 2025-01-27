# Huéspedes: Almacenamiento y gestión de la información de los clientes.

class Guest:

    def __init__(self, name, last, guest_id, email):
        self.name = name
        self.last = last
        self.guest_id = guest_id
        self.email = email

class GuestManager:

    def __init__(self):
        self.guests = {}

    def add_guest(self, guest: Guest):
        """Adds a new guest to the guest DB"""
        self.guests[guest.guest_id] = guest


    def get_guest_by_id(self, guest_id):
        """Allows to get a customer from the customer list given a guest_id"""

        return self.guests.get(guest_id, "Guest not found! Check your guest ID")
    
if __name__ == '__main__':
    
    guest1 = Guest("Martha", "Masters", 3345, "martha@masters.com")

    guestManager = GuestManager()
    guestManager.add_guest(guest1)
    print(guestManager.guests)
    print(guestManager.get_guest_by_id(3345))