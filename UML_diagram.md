CinemaHall
	- __seats: list
	+ get_seat(): list
	+ add_seat(seat, number)
	+ get_number_seat(number): Seat
 Seat
	- __number: int
	- __is_booked: bool
	- __name: str
	+ get_number(): int
	+ book()
	+ cancel_booking()
	+ get_name(): str
	+ set_name(name: str)
	+ get_booked(): bool
RegularSeat
	- __price: float
	+ get_booked(): bool
	+ set_name(name: str)
	+ book()
VIPSeat
	- __price: float
	+ get_booked(): bool
	+ set_name(name: str)
	+ book()
CinemaHall-->Seat
RegularSeat--Seat
VIPSeat--Seat
VIPSeat-->price
RegularSeat-->price