# Python 檔案操作：一步一步練習

這份教學會帶你練習如何用 Python 讀取、建立和修改文字檔。請先把本文件、`lesson_sample.txt` 和 `students.csv` 放在同一個資料夾，並用該資料夾作為執行程式時的目前工作目錄。

## 0. 準備範例檔案

打開 `lesson_sample.txt`，你會看到：

```text
蘋果：3 個
香蕉：5 個
橘子：2 個
```

稍後的程式會讀取這個檔案。範例使用 UTF-8 編碼，Python 開檔時也會明確指定 `encoding="utf-8"`，避免中文亂碼。

## 1. 讀取整個檔案

建立一個 Python 檔案，例如 `practice_read.py`，輸入：

```python
with open("lesson_sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

執行後會印出範例檔案的全部內容。

- `open(...)` 開啟檔案。
- `"lesson_sample.txt"` 是檔案名稱；這個相對路徑會從「目前工作目錄」開始尋找。
- `"r"` 表示以讀取模式開啟。
- `encoding="utf-8"` 指定文字編碼。
- `read()` 讀取整個檔案，並把內容回傳成字串。
- `with` 區塊結束時會自動關閉檔案，建議養成這個寫法。

## 2. 一次讀取一行

如果想逐行讀取，可以使用 `readline()`：

```python
with open("lesson_sample.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print(first_line, end="")
print(second_line, end="")
```

每呼叫一次 `readline()`，就會讀取下一行。每行通常包含換行字元 `\n`；`print()` 本身也會換行，因此範例用 `end=""` 避免多出空白行。

## 3. 用迴圈逐行讀取

讀取行數不固定的檔案時，直接迭代檔案物件很方便：

```python
with open("lesson_sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

`strip()` 會移除字串前後的空白字元，包含每行結尾的換行字元。

## 4. 把每一行存成清單

`readlines()` 會回傳由多行文字組成的清單：

```python
with open("lesson_sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

結果大致像這樣（每個項目通常還有 `\n`）：

```text
['蘋果：3 個\n', '香蕉：5 個\n', '橘子：2 個\n']
```

小檔案可以用這個方法；若檔案很大，使用上一節的逐行迴圈通常更合適。

## 5. 建立或覆寫檔案

使用 `"w"` 寫入模式。如果檔案不存在，Python 會建立它；如果已經存在，原本內容會被清空再寫入。

```python
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("今天開始學 Python 檔案操作。\n")
    file.write("這是第二行。\n")
```

執行後，資料夾會多出 `my_notes.txt`。再次執行這段程式，舊內容會被覆蓋，所以請小心使用 `"w"`。

## 6. 在檔案結尾附加內容

使用 `"a"` 附加模式，既有內容會保留，新內容會加在檔案結尾：

```python
with open("my_notes.txt", "a", encoding="utf-8") as file:
    file.write("這一行是後來附加的。\n")
```

程式每執行一次，就會多附加一行。

## 7. 常見檔案模式

| 模式 | 用途 | 注意事項 |
| --- | --- | --- |
| `"r"` | 讀取檔案 | 檔案必須已存在 |
| `"w"` | 建立或寫入檔案 | 會清空已存在的檔案 |
| `"a"` | 在檔案結尾附加內容 | 不會清除原內容 |
| `"x"` | 建立新檔案 | 若檔案已存在會發生錯誤 |

初學時，請特別記住：讀檔用 `"r"`，新增或覆寫用 `"w"`，保留舊內容並追加用 `"a"`。

## 8. 處理找不到檔案的情況

如果檔案名稱或路徑打錯，會發生 `FileNotFoundError`。你可以明確處理這種情況：

```python
try:
    with open("not_here.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("找不到檔案，請確認檔名和路徑。")
```

練習時可以先用不存在的檔名執行，觀察程式如何顯示提示。

## 9. 路徑練習（選讀）

`pathlib` 是 Python 內建的路徑工具。以下程式會建立子資料夾 `practice_output`，並在裡面寫入檔案：

```python
from pathlib import Path

output_folder = Path("practice_output")
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "message.txt"
output_file.write_text("我用 pathlib 寫入檔案！\n", encoding="utf-8")

print(output_file.read_text(encoding="utf-8"))
```

`Path("practice_output") / "message.txt"` 會組合出路徑；`mkdir(exist_ok=True)` 會建立資料夾，若資料夾已存在則不會報錯。

## 10. 讀寫 CSV 表格

CSV（逗號分隔值）是常見的表格格式，可以用 Excel 開啟。打開 `students.csv`，你會看到：

```text
姓名,國文,英文,數學
小明,85,92,78
小華,90,88,95
小美,76,81,89
小強,68,74,82
```

### 10-1. 用 `csv.reader` 逐列讀取

```python
import csv

with open("students.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # 先取出第一列標題
    print("欄位：", header)
    for row in reader:
        print(row)
```

每一列會變成一個清單，例如 `['小明', '85', '92', '78']`。注意：讀進來的數字都是字串，要計算時需用 `int(...)` 轉換。開啟 CSV 時建議加上 `newline=""`，交給 `csv` 模組處理換行。

### 10-2. 用 `csv.DictReader` 以欄位名稱取值

```python
import csv

with open("students.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row["國文"]) + int(row["英文"]) + int(row["數學"])
        print(row["姓名"], "總分：", total)
```

`DictReader` 會把第一列當作欄位名稱，每一列變成字典，用 `row["數學"]` 這種方式取值更好讀。

### 10-3. 用 `csv.writer` 寫出新的 CSV

```python
import csv

rows = [
    ["姓名", "總分"],
    ["小明", 255],
    ["小華", 273],
]

with open("scores.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

使用 `"utf-8-sig"` 編碼寫出，可讓 Excel 正確顯示中文。

## 11. 動手練習

請先使用 `lesson_sample.txt` 和 `students.csv` 完成以下任務，不必急著看解答：

1. 讀取並印出整個檔案。
2. 逐行印出內容，並移除每行尾端的換行。
3. 計算檔案有幾行。
4. 建立 `my_favorite.txt`，寫入你喜歡的三種水果。
5. 再執行一次附加模式，新增一種水果，確認舊內容仍在。
6. 改成讀取一個不存在的檔案，試著用 `try` / `except` 顯示友善訊息。
7. 讀取 `students.csv`，算出每位學生的平均分數。
8. 找出數學最高分的學生，並把每人的總分寫入 `scores.csv`。

### 第 3 題提示

可以先用 `readlines()` 取得清單，再用 `len(...)` 計算清單中的行數：

```python
with open("lesson_sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("行數：", len(lines))
```

## 小抄

```python
# 讀取
with open("檔名.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 覆寫
with open("檔名.txt", "w", encoding="utf-8") as file:
    file.write("新內容\n")

# 附加
with open("檔名.txt", "a", encoding="utf-8") as file:
    file.write("追加內容\n")
```
