# Appointment Booking System
# Command line 
# This is a simple command-line appointment booking tool.
# You can add new patient appointments, view all saved entries,
# and search for a specific appointment by patient ID.
# All appointment records are kept in memory while the program runs.
import re
import random

appointments = []

def generate_patient_id():
    # Generate a random 4-digit patient ID and make sure it is unique.
    while True:
        new_id = str(random.randint(1000, 9999))
        # Check if the generated ID is already in use.
        found = False
        for appt in appointments:
            if appt[0] == new_id:
                found = True
                break
        if not found:
            return new_id


def validate_time(time_str):
    # Verify the entered time matches a simple format like 10am or 2pm.
    pattern = r"^\d{1,2}[ap]m$"
    if re.search(pattern, time_str.lower()):
        return True
    return False


def validate_patient_id(patient_id_str):
    # Confirm the patient ID contains only digits.
    pattern = r"^\d+$"
    if re.search(pattern, patient_id_str.strip()):
        return True
    return False


def get_age_group(age):
    # Label the patient based on age: Child, Adult, or Elder.
    if age >= 50:
        return "Elder"
    elif age >= 18:
        return "Adult"
    return "Child"


def add_appointment():
    print("\n--- Add Appointment ---")

    # Ask whether the system should generate a unique patient ID automatically.
    choice = input("Auto-generate ID? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
        patient_id = generate_patient_id()
        print(f"ID: {patient_id}")
    else:
        while True:
            patient_id = input("Enter Patient ID (numbers only): ").strip()
            if not validate_patient_id(patient_id):
                print("Invalid ID. Use numbers only.")
                continue
            # Make sure the ID is not already assigned to another patient.
            if any(appt[0] == patient_id for appt in appointments):
                print("ID already taken. Try another.")
                continue
            break

    name = input("Name: ").strip()
    while not name:
        print("Name required.")
        name = input("Name: ").strip()

    # Ask for the patient's age and confirm it is a positive number.
    while True:
        age_str = input("Age: ").strip()
        if not age_str.isdigit() or int(age_str) <= 0:
            print("Enter valid age.")
            continue
        age = int(age_str)
        break

    problem = input("Problem/Reason: ").strip()
    while not problem:
        print("Please enter reason for visit.")
        problem = input("Problem/Reason: ").strip()

    # Ask how urgent this appointment should be.
    while True:
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Use High, Medium, or Low.")

    # Ask for the appointment time and validate the input format.
    while True:
        appointment_time = input("Time (10am, 2pm, etc): ").strip()
        if not validate_time(appointment_time):
            print("Wrong format. Use like: 10am, 2pm")
            continue
        break

    age_group = get_age_group(age)
    appointment = [patient_id, name, age, age_group, problem, priority, appointment_time.lower()]
    appointments.append(appointment)
    print("Done!\n")


def show_appointments():
    print("\n--- All Appointments ---")
    if not appointments:
        print("No records yet.\n")
        return

    # Print a simple table of all saved appointments.
    print(f"{'ID':<8} {'Name':<12} {'Age':<6} {'Group':<8} {'Problem':<18} {'Priority':<10} {'Time':<8}")
    print("-" * 80)
    for appt in appointments:
        print(f"{appt[0]:<8} {appt[1]:<12} {appt[2]:<6} {appt[3]:<8} {appt[4]:<18} {appt[5]:<10} {appt[6]:<8}")


def search_appointment():
    print("\n--- Search ---")
    patient_id = input("Enter ID: ").strip()

    # Look for the appointment with the matching ID.
    for appt in appointments:
        if appt[0] == patient_id:
            print("\nFound:")
            print(f"ID: {appt[0]}")
            print(f"Name: {appt[1]}")
            print(f"Age: {appt[2]} ({appt[3]})")
            print(f"Problem: {appt[4]}")
            print(f"Priority: {appt[5]}")
            print(f"Time: {appt[6]}")
            print()
            return

    print("Not found.\n")


def main_menu():
    while True:
        print("\n" + "="*40)
        print("Appointment Booking")
        print("="*40)
        print("1. Add")
        print("2. View All")
        print("3. Search")
        print("4. Exit")
        print("="*40)

        choice = input("Choose(B/W 1,2,3,4 as per the list) :  ").strip()

        if choice == "1":
            add_appointment()
        elif choice == "2":
            show_appointments()
        elif choice == "3":
            search_appointment()
        elif choice == "4":
            print("Bye!\n")
            break
        else:
            print("Invalid choice.\n")
            continue

        cont = input("Continue? (yes/no): ").strip().lower()
        if cont not in ["yes", "y"]:
            print("Bye!\n")
            break
main_menu()

