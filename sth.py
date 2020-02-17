# Starter code for CS 165B HW2 Spring 2019
from __future__ import division

def run_train_test(training_input, testing_input):
    """
    Implement the training and testing procedure here. You are permitted
    to use additional functions but DO NOT change this function definition.
    You are permitted to use the numpy library but you must write
    your own code for the linear w.

    Inputs:
        training_input: list form of the training file
            e.g. [[3, 5, 5, 5],[.3, .1, .4],[.3, .2, .1]...]
        testing_input: list form of the testing file

    Output:
        Dictionary of result values

        IMPORTANT: YOU MUST USE THE SAME DICTIONARY KEYS SPECIFIED

        Example:
            return {
                "tpr": #your_true_positive_rate,
                "fpr": #your_false_positive_rate,
                "error_rate": #your_error_rate,
                "accuracy": #your_accuracy,
                "precision": #your_precision
            }
    """

    setting = training_input[0]
    dimension = setting[0]
    sizeOfData = []
    for i in range(1, 4):
        sizeOfData.append(setting[i])
    collectionOfCenter = []
    for i in range(0,3):
        now = 1
        for j in range(0, i):
            now += sizeOfData[j]
        collectionOfCenter.append(getCenter(training_input, dimension, now, now + sizeOfData[i]-1, sizeOfData[i]))
    wAB = []
    for i in range(0,dimension):
        wAB.append(collectionOfCenter[0][i]-collectionOfCenter[1][i])
    wAC = []
    for i in range(0, dimension):
        wAC.append(collectionOfCenter[0][i] - collectionOfCenter[2][i])
    wBC = []
    for i in range(0, dimension):
        wBC.append(collectionOfCenter[1][i] - collectionOfCenter[2][i])
    tAB = 0
    for i in range(0,dimension):
        p_n = collectionOfCenter[0][i]+collectionOfCenter[1][i]
        p_n_ = collectionOfCenter[0][i] - collectionOfCenter[1][i]
        tAB += p_n*p_n_*0.5
    tAC = 0
    for i in range(0, dimension):
        p_n = collectionOfCenter[0][i] + collectionOfCenter[2][i]
        p_n_ = collectionOfCenter[0][i] - collectionOfCenter[2][i]
        tAC += p_n * p_n_ * 0.5
    tBC = 0
    for i in range(0, dimension):
        p_n = collectionOfCenter[1][i] + collectionOfCenter[2][i]
        p_n_ = collectionOfCenter[1][i] - collectionOfCenter[2][i]
        tBC += p_n * p_n_ * 0.5

###################testing
    TP_A = FN_A = FP_A = TN_A = 0
    TP_B = FN_B = FP_B = TN_B = 0
    TP_C = FN_C = FP_C = TN_C = 0
    testSetting = testing_input[0]
    TestsizeOfData = []
    for i in range(1, 4):
        TestsizeOfData.append(testSetting[i])
    for i in range(1, TestsizeOfData[0] + 1):
        if (test(testing_input, wAB, tAB, i, dimension)==True and test(testing_input, wAC, tAC, i,dimension)==True):
            TP_A += 1
        else:
            FN_A += 1

        if (test(testing_input, wAB,tAB, i,  dimension)==False and test(testing_input, wBC, tBC,i, dimension)==True):
            FP_B += 1
        else:
            TN_B += 1

        if (test(testing_input, wAC,tAC,i, dimension)==False and test(testing_input, wBC, tBC,i,dimension)==False):
            FP_C += 1
        else:
            TN_C += 1
    for i in range(TestsizeOfData[0] + 1, TestsizeOfData[0] + TestsizeOfData[1] + 1):
        if (test(testing_input, wAB, tAB, i, dimension) == True and test(testing_input, wAC, tAC, i,
                                                                         dimension) == True):
            FP_A += 1
        else:
            TN_A += 1

        if (test(testing_input, wAB,tAB, i,  dimension)==False and test(testing_input, wBC, tBC, i,dimension)==True):
            TP_B += 1
        else:
            FN_B += 1

        if (test(testing_input, wAC, tAC, i,dimension) == False and test(testing_input, wBC, tBC,i, dimension) == False):
            FP_C += 1
        else:
            TN_C += 1
    for i in range(TestsizeOfData[0] + TestsizeOfData[1] + + 1, TestsizeOfData[0] + TestsizeOfData[1] + TestsizeOfData[2] + 1):
        if (test(testing_input, wAB, tAB, i, dimension) == True and test(testing_input, wAC, tAC, i, dimension) == True):
            FP_A += 1
        else:
            TN_A += 1
        if (test(testing_input, wAB,tAB, i,  dimension)==False and test(testing_input, wBC, tBC, i,dimension)==True):
            FP_B += 1
        else:
            TN_B += 1

        if (test(testing_input, wAC, tAC,i, dimension) == False and test(testing_input, wBC, tBC, i,dimension) == False):
            TP_C += 1
        else:
            FN_C += 1
    tpr_A = (TP_A) / (TP_A + FN_A)
    tpr_B = (TP_B) / (TP_B + FN_B)
    tpr_C = (TP_C) / (TP_C + FN_C)
    if (FP_A != 0):
        fpr_A = (FP_A) / (FP_A + TN_A)
    else:
        fpr_A = 0
    if (FP_B != 0):
        fpr_B = (FP_B) / (FP_B + TN_B)
    else:
        fpr_B = 0
    if (FP_C != 0):
        fpr_C = (FP_C) / (FP_C + TN_C)
    else:
        fpr_C = 0
    error_rate_A = (FP_A + FN_A) / (TP_A + TN_A + FP_A + FN_A)
    accuracy_A = (TP_A + TN_A) / (TP_A + TN_A + FP_A + FN_A)
    precision_A = TP_A / (TP_A + FP_A)
    error_rate_B = (FP_B + FN_B) / (TP_B + TN_B + FP_B + FN_B)
    accuracy_B = (TP_B + TN_B) / (TP_B + TN_B + FP_B + FN_B)
    precision_B = TP_B / (TP_B + FP_B)
    error_rate_C = (FP_C + FN_C) / (TP_C + TN_C + FP_C + FN_C)
    accuracy_C = (TP_C + TN_C) / (TP_C + TN_C + FP_C + FN_C)
    precision_C = TP_C / (TP_C + FP_C)
    tpr = (tpr_A + tpr_B + tpr_C) / 3
    fpr = (fpr_A + fpr_B + fpr_C) / 3
    error_rate = (error_rate_A + error_rate_B + error_rate_C) / 3
    accuracy = (accuracy_A + accuracy_B + accuracy_C) / 3
    precision = (precision_A + precision_B + precision_C) / 3
    return {"tpr": tpr, "fpr": fpr, "error_rate": error_rate, "accuracy": accuracy, "precision": precision}


def test(filename, w, t, now, dimension):
    result = 0
    for j in range(0, dimension):
        result += filename[now][j] * w[j]
    if result > t:
        return 1
    else:
        return 0


def getCenter(filename, dimension, begins, ends, counts):
    points = []
    for i in range (0, dimension):
        points.append(0)
    for i in range(begins, ends+1):
        for j in range(0, dimension):
            points[j] += filename[i][j]

    for i in range(0, dimension):
        points[i] /= counts

    return points





#######
# The following functions are provided for you to test your w.
######
def parse_file(filename):
    """
    This function is provided to you as an example of the preprocessing we do
    prior to calling run_train_test
    """
    with open(filename, "r") as f:
        data = [[float(y) for y in x.strip().split(" ")] for x in f]
        data[0] = [int(x) for x in data[0]]

        return data

if __name__ == "__main__":
    """
    You can use this to test your code.
    python hw2.py [training file path] [testing file path]
    """
    import sys

    training_input = parse_file(sys.argv[1])
    testing_input = parse_file(sys.argv[2])

    run_train_test(training_input, testing_input)

