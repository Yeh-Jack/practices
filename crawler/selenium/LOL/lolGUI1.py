import tkinter as tk
from tkinter import ttk, messagebox
import MySQLdb
from PIL import Image, ImageTk
import io
import pandas as pd

# 您的資料庫連線資訊
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "12345678",
    "database": "testdb",
    "port": 3307,
    "charset": "utf8"
}

# 全域變數，用於儲存從資料庫讀取的資料
all_hero_data = pd.DataFrame()
category_map = {} # 儲存 {類別名稱: ID}

def load_data_from_db():
    """從資料庫讀取 herodata 和 herocategory 的所有資料"""
    global all_hero_data, category_map
    
    try:
        conn = MySQLdb.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # 1. 讀取英雄資料 (herodata)
        # 注意：使用 SELECT * 會將 BLOB 資料讀取出來
        sql_hero = "SELECT name, category_id, img FROM herodata"
        cursor.execute(sql_hero)
        hero_results = cursor.fetchall()
        all_hero_data = pd.DataFrame(hero_results, columns=['name', 'category_id', 'img'])
        
        # 2. 讀取英雄類別 (herocategory)
        sql_category = "SELECT id, category FROM herocategory"
        cursor.execute(sql_category)
        category_results = cursor.fetchall()
        
        # 建立類別對應字典 {ID: Name} 和 {Name: ID}
        category_name_id = {row[1]: row[0] for row in category_results}
        category_map = category_name_id
        
        conn.close()
        return True
        
    except Exception as e:
        messagebox.showerror("資料庫錯誤", f"無法連接或讀取資料庫：{e}")
        return False

# --- Tkinter 視窗函式 ---

def show_hero_image(hero_name, img_binary):
    """在新的頂層視窗中顯示英雄圖片"""
    
    # 創建新的頂層視窗
    img_window = tk.Toplevel(root)
    img_window.title(f"英雄圖片：{hero_name}")
    
    try:
        # 將二進制數據流轉換為 PIL Image 物件
        image_stream = io.BytesIO(img_binary)
        pil_image = Image.open(image_stream)
        
        # 調整圖片大小以適應視窗 (可選)
        max_size = (400, 400)
        pil_image.thumbnail(max_size)
        
        # 轉換為 Tkinter 圖片格式
        tk_image = ImageTk.PhotoImage(pil_image)
        
        # 顯示圖片
        img_label = tk.Label(img_window, image=tk_image)
        img_label.image = tk_image # 保持引用，防止垃圾回收
        img_label.pack(padx=20, pady=20)
        
    except Exception as e:
        messagebox.showerror("圖片錯誤", f"無法顯示圖片：{e}")

def update_hero_buttons(event=None):
    """根據下拉式選單的選擇，更新英雄按鈕"""
    
    # 1. 取得選定的類別名稱
    selected_category_name = category_combobox.get()
    
    # 2. 移除舊的按鈕
    for widget in hero_frame.winfo_children():
        widget.destroy()
        
    if not selected_category_name:
        return
        
    # 3. 根據名稱查找類別 ID
    category_id = category_map.get(selected_category_name)
    
    if category_id is None:
        return
    
    # 4. 過濾出該類別的英雄數據
    filtered_heroes = all_hero_data[all_hero_data['category_id'] == category_id]
    
    # 5. 生成新的英雄按鈕
    if filtered_heroes.empty:
        tk.Label(hero_frame, text="此類別沒有英雄資料。", padx=10, pady=10).pack()
    else:
        # 英雄按鈕排列，例如每行 4 個
        col_count = 4
        for i, row in filtered_heroes.iterrows():
            hero_name = row['name']
            img_binary = row['img']
            
            # 使用 lambda 函式將參數傳遞給點擊事件
            btn = tk.Button(
                hero_frame, 
                text=hero_name, 
                width=10, 
                command=lambda name=hero_name, img=img_binary: show_hero_image(name, img)
            )
            # 使用 grid 進行排列
            btn.grid(row=i // col_count, column=i % col_count, padx=5, pady=5)


# --- 主程式 ---

if __name__ == "__main__":
    if not load_data_from_db():
        # 如果資料庫載入失敗，則不啟動 GUI
        exit()

    root = tk.Tk()
    root.title("英雄聯盟資料瀏覽器")

    # 1. 類別選擇區域
    category_label = tk.Label(root, text="選擇英雄類別:", font=('Arial', 12))
    category_label.pack(pady=(10, 5))
    
    # 取得所有類別名稱
    category_names = sorted(list(category_map.keys()))
    
    category_combobox = ttk.Combobox(root, values=category_names, state="readonly", width=25)
    category_combobox.pack(padx=10, pady=5)
    
    # 綁定選單選擇事件
    category_combobox.bind("<<ComboboxSelected>>", update_hero_buttons)

    # 2. 英雄按鈕顯示區域
    tk.Label(root, text="--- 英雄列表 ---", font=('Arial', 12)).pack(pady=10)
    
    # 創建一個 Frame 來容納動態生成的英雄按鈕
    hero_frame = tk.Frame(root)
    hero_frame.pack(padx=10, pady=10)

    # 如果有類別，預設選擇第一個
    if category_names:
        category_combobox.set(category_names[0])
        update_hero_buttons()
    
    root.mainloop()