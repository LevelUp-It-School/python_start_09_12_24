import json

# with open("lesson_9/json_file.json", encoding="UTF-8") as file_in:
#     records = json.load(file_in)

# records[1]["group_number"] = 2

# with open("lesson_9/json_file.json", 'w', encoding="UTF-8") as file_out:
#     json.dump(records, file_out, ensure_ascii=False, indent = 2)


records = {1: "First",
           2: "Second",
           3 : "Third"}
with open("lesson_9/output.json", 'w', encoding="UTF-8") as file_out:
     json.dump(records, file_out, ensure_ascii=False, indent = 2)