import uuid
from App.utils.file_handler import read_data,write_data

TABLE_FILE="App/database/tables.json"
BOOKING_FILE="App/database/table_bookings.json"

class TableService:

    def reserve_table(self, customer_name):

        tables=read_data(TABLE_FILE)
        bookings=read_data(BOOKING_FILE)

        try:
            persons=int(input("Enter Number of Persons: "))
        except ValueError:
            print("Invalid Number!")
            return

        booking_date=input("Enter Booking Date (YYYY-MM-DD): ")
        booking_time=input("Enter Booking Time (HH:MM AM/PM): ")

        available_tables=[]

        for table in tables:

            if table["capacity"] >= persons:

                booked=False

                for booking in bookings:

                    if (
                        booking["table_no"]==table["table_no"]
                        and booking["booking_date"]==booking_date
                        and booking["booking_time"]==booking_time
                        and booking["status"] != "Cancelled"
                    ):
                        booked=True
                        break

                if not booked:
                    available_tables.append(table)

        if not available_tables:
            print("No Tables Available!")
            return

        print("\n===== AVAILABLE TABLES =====")

        for index, table in enumerate(available_tables, start=1):
            print(
                f"{index}. Table {table['table_no']} "
                f"({table['capacity']} Seats)"
            )

        try:
            choice=int(input("Select Table: "))
            selected_table=available_tables[choice - 1]

        except (ValueError, IndexError):
            print("Invalid Choice!")
            return

        booking={
            "booking_id": str(uuid.uuid4())[:8],
            "customer_name": customer_name,
            "table_no": selected_table["table_no"],
            "persons": persons,
            "booking_date": booking_date,
            "booking_time": booking_time,
            "status": "Reserved"
        }

        bookings.append(booking)

        write_data(BOOKING_FILE, bookings)

        print("\n===== BOOKING SUCCESSFUL =====")
        print(f"Booking ID : {booking['booking_id']}")
        print(f"Customer   : {booking['customer_name']}")
        print(f"Table No   : {booking['table_no']}")
        print(f"Status     : {booking['status']}")

    def view_my_bookings(self, customer_name):

        bookings=read_data(BOOKING_FILE)

        my_bookings=[
            booking
            for booking in bookings
            if booking["customer_name"]==customer_name
        ]

        if not my_bookings:
            print("No Bookings Found!")
            return

        print("\n===== MY BOOKINGS =====")

        for booking in my_bookings:

            print(f"\nBooking ID : {booking['booking_id']}")
            print(f"Customer   : {booking['customer_name']}")
            print(f"Table No   : {booking['table_no']}")
            print(f"Persons    : {booking['persons']}")
            print(f"Date       : {booking['booking_date']}")
            print(f"Time       : {booking['booking_time']}")
            print(f"Status     : {booking['status']}")

    def view_all_bookings(self):

        bookings=read_data(BOOKING_FILE)

        if not bookings:
            print("No Bookings Available!")
            return

        print("\n===== ALL BOOKINGS =====")

        for booking in bookings:

            print(
                f"{booking['booking_id']} | "
                f"{booking['customer_name']} | "
                f"Table {booking['table_no']} | "
                f"{booking['booking_date']} | "
                f"{booking['booking_time']} | "
                f"{booking['status']}"
            )

    def update_booking_status(self):

        booking_id=input("Enter Booking ID: ")

        bookings=read_data(BOOKING_FILE)

        for booking in bookings:

            if booking["booking_id"]==booking_id:

                print("\n1. Reserved")
                print("2. Occupied")
                print("3. Completed")
                print("4. Cancelled")

                choice=input("Select Status: ")

                status_map={
                    "1": "Reserved",
                    "2": "Occupied",
                    "3": "Completed",
                    "4": "Cancelled"
                }

                if choice in status_map:

                    booking["status"]=status_map[choice]

                    write_data(BOOKING_FILE, bookings)

                    print("Status Updated Successfully!")
                    return

                print("Invalid Status!")
                return

        print("Booking Not Found!")

    def cancel_booking(self, customer_name):

        booking_id=input("Enter Booking ID to Cancel: ")

        bookings=read_data(BOOKING_FILE)

        for booking in bookings:

            if (
                booking["booking_id"]==booking_id
                and booking["customer_name"]==customer_name
            ):

                if booking["status"]=="Cancelled":
                    print("Booking Already Cancelled!")
                    return

                booking["status"]="Cancelled"

                write_data(BOOKING_FILE, bookings)

                print("Booking Cancelled Successfully!")
                return

        print("Booking Not Found!")
        