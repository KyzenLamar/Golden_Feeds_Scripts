import csv

# with open('taxonomy_full_us.csv', 'r', encoding='utf-8') as taxonomy:
#     for row in taxonomy:
#         row = row.split('-->')[-1].strip().replace('"','')#.replace('&',',')
#
#         print(row)

with open('taxonomy_full_us.csv','r',encoding='utf-8') as f:
    tax = dict(csv.reader(f))


with open('Google-mapping.csv','r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    with open('Google-mapping-result.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["Product name", "Merchant category", "Google category"])
        writer.writeheader()
        for row in reader:
            if row['Merchant category'] == '':
                category = row['Product name'].strip().replace('/','  ')#.replace(',,','').replace('"','').replace('/',',')
                for val in category.split():
                    val = val.strip()
                    if val in tax:
                        row['Merchant category'] = tax[val]
                        print(row)
            writer.writerow(row)


