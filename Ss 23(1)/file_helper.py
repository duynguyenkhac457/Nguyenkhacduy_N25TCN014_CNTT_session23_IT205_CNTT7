import os

def create_log_dir(dir_name="logs"):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        return f"[INFO] Tạo thư mục {dir_name} thành công."
    return f"[INFO] Thư mục {dir_name} đã tồn tại."