from app.utils.file_handler import read_data, write_data
from app.utils.logger import write_log
import logging


class StaffSalaryService:

    def __init__(self, user_file):
        self.user_file=user_file

    # Encapsulation
    def _load_users(self):
        return read_data(self.user_file)

    # Encapsulation
    def _save_users(self, users):
        write_data(self.user_file, users)

    # Encapsulation
    def _get_staff(self, users):
        return [
            user for user in users
            if user.get("role", "").lower()=="staff"
        ]

    # Abstraction
    def assign_or_update_salary(self):

        try:

            users=self._load_users()
            staff_members=self._get_staff(users)

            if not staff_members:
                print("❌ No Staff Found!")
                return

            print("\n" + "═" * 70)
            print("💰 ASSIGN STAFF SALARY 💰".center(70))
            print("═" * 70)

            for index, staff in enumerate(staff_members, start=1):

                print(
                    f"{index}. ID: {staff['user_id']} | "
                    f"{staff['username']} | "
                    f"{staff.get('department', 'N/A')} | "
                    f"Current Salary: ₹{staff.get('salary', 0)}"
                )

            # choice=int(input("\nSelect Staff Number: "))
            # selected_staff=staff_members[choice - 1]
            print("\nSelect Method:")
            print("1. Staff Number")
            print("2. Staff ID")
            print("3. Exit")

            method=input("Enter choice: ")

            if method=="3":
                print("❌ Exiting without changes!")
                return

            selected_staff=None

            # Staff Number
            if method=="1":
                try:
                    choice=int(input("Enter Staff Number: "))

                    if choice < 1 or choice > len(staff_members):
                        print("❌ Invalid Staff Number!")
                        return

                    selected_staff=staff_members[choice - 1]

                except ValueError:
                    print("❌ Invalid input!")
                    return

            # Staff ID
            elif method=="2":
                staff_id=input("Enter Staff ID: ").strip()

                for staff in staff_members:
                    if staff.get("user_id")==staff_id:
                        selected_staff=staff
                        break

                if not selected_staff:
                    print("❌ Staff ID not found!")
                    return

            else:
                print("❌ Invalid Choice!")
                return

            salary=float(input("Enter Monthly Salary: ₹"))

            if salary <= 0:
                print("❌ Salary must be greater than 0!")
                return

            selected_staff["salary"]=salary

            self._save_users(users)

            write_log(
                f"Salary Assigned | "
                f"Staff: {selected_staff['username']} | "
                f"Salary: {salary}"
            )

            print("\n✅ Salary Assigned Successfully!")
            print(f"👤 Staff : {selected_staff['username']}")
            print(f"💰 Salary: ₹{salary}")

        except (ValueError, IndexError):
            logging.error("Invalid staff selection during salary assignment")
            print("❌ Invalid Selection!")

        except Exception:
            logging.exception("Error assigning salary")
            print("❌ Something went wrong!")

    # Abstraction
    # def view_staff_salaries(self):

    #     try:

    #         users=self._load_users()
    #         staff_members=self._get_staff(users)

    #         if not staff_members:
    #             print("❌ No Staff Found!")
    #             return

    #         print("\n" + "═" * 90)
    #         print("💰 STAFF SALARY REPORT 💰".center(90))
    #         print("═" * 90)

    #         print("╔════╦══════════════╦══════════════╦════════════╗")
    #         print("║ No ║ Name         ║ Department   ║ Salary     ║")
    #         print("╠════╬══════════════╬══════════════╬════════════╣")

    #         for index, staff in enumerate(staff_members, start=1):

    #             print(
    #                 f"║ {index:<2} "
    #                 f"║ {staff['username']:<12} "
    #                 f"║ {staff.get('department', 'N/A'):<12} "
    #                 f"║ ₹{staff.get('salary', 0):<10,.2f} ║"
    #             )

    #         print("╚════╩══════════════╩══════════════╩════════════╝")

    #     except Exception:
    #         logging.exception("Error viewing staff salaries")
    #         print("❌ Something went wrong!")



