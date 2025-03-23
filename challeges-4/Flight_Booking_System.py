""" Simulate booking seats on a flight, handling passenger info and seat availablity """

class Passenger :
    def __init__(self,name,passport_number):
        self.name = name
        self.passport_number = passport_number
    

class Flight :
    def __init__(self,flight_number,seats):
        self.flight_number = flight_number
        self.booked_passengers = {}
        self.seats  = seats
        self.next_seat = 1

    def book_seat(self,passenger):
        if passenger.passport_number in  self.booked_passengers:
            return f"Passenger :{passenger.name} is already booked"
        else:
            if len(self.booked_passengers) >=self.seats:
                return f"not seat availble "
        
        self.booked_passengers[passenger.passport_number] =(passenger,self.seats)
        
        message = f"{passenger.name} is booked with seat: {self.next_seat}"
        self.next_seat +=1
        return message
    def cancel_booking(self,passport_number):
        if passport_number in self.booked_passengers:
            passenger = self.booked_passengers[passport_number][0]
            del self.booked_passengers[passport_number]
            return f"the booking cancelled for :{passenger.name} "
        return f"No booking found with that passport :{passport_number}"
    def view_manifest(self):
        if not self.booked_passengers:
            return f"not booking is made yet."
        return [f"{p.name} seats : {s}" for p,s in self.booked_passengers.values()]
            


# Test it
flight = Flight("AB123", 2)
p1 = Passenger("Ali", "P001")
p2 = Passenger("Lina", "P002")
p3 = Passenger("John", "P003")

print(flight.view_manifest())

print(flight.book_seat(p1))  # ✅
print(flight.book_seat(p2))  # ✅
print(flight.book_seat(p1))  # ❌ Duplicate
print(flight.book_seat(p3)) 

print(flight.cancel_booking("P001"))


print(flight.view_manifest())
    