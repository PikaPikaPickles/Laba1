import csv
import matplotlib.pyplot as plt
New_File = []
with open("students.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    Preps = set()
    Grades = list()

    for row in file_reader:
        Preps.add(row[0].split(';')[0])
        New_File.append(row)
    Preps1 = sorted(list(Preps))
    SlovarPrepov = dict()
    for i in Preps1:
        ListThisGrade = list()
        for j in New_File:
            if j[0].split(';')[0] == i:
                ListThisGrade.append(j[0].split(';')[2])
        SlovarPrepov[i] = ListThisGrade
    for t in SlovarPrepov.keys():
        vals_name = sorted(list(set(SlovarPrepov[t])))
        vals_count = [SlovarPrepov[t].count(i) for i in vals_name]
        explode = None
        fig, ax = plt.subplots()
        ax.pie(vals_count, labels=vals_name, autopct='%1.1f%%', shadow=True, explode=explode,
               wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)
        ax.axis("equal")
        fig.savefig(f'{t}.png')

