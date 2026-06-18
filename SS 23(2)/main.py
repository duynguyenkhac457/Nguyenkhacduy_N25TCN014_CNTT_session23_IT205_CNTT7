from disk_manager import calculate_disk_blocks
from io_helper import safe_create_dir
from time_validator import parse_and_inspect_date

raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")

print(safe_create_dir("media_vault"))

print("----------------------------------------------------")

success_count = 0

for file in raw_files:
    print(f"\n[TỆP TIN: {file['filename']}]")

    # validate date
    parsed_date, error = parse_and_inspect_date(file["upload_at"])

    if error:
        print(f" + Trạng thái phân loại: 🔴 THẤT BẠI ({error})")
        continue

    # tính block
    blocks = calculate_disk_blocks(file["size_bytes"])

    # phân loại file
    file_type = "audio" if file["filename"].endswith(".mp3") else "video"

    print(f" + Dung lượng thực tế: {file['size_bytes']:,} Bytes")
    print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
    print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{file_type}')")

    success_count += 1

print("========================================================")
print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{len(raw_files)} tệp tin thành công.")