#### 安裝所需套件
`pip install -r requirements.txt`

#### 透過time套件來實作功能
- time.time(): 目前時間

#### 透過random套件來實作功能
- random.sample(): 產生不重複亂數

#### 透過multiprocessing套件來實作功能
- multiprocessing.freeze_support(): Windows 平台要使用此函數，避免 RuntimeError

- pool = multiprocessing.Pool(): 設定處理程序數量

- multiprocessing.cpu_count(): CPU核心數量

- pool.apply_async(): 異步處理

- pool.close(): 關閉進程池，不再接受新的進程

- pool.join(): 主進程阻塞等待子進程的退出
