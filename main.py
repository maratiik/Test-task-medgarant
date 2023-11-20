from datetime import datetime, timedelta

class Timetable:
    def __init__(self, day_start='09:00', day_end='21:00'):
        self.busy_time = []
        self.free_time = []
        self.free_slots = []
        self.day_start = day_start
        self.day_end = day_end

    def set_busy_time(self, busy_time):
        self.busy_time = [
            (datetime.strptime(slot['start'], '%H:%M'), datetime.strptime(slot['stop'], '%H:%M')) for slot in busy_time
            ]
        self.busy_time.sort()


    def find_free_time(self):
        last_stop = datetime.strptime(self.day_start, '%H:%M')
        for start, end in self.busy_time:
            if start > last_stop:
                self.free_time.append((last_stop, start))
            last_stop = max(last_stop, end)
        self.free_time.append((last_stop, datetime.strptime(self.day_end, '%H:%M')))


    def find_slots(self, slot_length=30):
        delta = timedelta(minutes=slot_length)

        for start, end in self.free_time:
            current_time = start
            while current_time + delta <= end:
                self.free_slots.append((current_time, current_time+delta))
                current_time += delta


    def print_busy_time(self):
        for start, end in self.busy_time:
            print(f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}")


    def print_free_time(self):
        for start, end in self.free_time:
            print(f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}")


    def print_slots(self):
        for start, end in self.free_slots:
            print(f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}")



if __name__ == '__main__':
    busy_slots = [
    {'start' : '10:30',
    'stop' : '10:50'
    },
    {'start' : '18:40',
    'stop' : '18:50'
    },
    {'start' : '14:40',
    'stop' : '15:50'
    },
    {'start' : '16:40',
    'stop' : '17:20'
    },
    {'start' : '20:05',
    'stop' : '20:20'
    }
    ]

    timetable = Timetable()

    timetable.set_busy_time(busy_slots)
    timetable.find_free_time()
    timetable.find_slots()
    timetable.print_slots()