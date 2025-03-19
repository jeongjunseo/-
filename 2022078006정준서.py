std = [[0] * 10 for _ in range(9)] #학생과 과목별 성적리스트

#인덱스별 구성
#   0    1    2   3        4     5     6      7      8    
# 학번 이름 영어   C   python  총점   평균   학점   등수

#총점
def total(n):
    std[n][5]=std[n][2]+std[n][3]+std[n][4]
        
#학점 처리
def grade(grade) :
    if grade>=95:
        return "A+"
    elif grade>=90:
        return "A"
    elif grade>=85:
        return "B+"
    elif grade>=80:
        return "B"
    elif grade>=75:
        return "C+"
    elif grade>=70:
        return "C"
    elif grade>=65:
        return "D+"
    elif grade>=60:
        return "D"
    elif grade<60:
        return "F"   

#평균
def average(n):
    std[n][6]=(std[n][5]/3)
    
#등수
def get_rank():
    scores=[std[n][5] for n in range(0,5)]
    sorted_scores=sorted(scores, reverse=True)
    for n in range(0,5):
        std[n][8]=sorted_scores.index(std[n][5])
                   
#5명 학생 정보입력
for n in range(0,5):
    print(f"학생{n+1}의 성적을 입력하시오.")
    std[n][0]=int(input("학번:"))
    std[n][1]=str(input("이름:"))
    std[n][2]=int(input("영어:"))
    std[n][3]=int(input("C-언어:"))
    std[n][4]=int(input("파이썬:"))
    total(n)                    #총점
    average(n)                  #평균
    std[n][7]=grade(std[n][6])  #학점

get_rank()

print("\n=============================================================================")
print("학번      이름        영어    C-언어  파이썬   총점    평균    학점    등수")
print("=============================================================================")
for n in range(0, 5):
    print(f"{std[n][0]:<10} {std[n][1]:<10} {std[n][2]:<6} {std[n][3]:<6} {std[n][4]:<6} "
          f"{std[n][5]:<6} {std[n][6]:<6.2f} {std[n][7]:<6} {std[n][8]:<6}")
