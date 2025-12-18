Assignment 2

專案說明

本專案為一個以 Python 撰寫的簡易支出紀錄系統，由兩位組員合作完成，目的在於練習 Git 分支與合併（merge）的協作流程。

Member A：負責支出輸入模組，將資料儲存至 CSV 檔案  
Member B：負責資料視覺化模組，讀取 CSV 並依分類產生圓餅圖  

---

執行環境需求
  Python 3.8 以上
  matplotlib 套件

安裝 matplotlib

---

使用方式

步驟一：執行輸入模組（Member A）
此模組用來輸入支出資料。
執行後依序輸入：日期（YYYY-MM-DD）、金額、分類、備註（可選）
可在同一次執行中新增多筆資料。
所有資料將儲存於expenses.csv

步驟二：執行視覺化模組（Member B）
此模組會讀取已儲存的支出資料，並產生圓餅圖。
程式會：依支出分類統計金額、顯示圓餅圖
將圖表存成piechart.png