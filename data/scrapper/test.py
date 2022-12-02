normal_count = 2
line_num = 1
sep = '/SEPARATOR/'
file_path = './data/csv_data/cleaned_ratings.csv'

sep_exeeded = []

with open(file_path, 'r') as f:
    for line in f:
        count = 0
        for c in line:
            if c == sep:
                count+=1
        if count > normal_count:
            sep_exeeded.append({
                "line_num" : line_num,
                'number' : count
                })
        line_num += 1

for line in sep_exeeded:
    print(line)
