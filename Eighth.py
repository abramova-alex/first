def compute_grade(score):
    try:
        score = float(score)
        if score <= 1 and score >= 0:
            if score >= 0.9:
                return 'A'
            elif score >= 0.8:
                return 'B'
            elif score >= 0.7:
                return 'C'
            elif score >= 0.6:
                return 'D'
            else:
                return 'F'
        else:
             return 'Bad score'
    except:
        return 'Bad score'

score = raw_input('Enter score: ')
print compute_grade(score)


