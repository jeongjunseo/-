##################
# 프로그램명: 성적관리 프로그램(grade_management)
# 작성자: 소프트웨어학부/정준서
# 작성일: 2025-04-13
# 프로그램 설명: 5명의 학생의 성적을 관리(학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산)
##################

class Student:
    def __init__(self, student_id, name, english, c_language, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.total = 0
        self.average = 0
        self.grade = ''
        self.rank = 0
        self.calculate_total_avg()
        self.calculate_grade()

    def calculate_total_avg(self):
        self.total = self.english + self.c_language + self.python
        self.average = self.total / 3

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

class StudentManager:
    def __init__(self):
        self.students = []

    def input_students(self):
        for _ in range(5):
            student_id = input("학번: ")
            name = input("이름: ")
            english = int(input("영어 점수: "))
            c_lang = int(input("C언어 점수: "))
            python = int(input("파이썬 점수: "))
            self.students.append(Student(student_id, name, english, c_lang, python))
        self.calculate_ranks()

    def calculate_ranks(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def display_students(self):
        print("\n[전체 학생 정보 출력]")
        for s in self.students:
            print(f"{s.student_id} {s.name} 총점:{s.total} 평균:{s.average:.2f} 학점:{s.grade} 등수:{s.rank}")

    def insert_student(self):
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_lang = int(input("C언어 점수: "))
        python = int(input("파이썬 점수: "))
        self.students.append(Student(student_id, name, english, c_lang, python))
        self.calculate_ranks()

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        self.calculate_ranks()

    def search_student(self, keyword):
        print(f"\n[검색결과: '{keyword}']")
        for s in self.students:
            if s.student_id == keyword or s.name == keyword:
                print(f"{s.student_id} {s.name} 총점:{s.total} 평균:{s.average:.2f} 학점:{s.grade} 등수:{s.rank}")

    def sort_by_total(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        print("\n[총점으로 정렬됨]")

    def count_above_80(self):
        count = sum(1 for s in self.students if s.average >= 80)
        print(f"\n평균 80점 이상 학생 수: {count}")

def main():
    manager = StudentManager()
    manager.input_students()

    while True:
        print("\n--- 메뉴 ---")
        print("1. 전체 출력\n2. 학생 추가\n3. 학생 삭제\n4. 학생 검색\n5. 총점 정렬\n6. 80점 이상 학생 수\n0. 종료")
        choice = input("선택: ")
        
        if choice == '1':
            manager.display_students()
        elif choice == '2':
            manager.insert_student()
        elif choice == '3':
            sid = input("삭제할 학번: ")
            manager.delete_student(sid)
        elif choice == '4':
            keyword = input("학번 또는 이름: ")
            manager.search_student(keyword)
        elif choice == '5':
            manager.sort_by_total()
        elif choice == '6':
            manager.count_above_80()
        elif choice == '0':
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()