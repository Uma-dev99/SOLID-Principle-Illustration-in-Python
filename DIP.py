from abc import ABC, abstractmethod
import time

class IRide(ABC):
    @abstractmethod
    def request_ride(self, pickup: str, dropoff: str):
        pass

class IDriver(ABC):
    @abstractmethod
    def accept_ride(self, ride: IRide):
        pass

class IPayment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class Ride(IRide):
    def __init__(self, pickup: str, dropoff: str):
        self.pickup = pickup
        self.dropoff = dropoff
        self.driver = None
        self.is_completed = False

    def request_ride(self, pickup: str, dropoff: str):
        if not pickup or not dropoff:
            raise ValueError("Pickup and dropoff locations must be provided.")
        if pickup == dropoff:
            raise ValueError("Pickup and dropoff locations cannot be the same.")
        
        print(f"Ride requested from {pickup} to {dropoff}.")
        self.pickup = pickup
        self.dropoff = dropoff

    def assign_driver(self, driver: IDriver):
        self.driver = driver
        print(f"Driver {driver.name} assigned to the ride.")

    def complete_ride(self):
        if self.driver is None:
            raise ValueError("Cannot complete ride. No driver assigned.")
        if self.is_completed:
            raise ValueError("Ride has already been completed.")

        self.is_completed = True
        print(f"Ride completed from {self.pickup} to {self.dropoff}.")

class Driver(IDriver):
    def __init__(self, name: str):
        if not name:
            raise ValueError("Driver name must be provided.")
        self.name = name

    def accept_ride(self, ride: IRide):
        if ride.is_completed:
            raise ValueError("Cannot accept an already completed ride.")
        
        ride.assign_driver(self)
        print(f"Driver {self.name} accepted the ride.")

class Payment(IPayment):
    def process_payment(self, amount: float):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        
        print(f"Processing payment of Rs{amount:.2f} for the ride...")
        time.sleep(1)  # Simulate payment processing time
        print("Payment processed successfully.")

if __name__ == "__main__":
    # Create a ride
    ride = Ride(pickup="Location A", dropoff="Location B")

    # Create a driver
    driver = Driver(name="John Doe")

    try:
        # Request the ride
        ride.request_ride("Location A", "Location B")

        # Driver accepts the ride
        driver.accept_ride(ride)

        # Complete the ride
        ride.complete_ride()

        # Process payment
        payment = Payment()
        payment.process_payment(amount=15.00)
        
    except ValueError as e:
        print(f"Error: {e}")
