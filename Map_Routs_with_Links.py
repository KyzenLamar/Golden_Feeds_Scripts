import csv

lines =[]

# This part is reading file with "null" routs

with open('Result.csv', 'r', encoding='utf-8') as file:
    result = file.readlines()
    #print(result)
    for line in result:
        line = line.rstrip()
        lines.append(line)

# This part is reading file with routs and links and make loop to find link for "null" rout.
with open('Booking links with routs.csv', 'r', encoding='utf-8') as orgfile:
    fildnames = ['rout', 'link']
    data = csv.reader(orgfile)
    res = dict(data)
    print(res)
    for key, value in res.items():
        if key not in lines:
            outFile = open('Final_results_Routs.csv', 'a', encoding='utf-8')
            fieldnames = ['Rout', 'Link']
            writer = csv.DictWriter(outFile, fieldnames=fieldnames)
            writer.writerow({'Rout': key, 'Link': value.replace('2021-04-08','2021-04-22')})  # making a replace for needed data.