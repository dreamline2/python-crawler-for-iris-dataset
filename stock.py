#!/user/bin/env python3
import csv
import matplotlib.pyplot as plt
fn = 'stock.csv'
with open(fn, encoding="ISO-8859-1") as f:
    csvRead = csv.reader(f)
    csvList = list(csvRead)  # 轉成串列
    csvData = csvList[2:-4]
    months, highs, lows, prices = [], [], [], []
    for row in csvData:
        highs.append(float(row[2]))
        lows.append(float(row[3]))
        prices.append(float(row[4]))
        months.append(int(row[1]))
fig = plt.figure(dpi=80, figsize=(12, 8))
plt.plot(months, highs, '-*', label='High')
plt.plot(months, lows, '-o', label='Low')
plt.plot(months, prices, '-^', label='Price')
plt.legend(loc='upper center')
# fig.autofmt_xdate()
plt.title("TSMC", fontsize=24)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Price", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
