import os

def create_log_folder():
    print("----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")

    folder = "aviation_logs"

    if os.path.exists(folder):
        print("[SYSTEM] Thư mục đã tồn tại, bỏ qua bước khởi tạo")
    else:
        os.mkdir(folder)
        print("[SYSTEM] Thư mục 'aviation_logs' chưa tồn tại. Đang tiến hành khởi tạo...")
        print("[SYSTEM] Tạo thư mục thành công!")