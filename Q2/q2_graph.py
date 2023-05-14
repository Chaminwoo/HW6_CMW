

import csv
import matplotlib.pyplot as plt

# 데이터 가져오기
with open('num_csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# 히스토그램 그리기
x_labels = ['1', '2', '3', '4', '5', '6']
for i in range(1, 4):
    count_data = [int(row[i]) for row in data[1:]]
    plt.hist(count_data, bins=20, alpha=0.5, label=f"{int(data[i][0]):,}")
plt.legend()
plt.xticks(range(1, 7), x_labels)
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Dice Roll Histogram')
plt.show()
