class Seat:
    def __init__(self, number):
        self.__number = number
        self.__is_booked = False
        self.__name = None

    def get_number(self):
        return self.__number

    def get_booked(self):
        return self.__is_booked

    def book(self):
        self.__is_booked = True

    def cancel_booking(self):
        self.__is_booked = False
    
    def get_name(self):
        return self.__name
    
    def set_name(self , name):
        self.__name = name


# inherit seat
class RegularSeat(Seat):
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
    def __init__(self ,seat_all):
        self.__seats = [None] * seat_all


    def book_seat(self, seat_number):
        seat = self.__seats[seat_number]
        if seat is not None and not seat.is_booked():
            seat.book()
            return True
        else:
            return False

    def get_seat(self):
        return self.__seats

    def add_seat(self , seat , seat_number):
        self.__seats[seat_number] = seat

    def get_number_seat(self , number):
         return self.__seats[number]

   



# # Example usage:
# num_seats = 10
# cinema = CinemaHall(num_seats)

# # Create some regular seats
# for i in range(5):
#     cinema._CinemaHall__seats[i] = RegularSeat(i + 1)

# # Create some VIP seats
# for i in range(5, 10):
#     cinema._CinemaHall__seats[i] = VIPSeat(i + 1)

# cinema.display_seating()

# # Book a regular seat
# cinema.book_seat(2)
# cinema.book_seat(7)

# # Book a VIP seat
# cinema.book_seat(9)

# cinema.display_seating()
