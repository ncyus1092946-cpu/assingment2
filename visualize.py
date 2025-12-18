import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import os

FILENAME = "expenses.csv"

def load_expenses(filename):
    """讀取 CSV 檔並彙總各 category 的金額"""
    if not os.path.exists(filename):
        print(f" 找不到 {filename}，請先請 Member A 執行 input.py 建立資料。")
        return None

    category_sum = defaultdict(float)

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                amount = float(row["amount"])
                category = row["category"]
                category_sum[category] += amount
            except (KeyError, ValueError):
                continue

    return category_sum

def make_pie_chart(category_sum):
    """根據各分類金額畫圓餅圖"""
    if not category_sum:
        print("沒有資料可畫圖。")
        return

    labels = list(category_sum.keys())
    values = list(category_sum.values())

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Breakdown by Category")
    plt.axis("equal")  # 讓圓餅圖為正圓

    plt.savefig("piechart.png")
    print("圓餅圖已儲存為 piechart.png")
    plt.show()

def main():
    data = load_expenses(FILENAME)
    if data:
        make_pie_chart(data)

if __name__ == "__main__":
    main()