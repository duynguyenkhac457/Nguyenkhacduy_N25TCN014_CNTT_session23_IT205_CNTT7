import math

def show_flight_log(flights):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    for i, f in enumerate(flights, 1):
        water_supply = math.ceil(f["passengers"] / 10)
        print(f"{i}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | "
              f"Số khách: {f['passengers']} | Dự phòng: {water_supply} thùng nước.")