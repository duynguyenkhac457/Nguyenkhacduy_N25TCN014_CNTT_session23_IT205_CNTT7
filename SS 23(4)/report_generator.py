from datetime import datetime
from colorama import Fore, init
from score_utils import calculate_average, classify_student

init(autoreset=True)

def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for i, s in enumerate(records, 1):
        avg = calculate_average(s["scores"])
        rank = classify_student(avg)

        print(f"{i}. [{s['student_id']}] {s['name']} | "
            f"Điểm: {s['scores']} | ĐTB: {avg:.2f} - {rank}")

    print("---------------------------------")


def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    pass_count = 0
    fail_count = 0

    for s in records:
        avg = calculate_average(s["scores"])
        if avg >= 5:
            pass_count += 1
        else:
            fail_count += 1

    content = f"""
===== LEARNING REPORT =====
Time: {datetime.now()}

Total students: {total}
Passed: {pass_count}
Need improvement: {fail_count}
"""

    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print(Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt")