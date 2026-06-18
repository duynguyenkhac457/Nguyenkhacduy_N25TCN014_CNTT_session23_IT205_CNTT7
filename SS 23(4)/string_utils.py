def normalize_student_names(records):
    for r in records:
        name = r["name"].strip()
        name = " ".join(name.split())
        r["name"] = name.title()

    return records