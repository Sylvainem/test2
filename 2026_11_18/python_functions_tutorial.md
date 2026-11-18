# Python 函式呼叫與參數語法完全指南

> **課程日期**：2026-11-18  
> **適用對象**：Python 初學至進階學習者  
> **核心主題**：掌握函式的呼叫方式、位置引數、關鍵字引數，以及特殊符號（`/`、`*`、`*args`、`**kwargs`、解包）的精確語意與應用場景。

---

## 目錄

- [一、核心觀念：參數 (Parameter) vs 引數 (Argument)](#一核心觀念參數-parameter-vs-引數-argument)
- [二、呼叫函式的基礎方式](#二呼叫函式的基礎方式)
  - [2.1 位置引數 (Positional Arguments)](#21-位置引數-positional-arguments)
  - [2.2 關鍵字引數 (Keyword Arguments)](#22-關鍵字引數-keyword-arguments)
  - [2.3 混合使用規則與常見錯誤](#23-混合使用規則與常見錯誤)
  - [2.4 預設參數 (Default Arguments)](#24-預設參數-default-arguments)
- [三、特殊符號在「函式定義」中的意義：`/` 與 `*`](#三特殊符號在函式定義中的意義-與-)
  - [3.1 為什麼需要限制傳入方式？](#31-為什麼需要限制傳入方式)
  - [3.2 僅限位置參數：`/` (Positional-Only)](#32-僅限位置參數--positional-only)
  - [3.3 僅限關鍵字參數：`*` (Keyword-Only)](#33-僅限關鍵字參數--keyword-only)
  - [3.4 完整語法簽章對照表](#34-完整語法簽章對照表)
- [四、特殊符號在「函式定義」中的打包：`*args` 與 `**kwargs`](#四特殊符號在函式定義中的打包-args-與-kwargs)
  - [4.1 `*args`：收集多餘的位置引數](#41-args收集多餘的位置引數)
  - [4.2 `**kwargs`：收集多餘的關鍵字引數](#42-kwargs收集多餘的關鍵字引數)
  - [4.3 參數定義的標準排列順序](#43-參數定義的標準排列順序)
- [五、特殊符號在「函式呼叫」中的解包：`*` 與 `**`](#五特殊符號在函式呼叫中的解包-與-)
  - [5.1 `*iterable`：解包序列為位置引數](#51-iterable解包序列為位置引數)
  - [5.2 `**dict`：解包字典為關鍵字引數](#52-dict解包字典為關鍵字引數)
  - [5.3 定義打包 vs 呼叫解包對比](#53-定義打包-vs-呼叫解包對比)
- [六、常見陷阱與最佳實踐](#六常見陷阱與最佳實踐)
- [七、課堂自我檢測題（附詳解）](#七課堂自我檢測題附詳解)

---

## 一、核心觀念：參數 (Parameter) vs 引數 (Argument)

在深入各種進階語法前，先釐清兩個常被混淆的名詞：

```python
def greet(name, message):  # <--- 定義函式時宣告的變數稱為「參數 (Parameter)」
    print(f"{message}, {name}!")

greet("Alice", "Hello")    # <--- 呼叫函式時實際傳入的值稱為「引數 (Argument)」
```

- **參數 (Parameter / 形參)**：函式定義括號裡的變數名稱，相當於「等待接收資料的空位」。
- **引數 (Argument / 實參)**：呼叫函式時真正傳給函式的值或物件。

---

## 二、呼叫函式的基礎方式

### 2.1 位置引數 (Positional Arguments)

最直覺的呼叫方式，按照參數宣告的**前後順序**依序對應傳值。

```python
def introduce(name, age, city):
    print(f"大家好，我是 {name}，今年 {age} 歲，住在 {city}。")

# 依序對應：name="小明", age=20, city="台北"
introduce("小明", 20, "台北")

# 順序錯誤會導致語意錯亂甚至型態錯誤：
introduce(20, "小明", "台北")
# 輸出：大家好，我是 20，今年 小明 歲，住在 台北。
```

### 2.2 關鍵字引數 (Keyword Arguments)

呼叫時明確指定「**參數名稱 = 值**」。優點是不受順序限制，大幅提高代碼可讀性。

```python
def introduce(name, age, city):
    print(f"大家好，我是 {name}，今年 {age} 歲，住在 {city}。")

# 明確指定參數名稱，順序調換完全不受影響
introduce(age=20, city="台北", name="小明")
introduce(city="台中", name="小華", age=22)
```

### 2.3 混合使用規則與常見錯誤

位置引數與關鍵字引數可以混用，但必須遵循唯一鐵則：

> [!IMPORTANT]
> **規則：所有的「位置引數」必須寫在「關鍵字引數」的前面！**  
> 一旦開始使用關鍵字引數，其後面就不能再出現純位置引數。

```python
def introduce(name, age, city):
    print(f"大家好，我是 {name}，今年 {age} 歲，住在 {city}。")

# 正確：前面是位置引數，後面是關鍵字引數
introduce("小明", city="台北", age=20)

# 錯誤 1：位置引數出現在關鍵字引數後面
# introduce(name="小明", 20, city="台北")
# SyntaxError: positional argument follows keyword argument

# 錯誤 2：同一個參數被重覆賦值
# introduce("小明", 20, name="小華")
# TypeError: introduce() got multiple values for argument 'name'
```

### 2.4 預設參數 (Default Arguments)

在定義函式時給予參數初始值。呼叫時如果沒有提供該引數，會自動套用預設值。

```python
def connect_database(host, port=5432, timeout=30):
    print(f"連線至 {host}:{port}，逾時設定為 {timeout} 秒")

connect_database("localhost")                     # port=5432, timeout=30
connect_database("localhost", 3306)               # port=3306, timeout=30
connect_database("localhost", timeout=10)         # port=5432, timeout=10
```

---

## 三、特殊符號在「函式定義」中的意義：`/` 與 `*`

Python 3.8 正式引入了 `/` 語法，與原本既有的 `*` 搭配，讓開發者能嚴格規範呼叫端傳遞引數的方式。

### 3.1 為什麼需要限制傳入方式？

1. **API 穩定性**：如果未來的版本想要修改參數名稱，但外部使用者都使用關鍵字引數呼叫，修改名稱就會造成重大 Breaking Change。若強制使用位置傳入，參數名稱就只是內部實作細節。
2. **避免語意模糊**：例如函式需要兩個布林旗標 `process(True, False)`，讀代碼的人無法得知分別代表什麼，強制要求關鍵字傳入 `process(verbose=True, dry_run=False)` 能顯著提升可讀性。

---

### 3.2 僅限位置參數：`/` (Positional-Only)

在函式定義中，**位於 `/` 左側**的所有參數，都**只能**使用位置引數傳入，**絕對不能**使用關鍵字引數！

```python
def calculate_bmi(weight, height, /):
    return weight / ((height / 100) ** 2)

# 正確呼叫：純位置引數
bmi = calculate_bmi(70, 175)
print(f"BMI: {bmi:.2f}")

# 錯誤呼叫：使用了關鍵字引數
# calculate_bmi(weight=70, height=175)
# TypeError: calculate_bmi() got some positional-only arguments passed as keyword arguments: 'weight, height'
```

> [!NOTE]
> Python 許多內建函式底層都是 Positional-Only，例如 `len([1, 2, 3])`。你不能寫 `len(obj=[1, 2, 3])`，因為 `len` 的簽章就是 `len(obj, /)`。

---

### 3.3 僅限關鍵字參數：`*` (Keyword-Only)

在函式定義中，**位於單獨一個 `*` 右側**的所有參數，都**只能**使用關鍵字引數傳入，**絕對不能**使用位置引數！

```python
def create_user(username, *, is_admin=False, send_welcome_email=True):
    print(f"建立使用者：{username}")
    print(f"管理員權限：{is_admin}，寄送歡迎信：{send_welcome_email}")

# 正確呼叫：username 可用位置或關鍵字，但 is_admin 與 send_welcome_email 必須用關鍵字
create_user("john_doe", is_admin=True, send_welcome_email=False)
create_user(username="jane_doe", is_admin=False)

# 錯誤呼叫：嘗試用位置引數傳遞 * 右側的參數
# create_user("john_doe", True, False)
# TypeError: create_user() takes 1 positional argument but 3 were given
```

---

### 3.4 完整語法簽章對照表

當 `/` 與 `*` 同時出現在同一個函式定義中時，參數會被劃分為三個清晰的區間：

```python
def example(pos_only1, pos_only2, /, standard, *, kw_only1, kw_only2):
    pass
```

```
def example( a, b,  / ,   c   ,  *  ,  d, e ):
             ───────      ───          ────
                │          │            │
                │          │            └── 僅限關鍵字 (Keyword-Only)
                │          └─────────────── 位置或關鍵字皆可 (Positional or Keyword)
                └────────────────────────── 僅限位置 (Positional-Only)
```

| 參數區間 | 所在位置 | 允許傳入方式 |
| :--- | :--- | :--- |
| **僅限位置 (Positional-only)** | `/` 的左邊 | 只能使用**位置引數** |
| **標準參數 (Positional or Keyword)** | `/` 與 `*` 之間 | **位置引數** 或 **關鍵字引數** 皆可 |
| **僅限關鍵字 (Keyword-only)** | `*` 的右邊 | 只能使用**關鍵字引數** |

#### 綜合範例演練：

```python
def configure_server(ip, port, /, protocol="https", *, timeout=60, retry=3):
    print(f"連線資訊：{protocol}://{ip}:{port} (timeout={timeout}s, retry={retry}次)")

# 合法呼叫方式：
configure_server("192.168.1.1", 8080)
configure_server("192.168.1.1", 8080, "http", timeout=30, retry=5)
configure_server("192.168.1.1", 8080, protocol="http", retry=1)

# 非法呼叫方式 1：ip 或 port 用關鍵字傳入（被 / 限制）
# configure_server(ip="192.168.1.1", port=8080)  # TypeError!

# 非法呼叫方式 2：timeout 用位置傳入（被 * 限制）
# configure_server("192.168.1.1", 8080, "https", 30)  # TypeError!
```

---

## 四、特殊符號在「函式定義」中的打包：`*args` 與 `**kwargs`

當我們事先不知道呼叫者會傳入多少個引數時，可以在定義時使用 `*` 與 `**` 進行**動態打包 (Packing)**。

### 4.1 `*args`：收集多餘的位置引數

- 符號：參數名前加單星號 `*`（慣用名稱為 `args`，全名 arguments）。
- 行為：將傳入的所有多餘**位置引數**，打包成一個 **`tuple`（元組）**。

```python
def calculate_sum(*numbers):
    print(f"收到的資料型態：{type(numbers)}，內容：{numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

print(calculate_sum(1, 2, 3))       # numbers 會是 (1, 2, 3)，回傳 6
print(calculate_sum(10, 20, 30, 40)) # numbers 會是 (10, 20, 30, 40)，回傳 100
print(calculate_sum())               # numbers 會是 ()，回傳 0
```

> [!NOTE]
> 注意：`*args` 後面的所有具名參數，都會自動變成**僅限關鍵字參數 (Keyword-only)**，效果如同前面講的單獨 `*`！
> ```python
> def build_query(table, *columns, distinct=False):
>     # distinct 位於 *columns 之後，呼叫時必須使用 distinct=True 傳入！
>     pass
> ```

---

### 4.2 `**kwargs`：收集多餘的關鍵字引數

- 符號：參數名前加雙星號 `**`（慣用名稱為 `kwargs`，全名 keyword arguments）。
- 行為：將傳入的所有多餘**關鍵字引數**，打包成一個 **`dict`（字典）**。

```python
def print_user_profile(user_id, **details):
    print(f"使用者 ID: {user_id}")
    print(f"額外資料型態：{type(details)}，內容：{details}")
    for key, value in details.items():
        print(f"  - {key}: {value}")

print_user_profile(1001, name="Alice", role="Admin", email="alice@example.com")
# details 會是 {'name': 'Alice', 'role': 'Admin', 'email': 'alice@example.com'}
```

---

### 4.3 參數定義的標準排列順序

若一個函式同時包含多種類型的參數，Python 語法規定必須依照以下順序宣告，否則會出現 `SyntaxError`：

```
1. 僅限位置參數 (Positional-only)
2. 符號 /
3. 一般參數 (位置或關鍵字皆可，含預設值)
4. *args (或單獨一個 *)
5. 僅限關鍵字參數 (Keyword-only)
6. **kwargs
```

```python
def complete_function(a, b, /, c, d=0, *args, e, f=100, **kwargs):
    print(f"a={a}, b={b}, c={c}, d={d}")
    print(f"args={args}")
    print(f"e={e}, f={f}")
    print(f"kwargs={kwargs}")

complete_function(1, 2, 3, 4, 5, 6, e=99, bonus=500, status="active")
# a=1, b=2 (位置傳入，且受限於 /)
# c=3, d=4 (標準參數)
# args=(5, 6)
# e=99, f=100 (僅限關鍵字傳入，受限於 *args)
# kwargs={'bonus': 500, 'status': 'active'}
```

---

## 五、特殊符號在「函式呼叫」中的解包：`*` 與 `**`

當 `*` 和 `**` 用在**呼叫函式**時，意義與定義時完全相反——它們不是打包，而是**解包 (Unpacking)**！

### 5.1 `*iterable`：解包序列為位置引數

在 list、tuple、set、字串前加上 `*`，會將容器中的每個元素**拆解並作為獨立的位置引數**依序傳入函式。

```python
def calculate_area(width, height):
    return width * height

box_dimensions = [15, 20]

# 一般寫法：手動索引
# area = calculate_area(box_dimensions[0], box_dimensions[1])

# 使用 * 解包：等價於 calculate_area(15, 20)
area = calculate_area(*box_dimensions)
print("面積：", area)  # 300
```

### 5.2 `**dict`：解包字典為關鍵字引數

在字典 (dict) 前加上 `**`，會將字典中的每一組 `key: value` **拆解為 `key=value` 的關鍵字引數**傳入函式。

```python
def render_profile(name, age, city):
    print(f"姓名: {name}, 年齡: {age}, 城市: {city}")

user_info = {
    "name": "Bob",
    "age": 28,
    "city": "高雄"
}

# 使用 ** 解包：等價於 render_profile(name="Bob", age=28, city="高雄")
render_profile(**user_info)
```

> [!WARNING]
> 解包字典時，字典的 **Key 必須與函式參數名稱完全吻合**（包含數量與名稱），否則會觸發 `TypeError: got an unexpected keyword argument`。

---

### 5.3 定義打包 vs 呼叫解包對比

| 符號 | 用在「函式定義時」 (Packing 打包) | 用在「函式呼叫時」 (Unpacking 解包) |
| :---: | :--- | :--- |
| **`*`** | 將多個位置引數收集為一個 `tuple` (`*args`) | 將 `list` / `tuple` 拆解為獨立的位置引數傳入 |
| **`**`** | 將多個關鍵字引數收集為一個 `dict` (`**kwargs`) | 將 `dict` 拆解為獨立的關鍵字引數傳入 |

---

## 六、常見陷阱與最佳實踐

### 陷阱 1：可變物件 (Mutable) 當預設引數

**千萬不要在參數預設值中使用 `[]` 或 `{}`！**  
預設值只會在函式定義時建立一次，之後所有呼叫都會共用同一份記憶體物件：

```python
# 錯誤示範：
def add_task(task, task_list=[]):
    task_list.append(task)
    return task_list

print(add_task("寫程式"))   # ['寫程式']
print(add_task("讀講義"))   # ['寫程式', '讀講義'] <-- 驚！被前一次呼叫污染了！

# 正確寫法：以 None 作為哨兵值
def add_task(task, task_list=None):
    if task_list is None:
        task_list = []
    task_list.append(task)
    return task_list
```

### 最佳實踐準則

1. **布林旗標建議設為 Keyword-Only**：  
   `def query_data(sql, *, debug=False, use_cache=True):`  
   呼叫端寫 `query_data("SELECT...", debug=True)` 比 `query_data("SELECT...", True, False)` 清楚十倍。
2. **參數名稱不具業務意義時使用 Positional-Only**：  
   像 `math.sin(x, /)`，`x` 只是個單純數值，寫 `math.sin(x=3.14)` 毫無意義且徒增開銷。

---

## 七、課堂自我檢測題（附詳解）

### 觀念題 1：以下程式碼執行後會輸出什麼？

```python
def check_order(a, b=10, *, c=20):
    return a + b + c

# 試問下列哪一個呼叫會拋出錯誤？
# (A) check_order(5)
# (B) check_order(5, 15, c=30)
# (C) check_order(5, c=30)
# (D) check_order(5, 15, 30)
```

<details>
<summary>點擊查看答案與解析</summary>

**答案：(D)**  
**解析**：  
`c` 位於 `*` 右邊，是 **僅限關鍵字參數 (Keyword-only)**。(D) 嘗試以第三個位置引數傳值給 `c`，會拋出 `TypeError: check_order() takes from 1 to 2 positional arguments but 3 were given`。  
(A) 為合法呼叫，使用預設值 `b=10, c=20`，結果為 35。  
(B) 與 (C) 也均為合法呼叫。
</details>

---

### 觀念題 2：判斷程式碼是否合法

```python
def test_func(x, /, y, *, z):
    return x * y * z

result = test_func(2, y=3, z=4)
```

<details>
<summary>點擊查看答案與解析</summary>

**答案：合法**  
**解析**：  
- `x` 在 `/` 左邊，必須用位置引數傳入（呼叫端傳入 `2`，符合規定）。
- `y` 在 `/` 與 `*` 之間，是標準參數，可用位置或關鍵字傳入（呼叫端傳入 `y=3`，符合規定）。
- `z` 在 `*` 右邊，必須用關鍵字引數傳入（呼叫端傳入 `z=4`，符合規定）。  
最終回傳 `2 * 3 * 4 = 24`。
</details>

---

### 實作題 3：綜合解包練習

給定以下函式與資料：

```python
def send_email(to, subject, body, *, priority="Normal", retry_count=3):
    print(f"寄給: {to} | 主旨: {subject} | 重要度: {priority} | 重試: {retry_count}")

basic_info = ["boss@company.com", "專案進度報告", "今日已完成函式講義撰寫。"]
settings = {"priority": "High", "retry_count": 5}
```

請使用**解包運算子**，以一行程式碼呼叫 `send_email`，將 `basic_info` 作為前三個引數，`settings` 作為設定值傳入。

<details>
<summary>點擊查看答案與解析</summary>

**答案**：
```python
send_email(*basic_info, **settings)
```

**解析**：  
- `*basic_info` 解包前三個元素，分別填入 `to`、`subject`、`body`。  
- `**settings` 解包字典，將鍵值對以 `priority="High", retry_count=5` 形式作為關鍵字引數傳入。
</details>
