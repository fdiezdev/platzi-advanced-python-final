# Gestiona la disponibilidad y características de las habitaciones.

class Room:
    """Unit of a hotel class"""

    def __init__(self, number: int, type, price: float, guests: int, available=True):
        self.number = number            # room number
        self.type = type                # basic / premium / suite
        self.price =price               # price per night in USD
        self.guests = guests            # number of people that fit in the room
        self.available = available      # availavility
    

    def check_number(self) -> int:
        """Returns the room number of a Room object"""
        return self.number
        
class RoomManager:
    """Allows to operate within a group of Rooms"""
    
    def __init__(self):
        self.rooms = {}

    def add_room(self, room: Room):
        """Adds a new room to the RoomManager room dictionary"""
        new_room = room.check_number()
        self.rooms[new_room] = room
        print(f"Room {new_room} added to list!")

    def check_availability(self, room_number:int) -> bool:
        """Checks wether the room can be booked"""
        room_to_check = self.rooms.get(room_number)
        availability = room_to_check.available

        if availability:
            print(f"Room {room_to_check.number} is available to reserve!")
            return True
        print(f"Room {room_to_check.number} is not available to reserve!")
        return False
        

if __name__ == '__main__':
    # Testing functionalities
    room123 = Room(123, 'basic', 66.99, 2)
    print(room123.check_number())

    manager = RoomManager()
    manager.add_room(room123)

    manager.check_availability(123)
