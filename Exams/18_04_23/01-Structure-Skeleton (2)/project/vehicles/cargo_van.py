from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    XTRA_PERCENT = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduction_percent = round(mileage / self.MAX_MILEAGE * 100)
        self.battery_level -= (reduction_percent + self.XTRA_PERCENT)
