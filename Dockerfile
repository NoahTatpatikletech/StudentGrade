FROM python:3.12
WORKDIR /app
COPY . .
CMD ["python3", "student_grade.py", "Noah", "BCA", "3", "85", "90", "88"]
