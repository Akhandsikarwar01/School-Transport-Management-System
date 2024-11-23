import json

# Define the Student class
class Student:
    def __init__(self, student_id, name, grade, address):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.address = address

    def __repr__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Address: {self.address}"


# Define the Vehicle class
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, capacity):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.assigned_students = []

    def __repr__(self):
        return f"Vehicle ID: {self.vehicle_id}, Type: {self.vehicle_type}, Capacity: {self.capacity}"


# Define the Route class
class Route:
    def __init__(self, route_id, route_name, vehicle=None):
        self.route_id = route_id
        self.route_name = route_name
        self.vehicle = vehicle

    def __repr__(self):
        vehicle_info = f"Assigned Vehicle: {self.vehicle.vehicle_id}" if self.vehicle else "No vehicle assigned"
        return f"Route ID: {self.route_id}, Route: {self.route_name}, {vehicle_info}"

# Transport System Class
class TransportSystem:
    def __init__(self, filename="transport_data.json"):
        self.filename = filename
        self.students = []
        self.vehicles = []
        self.routes = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.students = [Student(**student) for student in data.get("students", [])]
                self.vehicles = [Vehicle(**vehicle) for vehicle in data.get("vehicles", [])]
                self.routes = [Route(**route) for route in data.get("routes", [])]
        except FileNotFoundError:
            pass  # If file does not exist, skip loading

    def save_data(self):
        data = {
            "students": [student.__dict__ for student in self.students],
            "vehicles": [vehicle.__dict__ for vehicle in self.vehicles],
            "routes": [route.__dict__ for route in self.routes]
        }
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add a student
    def add_student(self, student):
        self.students.append(student)

    # Add a vehicle
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Add a route
    def add_route(self, route):
        self.routes.append(route)

    # Search by student ID
    def search_student_by_id(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            print(student)
        else:
            print("Student not found.")

    # Search by vehicle ID
    def search_vehicle_by_id(self, vehicle_id):
        vehicle = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)
        if vehicle:
            print(vehicle)
        else:
            print("Vehicle not found.")

    # Search by route ID
    def search_route_by_id(self, route_id):
        route = next((r for r in self.routes if r.route_id == route_id), None)
        if route:
            print(route)
        else:
            print("Route not found.")
            
    # Assign student to vehicle
    def assign_student_to_vehicle(self, student_id, vehicle_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        vehicle = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)

        if student and vehicle:
            if len(vehicle.assigned_students) < vehicle.capacity:
                vehicle.assigned_students.append(student)
                print(f"Assigned {student.name} to vehicle {vehicle_id}.")
            else:
                print("Vehicle is at full capacity.")
        else:
            print("Invalid student or vehicle ID.")
    
    # Assign vehicle to route
    def assign_vehicle_to_route(self, vehicle_id, route_id):
        vehicle = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)
        route = next((r for r in self.routes if r.route_id == route_id), None)

        if vehicle and route:
            route.vehicle = vehicle
            print(f"Assigned vehicle {vehicle_id} to route {route_id}.")
        else:
            print("Invalid vehicle or route ID.")

# Display Menu
def display_menu():
    print("\n--- School Transport Management System ---")
    print("1. Add Student")
    print("2. Add Vehicle")
    print("3. Add Route")
    print("4. View Students")
    print("5. View Vehicles")
    print("6. View Routes")
    print("7. Assign Student to Vehicle")
    print("8. Assign Vehicle to Route")
    print("9. Search Student by ID")
    print("10. Search Vehicle by ID")
    print("11. Search Route by ID")
    print("12. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main function to run the program
def main():
    system = TransportSystem()

    while True:
        choice = display_menu()

        if choice == '1':  # Add Student
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grade = input("Enter Student Grade: ")
            address = input("Enter Student Address: ")
            student = Student(student_id, name, grade, address)
            system.add_student(student)
            print(f"Added student: {student}")

        elif choice == '2':  # Add Vehicle
            vehicle_id = input("Enter Vehicle ID: ")
            vehicle_type = input("Enter Vehicle Type (Bus/Van): ")
            capacity = int(input("Enter Vehicle Capacity: "))
            vehicle = Vehicle(vehicle_id, vehicle_type, capacity)
            system.add_vehicle(vehicle)
            print(f"Added vehicle: {vehicle}")

        elif choice == '3':  # Add Route
            route_id = input("Enter Route ID: ")
            route_name = input("Enter Route Name: ")
            route = Route(route_id, route_name)
            system.add_route(route)
            print(f"Added route: {route}")

        elif choice == '4':  # View Students
            print("\n--- All Students ---")
            for student in system.students:
                print(student)

        elif choice == '5':  # View Vehicles
            print("\n--- All Vehicles ---")
            for vehicle in system.vehicles:
                print(vehicle)

        elif choice == '6':  # View Routes
            print("\n--- All Routes ---")
            for route in system.routes:
                print(route)

        elif choice == '7':  # Assign Student to Vehicle
            student_id = input("Enter Student ID: ")
            vehicle_id = input("Enter Vehicle ID: ")
            system.assign_student_to_vehicle(student_id, vehicle_id)

        elif choice == '8':  # Assign Vehicle to Route
            vehicle_id = input("Enter Vehicle ID: ")
            route_id = input("Enter Route ID: ")
            system.assign_vehicle_to_route(vehicle_id, route_id)

        elif choice == '9':  # Search Student by ID
            student_id = input("Enter Student ID to search: ")
            system.search_student_by_id(student_id)

        elif choice == '10':  # Search Vehicle by ID
            vehicle_id = input("Enter Vehicle ID to search: ")
            system.search_vehicle_by_id(vehicle_id)

        elif choice == '11':  # Search Route by ID
            route_id = input("Enter Route ID to search: ")
            system.search_route_by_id(route_id)

        elif choice == '12':  # Exit
            print("Saving data and exiting...")
            system.save_data()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
