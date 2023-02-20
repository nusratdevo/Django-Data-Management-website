def score_grade(score):
    #if score <= 10:
       # return "A"

    if 0 <= score < 40:
            return "Fail"
    elif 40 <= score < 70:
            return "Pass"
    elif 70 <= score < 100:
            return "Excellent"
    else:
            return "Error"