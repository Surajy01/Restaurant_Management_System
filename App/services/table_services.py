import uuid
from app.utils.file_handler import read_data,write_data
from app.utils.logger import write_log
import logging

TABLE_FILE="app/database/tables.json"
BOOKING_FILE="app/database/table_bookings.json"

class TableService:

    def reserve_table(self, customer_name):

        try:

            tables=read_data(TABLE_FILE)
            bookings=read_data(BOOKING_FILE)

            try:
                persons=int(input("Enter Number of Persons: "))
            except ValueError:
                logging.error(f"Table Booking Failed | Customer: {customer_name} | Invalid Person Count")
                
                print("Invalid Number!")
                return

            booking_date=input("Enter Booking Date (DD-MM-YYYY): ")
            booking_time=input("Enter Booking Time (HH:MM AM/PM): ")

            available_tables=[]

            for table in tables:

                if table["capacity"] >= persons:

                    booked=False

                    for booking in bookings:

                        ACTIVE_BOOKINGS=["Reserved", "Occupied"]

                        if (
                            booking["table_no"]==table["table_no"]
                            and booking["booking_date"]==booking_date
                            and booking["booking_time"]==booking_time
                            and booking["booking_status"] in ACTIVE_BOOKINGS
                        ):
                            booked=True
                            break

                    if not booked:
                        available_tables.append(table)

            if not available_tables:
                logging.error(
                    f"Table Booking Failed | "
                    f"Customer: {customer_name} | "
                    f"Date: {booking_date} | "
                    f"Time: {booking_time} | "
                    f"No Tables Available"
                )

                print("❌ No Tables Available!")
                return

            print("\n" + "═" * 60)
            print("🪑 AVAILABLE TABLES 🪑".center(60))
            print("═" * 60)

            print("┌────┬──────────────┬──────────────┐")
            print("│ No │ Table Number │ Capacity     │")
            print("├────┼──────────────┼──────────────┤")

            for index, table in enumerate(available_tables, start=1):

                print(
                    f"│ {index:<2} "
                    f"│ T{table['table_no']:<11} "
                    f"│ {table['capacity']} Seats      │"
                )

            print("└────┴──────────────┴──────────────┘")

            try:
                choice=int(input("Select Table: "))
                selected_table=available_tables[choice - 1]

            except (ValueError, IndexError):
                logging.error(
                    f"Table Booking Failed | "
                    f"Customer: {customer_name} | "
                    f"Invalid Table Selection"
                )

                print("❌ Invalid Choice!")
                return

            booking={
                "booking_id": str(uuid.uuid4())[:8],
                "customer_name": customer_name,
                "table_no": selected_table["table_no"],
                "persons": persons,
                "booking_date": booking_date,
                "booking_time": booking_time,
                "booking_status": "Reserved"
            }

            bookings.append(booking)

            write_data(BOOKING_FILE, bookings)
            write_log(
                f"Table Reserved Successfully | "
                f"Booking ID: {booking['booking_id']} | "
                f"Customer: {customer_name} | "
                f"Table No: {selected_table['table_no']} | "
                f"Persons: {persons} | "
                f"Date: {booking_date} | "
                f"Time: {booking_time}"
            )

            print("\n" + "═" * 60)
            print("🪑 BOOKING SUCCESSFUL 🪑".center(60))
            print("═" * 60)

            print(f"🆔 Booking ID : {booking['booking_id']}")
            print(f"👤 Customer   : {booking['customer_name']}")
            print(f"🪑 Table No   : {booking['table_no']}")
            print(f"📅 Date       : {booking['booking_date']}")
            print(f"⏰ Time       : {booking['booking_time']}")
            print(f"📦 Status     : {booking['booking_status']}")

            print("═" * 60)
            print("🙏 Thank you for choosing our restaurant!".center(60))
            print("═" * 60)

        except Exception:

            logging.exception(
                f"Unexpected Error While Reserving Table | "
                f"Customer: {customer_name}"
            )

            print("❌ Something went wrong while booking the table!")



    def view_my_bookings(self, customer_name):

        try:

            bookings=read_data(BOOKING_FILE)

            my_bookings=[
                booking
                for booking in bookings
                if booking["customer_name"]==customer_name
            ]
            write_log(f"Viewed Booking History | Customer: {customer_name}")

            if not my_bookings:
                logging.error(f"No Bookings Found | Customer: {customer_name}")
                print("❌ No Bookings Found!")
                return

            print("\n" + "═" * 70)
            print("🪑 MY BOOKINGS 🪑".center(70))
            print("═" * 70)

            for booking in my_bookings:

                print("\n" + "┌" + "─" * 62 + "┐")
                print(f"│ 🆔 Booking ID : {booking['booking_id']:<46}│")
                print(f"│ 👤 Customer   : {booking['customer_name']:<46}│")
                print(f"│ 🪑 Table No   : {booking['table_no']:<46}│")
                print(f"│ 👥 Persons    : {booking['persons']:<46}│")
                print(f"│ 📅 Date       : {booking['booking_date']:<46}│")
                print(f"│ ⏰ Time       : {booking['booking_time']:<46}│")
                print(f"│ 📦 Status     : {booking['booking_status']:<46}│")
                print("└" + "─" * 62 + "┘")

        except Exception:

            logging.exception(
                f"Unexpected Error While Viewing Bookings | "
                f"Customer: {customer_name}"
            )

            print("❌ Something went wrong!")


    def view_all_bookings(self):

        try:

            bookings=read_data(BOOKING_FILE)

            if not bookings:

                logging.error("View All Bookings | No bookings found")

                print("\n❌ No Bookings Available!")
                return

            write_log("Admin/Staff Viewed All Bookings")

            print("\n" + "═" * 80)
            print("🪑 ALL TABLE BOOKINGS 🪑".center(80))
            print("═" * 80)

            print(
                f"{'ID':<10} "
                f"{'Customer':<15} "
                f"{'Table':<8} "
                f"{'Persons':<8} "
                f"{'Date':<12} "
                f"{'Time':<10} "
                f"{'Status':<12}"
            )

            print("─" * 80)

            for booking in bookings:

                print(
                    f"{booking['booking_id']:<10} "
                    f"{booking['customer_name']:<15} "
                    f"{'T' + str(booking['table_no']):<8} "
                    f"{booking.get('persons', '-'): <8} "
                    f"{booking['booking_date']:<12} "
                    f"{booking['booking_time']:<10} "
                    f"{booking['booking_status']:<12}"
                )

            print("═" * 80)

        except Exception:

            logging.exception("Unexpected Error While Viewing All Bookings")
            print("❌ Something went wrong!")



    def update_booking_status(self):

        try:

            booking_id=input("\n🔎 Enter Booking ID: ").strip()

            bookings=read_data(BOOKING_FILE)

            print("\n" + "═" * 50)
            print("🔄 UPDATE BOOKING STATUS 🔄".center(50))
            print("═" * 50)

            for booking in bookings:

                if booking["booking_id"]==booking_id:

                    print("\n📌 Current Status:", booking["booking_status"])
                    print("\nChoose New Status:")
                    print("╔════════════════════╗")
                    print("║ 1. 🟡 Reserved     ║")
                    print("║ 2. 🪑 Occupied     ║")
                    print("║ 3. ✅ Completed    ║")
                    print("║ 4. ❌ Cancelled    ║")
                    print("╚════════════════════╝")

                    choice=input("\n👉 Select Status: ").strip()

                    status_map={
                        "1": "Reserved",
                        "2": "Occupied",
                        "3": "Completed",
                        "4": "Cancelled"
                    }

                    if choice in status_map:

                        old_status=booking["booking_status"]
                        new_status=status_map[choice]

                        booking["booking_status"]=new_status

                        write_data(BOOKING_FILE, bookings)

                        write_log(
                            f"Booking Status Updated | "
                            f"Booking ID: {booking_id} | "
                            f"Old: {old_status} → New: {new_status}"
                        )

                        print("\n" + "═" * 50)
                        print("✅ STATUS UPDATED SUCCESSFULLY".center(50))
                        print("═" * 50)
                        print(f"🆔 Booking ID : {booking_id}")
                        print(f"📌 Status     : {new_status}")
                        print("═" * 50)

                        return

                    logging.error(f"Invalid Booking Status Selection | Booking ID: {booking_id}")

                    print("❌ Invalid Status Choice!")
                    return

            logging.error(f"Booking Not Found | Booking ID: {booking_id}")

            print("❌ Booking Not Found!")

        except Exception:

            logging.exception(f"Unexpected Error While Updating Booking Status | Booking ID: {booking_id}")
            print("❌ Something went wrong!")


    def cancel_booking(self, customer_name):

        try:

            print("\n" + "═" * 55)
            print("❌ CANCEL BOOKING ❌".center(55))
            print("═" * 55)

            booking_id=input("🔎 Enter Booking ID to Cancel: ").strip()

            bookings=read_data(BOOKING_FILE)

            for booking in bookings:

                if (
                    booking["booking_id"]==booking_id
                    and booking["customer_name"]==customer_name
                ):

                    if booking["booking_status"]=="Cancelled":

                        logging.error(
                            f"Cancel Booking Failed | Already Cancelled | "
                            f"Booking ID: {booking_id} | Customer: {customer_name}"
                        )

                        print("\n❌ Booking is already cancelled!")
                        return

                    old_status=booking["booking_status"]
                    booking["booking_status"]="Cancelled"

                    write_data(BOOKING_FILE, bookings)

                    write_log(
                        f"Booking Cancelled Successfully | "
                        f"Booking ID: {booking_id} | "
                        f"Customer: {customer_name} | "
                        f"Old Status: {old_status} → Cancelled"
                    )

                    print("\n" + "═" * 55)
                    print("✅ BOOKING CANCELLED SUCCESSFULLY".center(55))
                    print("═" * 55)
                    print(f"🆔 Booking ID : {booking_id}")
                    print(f"👤 Customer   : {customer_name}")
                    print(f"📦 Status     : Cancelled")
                    print("═" * 55)

                    return

            logging.error(
                f"Cancel Booking Failed | Not Found | "
                f"Booking ID: {booking_id} | Customer: {customer_name}"
            )

            print("\n❌ Booking Not Found!")

        except Exception:

            logging.exception(f"Unexpected Error While Cancelling Booking | Customer: {customer_name}")

            print("❌ Something went wrong!")
        