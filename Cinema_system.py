from abc import ABC, abstractmethod
# กำหนด Seat เป็น interface class
class Seat(ABC):
    # method Seat
    def __init__(self, number):
        self.__number = number
        self.__is_booked = False
        self.__name = None

    def get_number(self):
        return self.__number
    
    def book(self):
        self.__is_booked = True

    def cancel_booking(self):
        self.__is_booked = False
    
    def get_name(self):
        return self.__name
    
    # abstract method
    @abstractmethod
    def set_name(self , name):
        self.__name = name

    @abstractmethod
    def get_booked(self):
        return self.__is_booked



# inherit seat
class RegularSeat(Seat):
     # method RegularSeat
    def __init__(self, number ,price):
        super().__init__(number)
        self.__price = price  # Set price for regular seat

    def get_booked(self):
        return super().get_booked()
    
    def set_name(self, name):
        return super().set_name(name)
    
    def book(self):
        super().book()

# inherit seat
class VIPSeat(Seat):
     # method VIPSeat
    def __init__(self, number , price):
        super().__init__(number)
        self.__price = price  # Set price for VIP seat

    def get_booked(self):
        return super().get_booked()
    
    def set_name(self, name):
        return super().set_name(name)
    
    def book(self):
        super().book()
    


# class CinemaHall
class CinemaHall:
   #  method CinemaHall  
    def __init__(self ,seat_all):
        self.__seats = [None] * seat_all

    def get_seat(self):
        return self.__seats

    def add_seat(self , seat , seat_number):
        self.__seats[seat_number] = seat

    def get_number_seat(self , number):
         return self.__seats[number]

   

