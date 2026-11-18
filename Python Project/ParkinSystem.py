from datetime import datetime
from math import ceil

parkings={
    1:{"2W":[0]*20,"4W":[0]*15},
    2:{"2W":[0]*20,"4W":[0]*15}
}
tickets={}
ticket_number=1

def entry(vehicle_no,vehicle_type):
    global ticket_number

    for level in parkings:
        for i in range(len(parkings[level][vehicle_type])):
            if parkings[level][vehicle_type][i] == 0:
                parkings[level][vehicle_type][i] = 1

                id = "T"+str(ticket_number)
                ticket_number += 1

                tickets[id] = {
                    "vehcile_no":vehicle_no,
                    "type":vehicle_type,
                    "level":level,
                    "slot":i,
                    "time":datetime.now()
                }

                return id
    return "Slots are not available"

# t1=entry("MH45AK8352","2W")
# print("Ticket:",t1)

def exit_entry(id):
    if id not in tickets:
        return "Invalid Ticket"

    t=tickets[id]

    duration = datetime.now()-t["time"]
    hours = ceil(duration.total_seconds()/3600)

    rate =10 if t["type"]=="2W" else 20

    bill = hours*rate
    parkings[t["level"]][t["type"]][t["slot"]] = 0

    del tickets[id]
    return bill


t1=entry("MH45AK8352","2W")
print("Ticket:",t1)
bill=exit_entry(t1)
print("Bill:",bill)