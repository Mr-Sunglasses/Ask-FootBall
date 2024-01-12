import csv
from ask_football.main import find_columns_and_filters

table_headers = [
    "Year",
    "Hosts",
    "Venues_Cities",
    "Total_Attendance",
    "Matches",
    "Average_Attendance",
    "Highest_Attendance",
    "Highest_Attendance_Venue",
    "Highest_Attendance_Games"
]

questions = [
    "What was the venue/host of the World Cup in 1950?",
    "In which location was the World Cup of 1950 held?",
    "How many people attended the World Cup in 1950?",
    "Where were all World Cups held between 1900-2000?",
    "Which country hosted the most World Cups?",
    "Which World Cup had the highest overall attendance?",
    "Which World Cup venues were used in Brazil?",
    "Which World Cup had the lowest final match attendance?",
    "What is the average attendance of World Cup finals since 1950?",
    "Which city has hosted the most World Cup matches?",
    "Which World Cup had the most attending fans in total?",
    "What was the last World Cup venue before 1950?",
    "How many World Cup finals have been held in Brazil?",
    "Who were the finalists in the most attended World Cup final?",
    "What is the total attendance of all World Cup finals combined?",
    "What was the venue of the highest scoring World Cup final?",
    "Which World Cup had the lowest average match attendance?"
]

answers = []

for question in questions:
    output = find_columns_and_filters(
        table_headers=table_headers, question=question)
    answers.append(output)

null = 0

for i in answers:
    if i == ([], {}):
        null += 1

print(f"Accuracy Right {len(questions) - null} out of {len(questions)}")
