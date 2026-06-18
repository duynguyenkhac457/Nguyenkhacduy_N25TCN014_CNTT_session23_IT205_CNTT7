from logistics import show_flight_log
from manager import add_flight
from time_helper import calculate_eta
from file_helper import create_log_folder

flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85, "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
    print("1. Hiển thị lịch trình và Thống kê hậu cần")
    print("2. Tiếp nhận chuyến bay mới")
    print("3. Tính ETA")
    print("4. Tạo thư mục log hệ thống")
    print("5. Thoát")
    print("==================================================")

    try:
        choice = int(input("Nhập lựa chọn của bạn: "))

        if choice == 1:
            show_flight_log(flights)

        elif choice == 2:
            add_flight(flights)

        elif choice == 3:
            calculate_eta(flights)

        elif choice == 4:
            create_log_folder()

        elif choice == 5:
            print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
            break

        else:
            print("Vui lòng nhập từ 1-5!")

    except ValueError:
        print("Lỗi: Vui lòng nhập số từ 1 đến 5!")