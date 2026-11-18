# Python 函式呼叫（Function Call）：一步一步練習

這份教材會帶你認識 Python 呼叫函式（Function）的各種方式，並看懂在函式說明或定義中常見的特殊符號：`/`、`*`、`*args`、`**kwargs`。請打開 VS Code 或終端機，跟著每個步驟實際執行範例看看結果。

## 前置觀念：參數（Parameter）與引數（Argument）

在開始之前，先釐清兩個常一起出現的名詞：

- **參數（Parameter）**：**定義函式**時，寫在 `def 函式名稱(...)` 括號裡的變數名稱（像空白表格上的欄位名稱）。
- **引數（Argument）**：**呼叫函式**時，實際填進括號裡的資料值（像真正填入表格的內容）。

```python
# 定義函式時，括號裡的 name 是「參數」(Parameter)
def greet(name):
    print(f"哈囉，{name}！")

# 呼叫函式時，實際傳進去的 "小明" 是「引數」(Argument)
greet("小明")
```

---

## 第 1 步：依「引數位置」呼叫（Positional Arguments）

最常見的呼叫方式，就是直接把值放進括號裡。Python 會依照呼叫時排列的**先後順序**，從左到右一對一對應到函式定義的參數位置：

```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

describe_pet("貓", "小橘")   # 輸出：我養了一隻貓，牠叫做小橘。
describe_pet("小橘", "貓")   # 位置對調了：我養了一隻小橘，牠叫做貓。
```

- 第 1 個引數 `"貓"` 會對應到第 1 個參數 `animal`。
- 第 2 個引數 `"小橘"` 會對應到第 2 個參數 `name`。
- 使用位置引數時，**順序錯了結果就會跟著錯**；如果少傳或多傳引數，Python 會回報 `TypeError`：

```python
# describe_pet("貓")             # TypeError: 少傳了 1 個必要的位置引數 name
# describe_pet("貓", "小橘", 3)  # TypeError: 只接收 2 個位置引數，卻傳了 3 個
```

---

## 第 2 步：依「引數名稱」呼叫（Keyword Arguments）與預設值

當函式的參數比較多、不容易記住順序時，可以在呼叫時直接寫出 **`參數名稱=值`**，這種方式稱為**引數名稱呼叫**（或**關鍵字引數**）：

```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

describe_pet(animal="貓", name="小橘")
describe_pet(name="小橘", animal="貓")  # 順序對調也完全正確！
```

- **不必死記順序**：只要名稱寫對，順序可以自由調整。
- **可讀性高**：看呼叫的地方就知道每個值代表什麼意思。

### 重要規則：混用時「位置引數」一定要在前面

位置引數和引數名稱可以混用，但**位置引數必須放在引數名稱的前面**，否則會直接出現語法錯誤（`SyntaxError`）：

```python
# 正確：先傳位置引數，再傳引數名稱
describe_pet("狗", name="旺財")

# 錯誤：位置引數不能跟在引數名稱後面
# describe_pet(animal="狗", "旺財")
# SyntaxError: positional argument follows keyword argument

# 錯誤：同一個參數不可同時用位置與名稱重複指定
# describe_pet("狗", animal="貓")
# TypeError: describe_pet() got multiple values for argument 'animal'
```

### 搭配預設值（Default Arguments）

定義函式時，如果有幫參數設定預設值，呼叫時就能只改自己想調整的項目：

```python
def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"點餐：{drink}（{ice} / {sugar}）")

order_drink("紅茶")                       # 點餐：紅茶（正常冰 / 半糖）
order_drink("紅茶", "去冰")               # 點餐：紅茶（去冰 / 半糖）
order_drink("紅茶", sugar="無糖")         # 跳過 ice，直接指定 sugar：點餐：紅茶（正常冰 / 無糖）
order_drink("綠茶", sugar="微糖", ice="少冰")  # 點餐：綠茶（少冰 / 微糖）
```

> 定義函式時，沒有預設值的參數（如 `drink`）必須寫在有預設值的參數（如 `ice`、`sugar`）前面。

---

## 第 3 步：特殊符號 `/` 與 `*` —— 限制引數的呼叫方式

在 VS Code 的函式提示或 Python `help()` 說明中，經常會看到參數列表裡單獨出現 `/` 或 `*`。它們本身**不是參數**，而是用來**限制呼叫者該怎麼傳入引數**的分隔符號。

### 1. `/`（僅限位置引數 Positional-Only）

寫在 `/` **左邊**的所有參數，呼叫時**只能依位置傳入**，**不能寫出引數名稱**：

```python
def calc_bmi(weight, height, /):
    bmi = weight / (height ** 2)
    print(f"BMI 為：{bmi:.1f}")

calc_bmi(65, 1.75)                  # 正確：依位置傳入
# calc_bmi(weight=65, height=1.75)  # 錯誤：weight 與 height 在 / 左邊，不能寫名稱
```

若硬寫名稱，會發生 `TypeError`（表示有人把僅限位置的參數當成關鍵字引數傳入了）。

- **為什麼需要 `/`？** 當參數名稱未來可能會改名（例如把 `x` 改成 `value`），或位置本身就夠直覺時，加上 `/` 可以避免呼叫端寫死參數名稱，保持彈性。

### 2. `*`（僅限關鍵字引數 Keyword-Only）

寫在單獨一個 `*` **右邊**的所有參數，呼叫時**必須寫出引數名稱**，**不能只靠位置傳入**：

```python
def send_email(to, *, subject, urgent=False):
    print(f"寄給：{to}｜主旨：{subject}｜急件：{urgent}")

send_email("student@example.com", subject="課堂通知", urgent=True)  # 正確
send_email("student@example.com", subject="作業提醒")               # 正確（urgent 使用預設值）

# 錯誤：subject 和 urgent 在 * 右邊，不能用位置傳入
# send_email("student@example.com", "課堂通知", True)
```

- **為什麼需要 `*`？** 像 `urgent=True` 這種布林開關或進階選項，如果只寫 `send_email("...", "...", True)`，別人看程式碼時根本不知道 `True` 是什麼意思。加上 `*` 強迫寫出 `urgent=True`，能大幅減少傳錯欄位的機會。

### 3. `/` 與 `*` 同時使用的切分規則

把兩者合在一起看，可以把函式的參數分成三個區域：

```text
def 函式名稱( 僅限位置參數 , / , 位置或名稱皆可 , * , 僅限引數名稱 ):
```

實際範例：

```python
def register(id_no, /, name, *, role="student"):
    print(f"編號：{id_no}｜姓名：{name}｜身分：{role}")

# 合法的呼叫方式
register("A01", "小明", role="leader")       # id_no 用位置；name 用位置；role 用名稱
register("A01", name="小明", role="leader")  # id_no 用位置；name 用名稱；role 用名稱
register("A01", "小明")                      # role 使用預設值

# 不合法的呼叫方式（皆會觸發 TypeError）
# register(id_no="A01", name="小明")         # 錯誤：id_no 在 / 左邊，只能用位置
# register("A01", "小明", "leader")          # 錯誤：role 在 * 右邊，必須寫名稱
```

---

## 第 4 步：`*args` 與 `**kwargs` —— 定義函式時接收任意數量的引數（打包 Packing）

有時候設計函式時，並不知道使用者會傳入幾個引數（例如計算任意個數字的總和，或接收額外的設定欄位）。這時候可以在定義函式時，在參數前面加上 `*` 或 `**`，把多出來的引數「打包」起來。

### 1. `*args`（一個星號）：把多餘的「位置引數」打包成 `tuple`

```python
def sum_scores(*scores):
    print("收到的資料：", scores, type(scores))
    return sum(scores)

print(sum_scores(80, 90, 85))
print(sum_scores(100))
print(sum_scores())
```

執行輸出：

```text
收到的資料： (80, 90, 85) <class 'tuple'>
255
收到的資料： (100,) <class 'tuple'>
100
收到的資料： () <class 'tuple'>
0
```

- 呼叫時傳入的 0 個、1 個或多個**位置引數**，都會被打包進一個 `tuple`（元組）。
- `args` 只是慣用的變數名稱（arguments 的縮寫），真正發揮作用的是前面的 **`*`**；像上面寫成 `*scores` 一樣能運作。

### 2. `**kwargs`（兩個星號）：把多餘的「引數名稱」打包成 `dict`

```python
def build_profile(name, **info):
    print("姓名：", name)
    print("其他資料：", info, type(info))

build_profile("小華", city="台北", course="Python")
```

執行輸出：

```text
姓名： 小華
其他資料： {'city': '台北', 'course': 'Python'} <class 'dict'>
```

- 呼叫時傳入的額外**關鍵字引數（`key=value`）**，都會被打包進一個 `dict`（字典）。
- 同樣地，`kwargs` 只是慣用命名（keyword arguments 的縮寫），真正發揮作用的是前面的 **`**`**。

### 3. 同時混用多種參數時的標準順序

如果在同一個函式裡同時使用各種參數，必須依照以下順序定義：

```python
def demo(a, /, b, *args, c, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

demo(1, 2, 3, 4, c=5, x=10, y=20)
# 輸出：a=1, b=2, args=(3, 4), c=5, kwargs={'x': 10, 'y': 20}
```

> [!TIP]
> 注意到了嗎？`c` 寫在 `*args` 的後面，因為多餘的位置引數都會被 `*args` 吸走，所以 `c` 自動變成**僅限關鍵字引數**（呼叫時一定要寫 `c=...`），不用在 `*args` 後面再多寫一個單獨的 `*`。

---

## 第 5 步：呼叫函式時的 `*` 與 `**` —— 把資料拆開傳入（拆解 Unpacking）

前面第 4 步是在**定義函式**時把多餘的引數「打包」起來；反過來，如果資料已經裝在 `list`、`tuple` 或 `dict` 裡，我們也可以在**呼叫函式**時加上 `*` 或 `**`，把它們「拆開」傳進去！

### 1. 呼叫時用 `*` 拆解 `list` / `tuple` 成位置引數

```python
def add_three(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

# 如果直接寫 add_three(numbers) 會報錯，因為整個 list 只算 1 個引數
# 加上 * 之後，會把 list 拆開成 3 個位置引數：等同於 add_three(10, 20, 30)
print(add_three(*numbers))  # 輸出：60
```

### 2. 呼叫時用 `**` 拆解 `dict` 成引數名稱

```python
def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"點餐：{drink}（{ice} / {sugar}）")

my_order = {
    "drink": "珍珠奶茶",
    "ice": "少冰",
    "sugar": "微糖",
}

# 加上 ** 之後，會把字典拆開成：order_drink(drink="珍珠奶茶", ice="少冰", sugar="微糖")
order_drink(**my_order)
```

> 使用 `**字典` 拆解傳入時，字典的鍵（key）名稱必須與函式參數名稱相符（除非函式本身有 `**kwargs` 可以接收多餘的鍵值）。

---

## 第 6 步：實戰解讀 Python 內建函式與符號總整理

學會以上規則後，現在你可以直接看懂 Python 官方文件或 VS Code 彈出的函式提示了！試著看這兩個最常用的內建函式：

### 實戰 1：`print(*objects, sep=' ', end='\n', file=None, flush=False)`

1. **`*objects`**：表示 `print()` 可以接收任意數量的位置引數（所以 `print("A", "B", "C")` 可以印好幾個值）。
2. **`sep=' '`、`end='\n'` 在 `*objects` 後面**：它們是僅限關鍵字引數，所以想改變分隔字元或結尾符號時，**必須寫名稱**，例如 `print("A", "B", sep="-", end="!\n")`。

### 實戰 2：`sorted(iterable, /, *, key=None, reverse=False)`

1. **`iterable` 在 `/` 左邊**：只能依位置傳入（例如 `sorted([3, 1, 2])`），不能寫 `sorted(iterable=[3, 1, 2])`。
2. **`key` 與 `reverse` 在 `*` 右邊**：必須寫出引數名稱（例如 `sorted([3, 1, 2], reverse=True)`），不能寫成 `sorted([3, 1, 2], True)`。

### 特殊符號速查總表

| 符號 / 寫法 | 出現位置 | 代表意思與規則 | 範例 |
| :--- | :--- | :--- | :--- |
| `/` | 定義函式 `def` | `/` **左邊**的參數僅限用**位置**傳入 | `def f(a, /):` → `f(1)` |
| `*`（單獨一個） | 定義函式 `def` | `*` **右邊**的參數必須寫**引數名稱** | `def f(*, b):` → `f(b=2)` |
| `*args` | 定義函式 `def` | 接收任意數量**位置引數**，打包成 `tuple` | `def f(*args):` |
| `**kwargs` | 定義函式 `def` | 接收任意數量**關鍵字引數**，打包成 `dict` | `def f(**kwargs):` |
| `*序列` | 呼叫函式時 | 把 `list` / `tuple` **拆解**成多個位置引數 | `f(*[1, 2])` → `f(1, 2)` |
| `**字典` | 呼叫函式時 | 把 `dict` **拆解**成多個 `key=value` 引數名稱 | `f(**{"b": 2})` → `f(b=2)` |

---

## 練習題

請先自己動手寫寫看，再對照下方提示檢查：

1. 有一個函式 `def make_coffee(beans, milk="全脂鮮奶", sugar=0):`。請練習用以下兩種方式呼叫它：
   - 全部用**位置引數**點一杯 `"義式深焙"`、`"燕麥奶"`、糖度 `1`。
   - 保留預設牛奶，只把糖度改為 `2`（請使用**位置引數 + 引數名稱**混用）。
2. 觀察下方函式定義，判斷哪幾行呼叫會出錯，並試著修改為正確的呼叫方式：
   ```python
   def create_ticket(event, /, seat, *, price, vip=False):
       print(event, seat, price, vip)

   create_ticket("Python 年會", "A12", price=1200)
   create_ticket(event="Python 年會", seat="A12", price=1200)
   create_ticket("Python 年會", "A12", 1200, True)
   ```
3. 寫一個函式 `average_score(*scores)`，可以傳入任意多個成績並印出平均分數（若沒有傳入任何成績，則印出 `"尚無成績"`）。
4. 已有資料 `data = {"title": "Python 講座", "room": "301"}` 與函式 `def announce(title, room, time="14:00"):`，請用 `**` 拆解 `data` 來呼叫 `announce`，並同時把 `time` 改為 `"10:00"`。

提示：

```python
# 第 3 題提示：先檢查 if len(scores) == 0: ...，再用 sum(scores) / len(scores)
# 第 4 題提示：呼叫時可以寫 announce(**data, time="10:00")
```

---

## 常見問題

- **`SyntaxError: positional argument follows keyword argument`**
  呼叫時把位置引數寫在引數名稱後面了（例如 `func(a=1, 2)`）。請把所有位置引數移到引數名稱之前，或全部改寫成引數名稱。
- **`TypeError: ... got some positional-only arguments passed as keyword arguments`**
  你幫寫在 `/` 左邊的參數加上了引數名稱。請改回直接依位置傳入值，不要寫 `參數名=`。
- **`TypeError: ... takes X positional arguments but Y were given`**
  多半是因為不小心把寫在 `*` 右邊（僅限關鍵字）的參數用位置傳入了，或是真的多傳了引數。請為 `*` 右邊的參數補上 `參數名=`。
- **`TypeError: ... got multiple values for argument '...'`**
  同一個參數同時被位置引數和引數名稱各指定了一次（例如 `describe_pet("狗", animal="貓")`）。請檢查並移除重複指定的引數。

---

## 完成檢查

- [ ] 能說出參數（Parameter）與引數（Argument）的差別。
- [ ] 能用位置引數、引數名稱（含混用順序）與預設值正確呼叫函式。
- [ ] 能分辨 `/` 左邊與 `*` 右邊的參數在呼叫時有什麼限制。
- [ ] 能區分 `*` / `**` 在「定義函式（打包成 `tuple` / `dict`）」與「呼叫函式（拆解傳入）」時的不同用法。
- [ ] 能看懂 `print(*objects, sep=' ', end='\n')` 與 `sorted(iterable, /, *, key=None, reverse=False)` 的呼叫規則。
