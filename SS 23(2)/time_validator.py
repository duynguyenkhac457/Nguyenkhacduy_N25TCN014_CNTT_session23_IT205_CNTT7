from datetime import datetime

def parse_and_inspect_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d"), None
    except ValueError:
        return None, f"Lỗi: Định dạng ngày '{date_str}' không hợp lệ"