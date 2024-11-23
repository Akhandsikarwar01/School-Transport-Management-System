class Student:
    def __init__(self, student_id, name, grade, address):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.address = address
        self.assigned_vehicle = None

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}, Grade: {self.grade}, Address: {self.address})"


class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, capacity):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.assigned_students = []

    def assign_student(self, student):
        if len(self.assigned_students) < self.capacity:
            self.assigned_students.append(student)
            student.assigned_vehicle = self
        else:
            print("Vehicle is full!")

    def __str__(self):
        return f"Vehicle {self.vehicle_id} ({self.vehicle_type}, Capacity: {self.capacity})"


class Route:
    def __init__(self, route_id, start_point, end_point):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.vehicles = []

    def assign_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def __str__(self):
        return f"Route {self.route_id}: {self.start_point} to {self.end_point}"


class TransportSystem:
    def __init__(self):
        self.students = []
        self.vehicles = []
        self.routes = []

    def add_student(self, student):
        self.students.append(student)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_route(self, route):
        self.routes.append(route)

    def view_students(self):
        if not self.students:
            print("No students added yet.")
        for student in self.students:
            print(student)

    def view_vehicles(self):
        if not self.vehicles:
            print("No vehicles added yet.")
        for vehicle in self.vehicles:
            print(vehicle)

    def view_routes(self):
        if not self.routes:
            print("No routes added yet.")
        for route in self.routes:
            print(route)

    def assign_student_to_vehicle(self, student_id, vehicle_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        vehicle = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)

        if student and vehicle:
            vehicle.assign_student(student)
            print(f"Assigned {student.name} to vehicle {vehicle_id}.")
        else:
            print("Invalid student or vehicle ID.")

    def assign_vehicle_to_route(self, vehicle_id, route_id):
        vehicle = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)
        route = next((r for r in self.routes if r.route_id == route_id), None)

        if vehicle and route:
            route.assign_vehicle(vehicle)
            print(f"Assigned vehicle {vehicle_id} to route {route_id}.")
        else:
            print("Invalid vehicle or route ID.")


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
    print("9. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    system = TransportSystem()

    while True:
        choice = display_menu()

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grade = input("Enter Student Grade: ")
            address = input("Enter Student Address: ")
            student = Student(student_id, name, grade, address)
            system.add_student(student)
            print(f"Added student: {student.name}")

        elif choice == '2':
            vehicle_id = input("Enter Vehicle ID: ")
            vehicle_type = input("Enter Vehicle Type (e.g., Bus, Van): ")
            capacity = int(input("Enter Vehicle Capacity: "))
            vehicle = Vehicle(vehicle_id, vehicle_type, capacity)
            system.add_vehicle(vehicle)
            print(f"Added vehicle: {vehicle.vehicle_id}")

        elif choice == '3':
            route_id = input("Enter Route ID: ")
            start_point = input("Enter Route Start Point: ")
            end_point = input("Enter Route End Point: ")
            route = Route(route_id, start_point, end_point)
            system.add_route(route)
            print(f"Added route: {route.route_id}")

        elif choice == '4':
            system.view_students()

        elif choice == '5':
            system.view_vehicles()

        elif choice == '6':
            system.view_routes()

        elif choice == '7':
            student_id = input("Enter Student ID: ")
            vehicle_id = input("Enter Vehicle ID: ")
            system.assign_student_to_vehicle(student_id, vehicle_id)

        elif choice == '8':
            vehicle_id = input("Enter Vehicle ID: ")
            route_id = input("Enter Route ID: ")
            system.assign_vehicle_to_route(vehicle_id, route_id)

        elif choice == '9':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
