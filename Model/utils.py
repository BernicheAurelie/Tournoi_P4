from datetime import datetime


def is_date_valid(date_string): #self?
    format = "%d/%m/%Y"
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def register_end_time(self):
    self.end = datetime.now()
    print(f"fin : {self.end}")
