import csv

def get_trends():
    with open("relatedEntities.csv") as f:
        lines = f.readlines()
        i =0
        for line in lines:
            if line == "RISING\n":
                break
            i += 1
        data = []
        for integers in range(i+1,lines.__len__()-1):
            a = lines[integers].split(",")
            a[1] =a[1].replace("+","")
            a[1] = a[1].replace("\n", "")
            a[1] =a[1].replace("%", "")
            if a[1] == "Breakout":
                a[1] = 3000
            a[1] = float(a[1])
            a[1] = a[1]/100
            data.append(a)
        return data

if __name__ == '__main__':
    get_trends()

