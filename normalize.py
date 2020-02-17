from io import open
if __name__ == "__main__":
    f1 = open("1.txt",encoding='UTF-8')
    f2 = open("2.txt",encoding='UTF-8')
    f5 = open("5.txt",encoding='UTF-8')
    f6 = open("6.txt", encoding='UTF-8')
    f9 = open("9.txt",encoding='UTF-8')
    fall = open("all.txt",'w', encoding='UTF-8')
    contents2 = f2.readlines()
    contents1 = f1.readlines()
    contents5 = f5.readlines()
    contents6 = f6.readlines()
    contents9 = f9.readlines()
    for each1 in contents1:
        each1 = each1.replace(',','')
        seperate1 = each1.split("+++")
        seperate1[1] = seperate1[1].strip("\n")
        fall.write(unicode(seperate1[1]+","+seperate1[0]+'\n'))
    for each2 in contents2:
        each2 = each2.replace(',', '')
        seperate2 = each2.split("+++")
        seperate2[1] = seperate2[1].strip("\n")
        fall.write(unicode(seperate2[1] + "," + seperate2[0] + '\n'))
    for each5 in contents5:
        each5 = each5.replace(',', '')
        seperate5 = each5.split("+++")
        seperate5[1] = seperate5[1].strip("\n")
        fall.write(unicode(seperate5[1] + "," + seperate5[0] + '\n'))
    for each6 in contents6:
        each6 = each6.replace(',', '')
        seperate6 = each6.split("+++")
        seperate6[1] = seperate6[1].strip("\n")
        fall.write(unicode(seperate6[1] + "," + seperate6[0] + '\n'))
    for each9 in contents9:
        each9 = each9.replace(',', '')
        seperate9 = each9.split("+++")
        seperate9[1] = seperate9[1].strip("\n")
        fall.write(unicode(seperate9[1] + "," + seperate9[0] + '\n'))
    fall.close()