from app.utils.file_handler import read_data
from app.utils.logger import write_log
import logging


class ViewAllStaffService:

    def __init__(self, user_file):
        self.user_file=user_file

    # Encapsulation: internal method
    def _load_users(self):
        try:
            return read_data(self.user_file)
        except Exception:
            logging.exception("Error loading users data")
            return []

    # Encapsulation: internal filtering logic
    def _get_staff_members(self, users):
        return [
            user for user in users
            if user.get("role", "").lower() == "staff"
        ]

    # Main public method (Abstraction)
    def view_all_staff(self):

        try:

            users=self._load_users()
            staff_members=self._get_staff_members(users)

            if not staff_members:
                print("\n❌ No Staff Members Found!")
                return

            print("\n" + "═" * 145)
            print("👨‍🍳 ALL STAFF MEMBERS 👨‍🍳".center(145))
            print("═" * 145)

            print(
                "╔════╦══════════╦══════════════╦════════════╦══════════════╦═══════════════════════╦═══════════════════╦══════════════╦════════════╦════════════╗"
            )
            print(
                "║ No ║ Staff ID ║ Name         ║ DOB        ║ Phone        ║ Email                 ║ Address           ║ Department   ║ Experience ║ Salary     ║"
            )
            print(
                "╠════╬══════════╬══════════════╬════════════╬══════════════╬═══════════════════════╬═══════════════════╬══════════════╬════════════╬════════════╣"
            )

            for index, staff in enumerate(staff_members, start=1):

                print(
                    f"║ {index:<2} "
                    f"║ {staff.get('user_id', 'N/A')[:8]:<8} "
                    f"║ {staff.get('username', 'N/A')[:12]:<12} "
                    f"║ {staff.get('dob', 'N/A'):<10} "
                    f"║ {staff.get('phone', 'N/A'):<12} "
                    f"║ {staff.get('email', 'N/A')[:21]:<21} "
                    f"║ {staff.get('address', 'N/A')[:17]:<17} "
                    f"║ {staff.get('department', 'N/A')[:12]:<12} "
                    f"║ {str(staff.get('experience', '0')):<10} "
                    f"║ {str(staff.get('salary', '0')):<10} ║"
                )

            print(
                "╚════╩══════════╩══════════════╩════════════╩══════════════╩═══════════════════════╩═══════════════════╩══════════════╩════════════╩════════════╝"
            )

            print(f"\n📊 Total Staff Members : {len(staff_members)}")

            write_log(f"Viewed All Staff | Total Staff: {len(staff_members)}")

        except Exception:
            logging.exception("Error while viewing all staff")
            print("❌ Something went wrong!")

        