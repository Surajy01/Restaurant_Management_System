import uuid
from App.utils.file_handler import read_data,write_data

TABLE_FILE="App/database/tables.json"
BOOKING_FILE="App/database/table_bookings.json"

class TableService:

    def reserve_table(self, customer_name):

        tables=read_data(TABLE_FILE)
        bookings=read_data(BOOKING_FILE)

        