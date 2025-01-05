class StudentScores:
    scores = {}
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n')
                line_sp = line.split(',')
                StudentScores.scores[line_sp[0]] = line_sp[1]
    
    def avg_scroes(self):
        sum = 0
        score = list(StudentScores.scores.values())
        for i in score:
            sum += int(i)
        return sum / len(score)
    
    def split_students(self, over=True):
        students = list(StudentScores.scores.keys())
        st_output = []
        if over:
            for name in students:
                if int(StudentScores.scores.get(name)) >= self.avg_scroes():
                    st_output.append(name)
                else:
                    continue
        else:
            for name in students:
                if int(StudentScores.scores.get(name)) <= self.avg_scroes():
                    st_output.append(name)
                else:
                    continue
        return st_output
    
    def down_to_file(self):
        down_st = self.split_students(0)
        with open("below_average_korean.txt", "w", encoding='utf-8') as f:
            for i in down_st:
                data = f'{i},{StudentScores.scores[i]}\n'
                f.write(data)
    
    def print_scores(self):
        print(f'평균 점수: {self.avg_scroes()}')
        print(f'평균 이상을 받은 학생들: {self.split_students()}')
 

test = StudentScores("scores_korean.txt")
test.print_scores()
test.down_to_file()