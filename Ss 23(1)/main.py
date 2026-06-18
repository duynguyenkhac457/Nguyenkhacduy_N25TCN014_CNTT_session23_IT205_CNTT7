from file_helper import create_log_dir
from geo_calculator import calculate_distance
from time_estimator import predict_eta
from datetime import datetime

shipments = [
    {"id": "TRK-001", "from_lat": 21.0285, "from_lon": 105.8542,
     "to_lat": 10.8231, "to_lon": 106.6297,
     "depart": "2026-06-10 08:00:00",
     "deadline": "2026-06-11 12:00:00"},

    {"id": "TRK-002", "from_lat": 21.0285, "from_lon": 105.8542,
     "to_lat": 16.0544, "to_lon": 108.2022,
     "depart": "2026-06-10 09:30:00",
     "deadline": "2026-06-10 15:00:00"},
]

print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

print(create_log_dir())

print("--------------------------------------------------")

for s in shipments:
    distance = calculate_distance(
        s["from_lat"], s["from_lon"],
        s["to_lat"], s["to_lon"]
    )

    eta, dep_time = predict_eta(s["depart"], distance)

    deadline = datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")

    status = ""
    if eta <= deadline:
        status = "AN TOÀN (Kịp tiến độ trước deadline)"
    else:
        status = "CẢNH BÁO (Trễ hạn!)"

    print(f"\n[CHUYẾN XE {s['id']}]")
    print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
    print(f" + Thời gian khởi hành: {dep_time}")
    print(f" + Dự kiến cập bến (ETA): {eta}")
    print(f" + Trạng thái: {status}")

print("==================================================")