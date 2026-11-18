# Python 函式呼叫與參數語法完全說明書

本教材依據 [`function.ipynb`](file:///C:/Users/User/Desktop/暫存資料夾/test2/2026_11_18/function.ipynb) 課堂實作程式碼編寫，以循序漸進的方式，帶你徹底掌握 Python 函式（Function）的各種呼叫方式，並看懂函式簽章中常見的特殊符號：`/`、`*`、`*args`、`**kwargs` 以及解包（Unpacking）技巧。

---

## 目錄
- [一、核心前置觀念：參數 (Parameter) vs 引數 (Argument)](#一核心前置觀念參數-parameter-vs-引數-argument)
- [二、基礎呼叫方式](#二基礎呼叫方式)
  - [2.1 依位置呼叫（Positional Arguments）](#21-依位置呼叫positional-arguments)
  - [2.2 依名稱呼叫（Keyword Arguments）](#22-依名稱呼叫keyword-arguments)
  - [2.3 混用規則：位置引數必在關鍵字引數之前](#23-混用規則位置引數必在關鍵字引數之前)
  - [2.4 搭配預設參數值（Default Arguments）](#24-搭配預設參數值default-arguments)
- [三、特殊符號：限制傳遞方式（`/` 與 `*`）](#三特殊符號限制傳遞方式-與-)
  - [3.1 僅限位置參數：`/` (Positional-Only)](#31-僅限位置參數--positional-only)
  - [3.2 僅限關鍵字參數：`*` (Keyword-Only)](#32-僅限關鍵字參數--keyword-only)
  - [3.3 綜合切分：`/` 與 `*` 同時並存](#33-綜合切分-與--同時並存)
- [四、任意引數的打包（Packing）：`*args` 與 `**kwargs`](#四任意引數的打包packingargs-與-kwargs)
  - [4.1 `*args`：將多餘位置引數打包為 Tuple](#41-args將多餘位置引數打包為-tuple)
  - [4.2 `**kwargs`：將多餘關鍵字引數打包為 Dict](#42-kwargs將多餘關鍵字引數打包為-dict)
  - [4.3 函式參數宣告的標準完整順序](#43-函式參數宣告的標準完整順序)
- [五、實戰解讀 Python 內建函式簽章](#五實戰解讀-python-內建函式簽章)
  - [5.1 `print()` 函式解析與 `sep` / `end` 應用](#51-print-函式解析與-sep--end-應用)
  - [5.2 `sorted()` 函式解析與 `reverse` 應用](#52-sorted-函式解析與-reverse-應用)
- [六、進階呼叫技巧：引數解包（Unpacking）](#六進階呼叫技巧引數解包unpacking)
- [七、特殊符號速查對照表](#七特殊符號速查對照表)
- [八、常見錯誤與 Traceback 排除指南](#八常見錯誤與-traceback-排除指南)
- [九、課堂自我檢測題（附詳解）](#九課堂自我檢測題附詳解)

---

## 一、核心前置觀念：參數 (Parameter) vs 引數 (Argument)

在學習函式時，初學者常混淆這兩個名詞。請務必建立清楚的認知邊界：

- **參數 (Parameter / 形參)**：**定義函式時**宣告在 `def 函式名稱(...)` 括號內的變數名稱（如同空白表格中的「欄位名稱」）。
- **引數 (Argument / 實參)**：**呼叫函式時**實際填入括號內的值或物件（如同填入表格欄位中的「真實資料」）。

### 程式碼範例 (`Cell 1`)
```python
# 定義函式時，括號內的 name 是「參數」(Parameter)
def greet(name):
    print(f"哈囉,{name}!")

# 呼叫函式時，傳入的 "小明" 是「引數」(Argument)
greet("小明")  # 輸出：哈囉,小明!
```

> [!NOTE]
> 一句話記憶法：「**定**義寫**參**數，**呼**叫傳**引**數」。

---

## 二、基礎呼叫方式

### 2.1 依位置呼叫（Positional Arguments）
最直觀且常用的呼叫方式。Python 會依照呼叫時引數傳入的**由左至右順序**，一對一指派給對應的參數。

#### 程式碼範例 (`Cell 2-3`)
```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

# 正常位置傳入
describe_pet("貓", "小橘")  # 輸出：我養了一隻貓，牠叫做小橘。

# 順序對調時，語意會跟著改變
describe_pet("小橘", "貓")  # 輸出：我養了一隻小橘，牠叫做貓。
```

> [!WARNING] 常見錯誤
> 位置引數必須**數量完全吻合**：
> ```python
> # 少傳引數
> describe_pet("貓")
> # TypeError: describe_pet() missing 1 required positional argument: 'name'
>
> # 多傳引數
> describe_pet("貓", "小橘", 3)
> # TypeError: describe_pet() takes 2 positional arguments but 3 were given
> ```

---

### 2.2 依名稱呼叫（Keyword Arguments）
呼叫時明確指定 **`參數名稱=引數值`**。

#### 程式碼範例 (`Cell 4-5`)
```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

# 透過參數名稱指定，順序可自由調換
describe_pet(animal="貓", name="小橘")  # 輸出：我養了一隻貓，牠叫做小橘。
describe_pet(name="小橘", animal="貓")  # 輸出：我養了一隻貓，牠叫做小橘。
```

- **優點 1**：調換前後順序完全不影響執行結果。
- **優點 2**：程式碼可讀性大幅提升，閱讀者一目了然每個數值所代表的意義。

---

### 2.3 混用規則：位置引數必在關鍵字引數之前
若同時使用位置引數與關鍵字引數，**位置引數必須全部排在前面**。

#### 程式碼範例 (`Cell 6-7`)
```python
# 正確：先傳位置引數，再傳關鍵字引數
describe_pet("狗", name="旺財")  # 輸出：我養了一隻狗，牠叫做旺財。
```

> [!CAUTION] 語法違規示範
> 1. 位置引數排在關鍵字引數後面：
>    ```python
>    describe_pet(animal="狗", "旺財")
>    # SyntaxError: positional argument follows keyword argument
>    ```
> 2. 重複對同一個參數指派值：
>    ```python
>    describe_pet("狗", animal="貓")
>    # TypeError: describe_pet() got multiple values for argument 'animal'
>    ```

---

### 2.4 搭配預設參數值（Default Arguments）
定義函式時可賦予參數預設值。呼叫時若未傳入該引數，將自動採用預設值。

#### 程式碼範例 (`Cell 8-9`)
```python
def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"點餐：{drink}（{ice} / {sugar}）")

order_drink("紅茶")                            # 輸出：點餐：紅茶（正常冰 / 半糖）
order_drink("紅茶", "去冰")                    # 輸出：點餐：紅茶（去冰 / 半糖）
order_drink("紅茶", sugar="無糖")              # 輸出：點餐：紅茶（正常冰 / 無糖）
order_drink("綠茶", sugar="微糖", ice="少冰")  # 輸出：點餐：綠茶（少冰 / 微糖）
```

> [!TIP]
> 結合關鍵字引數，可直接跳過中間的參數（例如跳過 `ice`），僅指定欲客製化的參數（如 `sugar="無糖"`）。

---

## 三、特殊符號：限制傳遞方式（`/` 與 `*`）

在函式定義簽章中，單獨出現的 `/` 與 `*` 不是參數本身，而是**引數傳遞模式的邊界指示符**。

### 3.1 僅限位置參數：`/` (Positional-Only)
- 出現在 `/` **左側**的所有參數，在呼叫時**只能用位置傳入**，嚴禁寫出參數名稱。
- 設計目的：保護內部變數名稱，避免未來修改參數名稱時破壞呼叫端；或針對如 `math.sin(x)` 等語意極度明確的運算。

#### 程式碼範例 (`Cell 10-11`)
```python
def calc_bmi(weight, height, /):
    bmi = weight / (height ** 2)
    print(f"BMI 為：{bmi:.1f}")

calc_bmi(65, 1.75)  # 輸出：BMI 為：21.2

# 錯誤示範（寫出名稱會引發異常）：
# calc_bmi(weight=65, height=1.75)
# TypeError: calc_bmi() got some positional-only arguments passed as keyword arguments: 'weight, height'
```

---

### 3.2 僅限關鍵字參數：`*` (Keyword-Only)
- 出現在單獨 `*` **右側**的所有參數，在呼叫時**必須寫出參數名稱**，不得僅依位置傳值。
- 設計目的：強制呼叫者標註參數意義，特別適合布林值開關（Boolean Flag）或進階組態設定，大幅提升閱讀性與安全性。

#### 程式碼範例 (`Cell 12`)
```python
def send_email(to, *, subject, urgent=False):
    print(f"寄給：{to}｜主旨：{subject}｜急件：{urgent}")

send_email("student@example.com", subject="課堂通知", urgent=True)
# 輸出：寄給：student@example.com｜主旨：課堂通知｜急件：True

# 錯誤示範（用位置傳遞 subject 或 urgent）：
# send_email("student@example.com", "課堂通知", True)
# TypeError: send_email() takes 1 positional argument but 3 were given
```

---

### 3.3 綜合切分：`/` 與 `*` 同時並存
當 `/` 與 `*` 同時存在時，參數列表被精確切分為三個區間：

```text
def 函式名稱( 僅限位置參數 , / , 位置或名稱均可 , * , 僅限引數名稱 ):
```

#### 程式碼範例 (`Cell 13-14`)
```python
def register(id_no, /, name, *, role="student"):
    print(f"編號：{id_no}｜姓名：{name}｜身分：{role}")

# 正確呼叫示範
register("A01", "小明", role="leader")       # 輸出：編號：A01｜姓名：小明｜身分：leader
register("A01", name="小明", role="leader")  # 輸出：編號：A01｜姓名：小明｜身分：leader
register("A01", "小明")                      # 輸出：編號：A01｜姓名：小明｜身分：student
```

---

## 四、任意引數的打包（Packing）：`*args` 與 `**kwargs`

當設計函式時無法事先預期使用者會傳入多少引數時，使用星號語法可以在函式內部將引數「打包」為容器物件。

### 4.1 `*args`：將多餘位置引數打包為 Tuple
在參數前加上單星號 `*`，可吸收任意數量的位置引數，並組裝為一個 `tuple`。

#### 程式碼範例 (`Cell 15-16`)
```python
def sum_scores(*scores):
    print("收到的資料：", scores, type(scores))
    return sum(scores)

print(sum_scores(80, 90, 85))
# 輸出：
# 收到的資料： (80, 90, 85) <class 'tuple'>
# 255

print(sum_scores(80, 90))
# 輸出：
# 收到的資料： (80, 90) <class 'tuple'>
# 170

print(sum_scores())
# 輸出：
# 收到的資料： () <class 'tuple'>
# 0
```

---

### 4.2 `**kwargs`：將多餘關鍵字引數打包為 Dict
在參數前加上雙星號 `**`，可吸收任意數量的關鍵字引數，並組裝為一個 `dict`。

#### 程式碼範例 (`Cell 17`)
```python
def build_profile(name, **info):
    print("姓名：", name)
    print("其他資料：", info, type(info))

build_profile("小華", city="台北", course="Python")
# 輸出：
# 姓名： 小華
# 其他資料： {'city': '台北', 'course': 'Python'} <class 'dict'>
```

---

### 4.3 函式參數宣告的標準完整順序
若在同一個函式定義中包含多種參數類型，必須嚴格依照下列順序排列：

```python
def standard_func(
    pos_only, /,          # 1. 僅限位置參數
    pos_or_kw,            # 2. 位置或關鍵字皆可的標準參數
    *args,                # 3. 可變位置參數 (Tuple 打包)
    kw_only,              # 4. 僅限關鍵字參數 (*args 之後的參數自動具備此特性)
    **kwargs              # 5. 可變關鍵字參數 (Dict 打包)
):
    pass
```

---

## 五、實戰解讀 Python 內建函式簽章

掌握上述語法後，便能輕鬆解讀 Python 官方內建函式的規格簽章。

### 5.1 `print()` 函式解析與 `sep` / `end` 應用
官方定義簽章：
```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```
- `*objects`：允許傳入 0 個或任意多個位置引數。
- `sep` 與 `end`：出現在 `*objects` 後方，屬於**僅限關鍵字引數**，必須以 `名稱=值` 指定。

#### 程式碼範例 (`Cell 18-19`)
```python
print('a', 'b', 1, 67, 89)
# 輸出：a b 1 67 89

print('a', 'b', 1, 67, 89, sep='-')
# 輸出：a-b-1-67-89

print('a', 'b', 1, 67, 89, end='讚啦!\n')
# 輸出：a b 1 67 89讚啦!
```

---

### 5.2 `sorted()` 函式解析與 `reverse` 應用
官方定義簽章：
```python
sorted(iterable, /, *, key=None, reverse=False)
```
- `iterable`：在 `/` 左側，表示被排序的序列**只能用位置傳入**。
- `key` 與 `reverse`：在單獨 `*` 右側，屬於**僅限關鍵字引數**，欲反轉排序時必須明確寫出 `reverse=True`。

#### 程式碼範例 (`Cell 20-21`)
```python
result = sorted([8, 92, 63, 75], reverse=True)
# 輸出：[92, 75, 63, 8]
```

---

## 六、進階呼叫技巧：引數解包（Unpacking）

星號除了用於定義函式時「打包」，在**呼叫函式**時則代表「解包」：

1. **單星號 `*可迭代物件`**：解開串列（List）或元組（Tuple），將元素按位置依序傳入。
   ```python
   def add_three(a, b, c):
       return a + b + c

   numbers = [10, 20, 30]
   print(add_three(*numbers))  # 等同於 add_three(10, 20, 30) -> 輸出：60
   ```
2. **雙星號 `**字典`**：解開字典（Dictionary），將鍵值對以關鍵字引數傳入。
   ```python
   drink_order = {
       "drink": "珍珠奶茶",
       "ice": "少冰",
       "sugar": "微糖",
   }
   order_drink(**drink_order)  # 輸出：點餐：珍珠奶茶（少冰 / 微糖）
   ```

---

## 七、特殊符號速查對照表

| 符號 / 寫法 | 出現情境 | 角色與作用 | 典型範例 |
| :--- | :--- | :--- | :--- |
| `/` | `def` 宣告中 | 劃定分界：其**左邊**參數為**僅限位置**傳遞 | `def f(a, /):` |
| `*`（單獨） | `def` 宣告中 | 劃定分界：其**右邊**參數為**僅限關鍵字**傳遞 | `def f(*, b):` |
| `*args` | `def` 宣告中 | **打包**：將不定量的位置引數組裝成 `tuple` | `def f(*args):` |
| `**kwargs` | `def` 宣告中 | **打包**：將不定量的關鍵字引數組裝成 `dict` | `def f(**kwargs):` |
| `*iterable` | 函式呼叫時 | **解包**：將串列或元組解開為個別位置引數 | `f(*[1, 2])` |
| `**dict` | 函式呼叫時 | **解包**：將字典解開為 `key=value` 關鍵字引數 | `f(**{"a": 1})` |

---

## 八、常見錯誤與 Traceback 排除指南

| 錯誤類型 | 常見觸發情境 | 範例與診斷方式 | 修復對策 |
| :--- | :--- | :--- | :--- |
| `SyntaxError: positional argument follows keyword argument` | 呼叫時位置引數排在關鍵字引數後面 | `func(a=1, 2)` | 將位置引數全數移至前面，或統一改為關鍵字引數傳遞。 |
| `TypeError: ... got some positional-only arguments passed as keyword arguments` | 呼叫時對 `/` 左側的參數寫出名稱 | `calc_bmi(weight=65, height=1.75)` | 移除參數名稱，單純傳入數值 `calc_bmi(65, 1.75)`。 |
| `TypeError: ... takes X positional arguments but Y were given` | 對 `*` 右側的僅限關鍵字參數用位置傳入 | `send_email("a@b.com", "Title", True)` | 為該引數補上名稱：`send_email("a@b.com", subject="Title", urgent=True)`。 |
| `TypeError: ... got multiple values for argument` | 同一參數先用位置傳入，後續又以關鍵字指定 | `describe_pet("狗", animal="貓")` | 檢查引數對應，移除多餘的重複指派。 |

---

## 九、課堂自我檢測題（附詳解）

### 題目一：觀念辨析
觀察以下函式宣告：
```python
def setup_server(host, port=8080, /, timeout=30, *, secure=False, **options):
    pass
```
請問下列何者為**錯誤**的呼叫方式？
- (A) `setup_server("127.0.0.1", 9000, 60, secure=True)`
- (B) `setup_server("127.0.0.1", timeout=15, secure=True)`
- (C) `setup_server(host="127.0.0.1", port=8080, secure=True)`
- (D) `setup_server("127.0.0.1", 8080, timeout=10, secure=False, debug=True)`

> **詳解**：
> 正確答案為 **(C)**。
> 原因：`host` 與 `port` 位於 `/` 左側，屬於「僅限位置參數」，呼叫時絕對不能使用 `host=...` 或 `port=...` 的形式傳入，否則會丟出 `TypeError`。

---

### 題目二：程式追蹤
試推導下列程式碼的執行結果：
```python
def calculate(base, *values, scale=1):
    total = base + sum(values)
    return total * scale

data = [2, 3, 4]
print(calculate(10, *data, scale=2))
```

> **詳解**：
> 輸出為 **`38`**。
> 解析步驟：
> 1. `calculate` 接收到 `base = 10`。
> 2. `*data` 解包傳入 `2, 3, 4`，被 `*values` 打包為元組 `(2, 3, 4)`。
> 3. `total = 10 + sum((2, 3, 4)) = 10 + 9 = 19`。
> 4. 最後乘上 `scale=2`，結果為 `19 * 2 = 38`。

---

### 題目三：動手實作
請編寫一個名為 `log_message` 的函式，規格如下：
1. `level`（日誌等級）：僅限位置傳遞（如 `"INFO"`、`"ERROR"`）。
2. `message`（訊息內容）：位置或名稱皆可。
3. `timestamp`：僅限關鍵字傳遞，預設為 `"NOW"`。
4. `tags`：可接收任意數量的額外標籤關鍵字（如 `module="auth"`, `user_id=12`），以字典形式輸出。

#### 參考解答：
```python
def log_message(level, /, message, *, timestamp="NOW", **tags):
    print(f"[{timestamp}] [{level}] {message} | Tags: {tags}")

# 呼叫示範：
log_message("ERROR", "登入失敗", timestamp="2026-11-18 15:30", ip="192.168.1.1", retry=3)
# 輸出：[2026-11-18 15:30] [ERROR] 登入失敗 | Tags: {'ip': '192.168.1.1', 'retry': 3}
```
