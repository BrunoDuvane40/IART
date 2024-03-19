import random

import pandas as pd

class Package:
    def __init__(self, package_id, package_type, coordinates):
        self.id = package_id
        self.package_type = package_type
        self.coordinates_x = coordinates[0]
        self.coordinates_y = coordinates[1]

        if package_type == 'fragile':
            self.breaking_chance = random.uniform(0.0001, 0.01) # 0.01-1% chance of breaking per km

            self.breaking_cost = random.uniform(3, 10) # Extra cost in case of breaking

        elif package_type == 'urgent':
            self.delivery_time = random.uniform(100, 240) # Delivery time in minutes (100 minutes to 4 hours)

    def __str__(self):
        return f"ID, {self.id},  Type: {self.package_type}, Coordinates: ({self.coordinates_x}, {self.coordinates_y})"

def generate_package_stream(num_packages, map_size):
    package_types = ['fragile', 'normal', 'urgent']

    package_stream = [Package(0, 'start', (0, 0))]

    package_stream = package_stream + [Package(i, random.choice(package_types),(random.uniform(0, map_size), random.uniform(0, map_size))) for i in range(1,num_packages+1)]
    
    return package_stream


