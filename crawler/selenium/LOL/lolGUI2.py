import customtkinter as ctk
import MySQLdb
from PIL import Image, ImageTk
import io
import pandas as pd
from tkinter import messagebox

# 設定全域主題
ctk.set_appearance_mode("Dark")  # 可選 "Light" 或 "Dark"
ctk.set_default_color_theme("blue") # 可選 "blue", "green", "dark-blue"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "12345678",
    "database": "testdb",
    "port": 3307,
    "charset": "utf8"
}

class ModernHeroBrowser(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LoL 英雄數據中心")
        self.geometry("1000x700")

        # 資料儲存
        self.all_hero_data = pd.DataFrame()
        self.category_map = {}
        
        # 佈局配置
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 建立 UI 元件
        self.setup_sidebar()
        self.setup_main_content()

        # 載入資料
        if self.load_data():
            self.refresh_sidebar()

    def load_data(self):
        try:
            conn = MySQLdb.connect(**DB_CONFIG)
            df_cat = pd.read_sql("SELECT id, category FROM herocategory", conn)
            self.category_map = dict(zip(df_cat['category'], df_cat['id']))
            self.all_hero_data = pd.read_sql("SELECT name, category_id, img FROM herodata", conn)
            conn.close()
            return True
        except Exception as e:
            messagebox.showerror("資料庫連線失敗", str(e))
            return False

    def setup_sidebar(self):
        """左側導覽列"""
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="LOL 英雄庫", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.label_cat = ctk.CTkLabel(self.sidebar_frame, text="選擇英雄類別:", anchor="w")
        self.label_cat.grid(row=1, column=0, padx=20, pady=(10, 0))

        self.cat_menu = ctk.CTkOptionMenu(self.sidebar_frame, command=self.display_heroes)
        self.cat_menu.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="主題模式:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

    def setup_main_content(self):
        """右側英雄顯示區"""
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="英雄清單", label_font=("Microsoft JhengHei", 16, "bold"))
        self.scroll_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def refresh_sidebar(self):
        names = sorted(list(self.category_map.keys()))
        if names:
            self.cat_menu.configure(values=names)
            self.cat_menu.set(names[0])
            self.display_heroes(names[0])

    def display_heroes(self, category_name):
        # 清除現有按鈕
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        cat_id = self.category_map.get(category_name)
        filtered = self.all_hero_data[self.all_hero_data['category_id'] == cat_id]

        for idx, row in enumerate(filtered.itertuples()):
            # 建立具備卡片感的按鈕
            btn = ctk.CTkButton(
                self.scroll_frame, 
                text=row.name,
                font=("Microsoft JhengHei", 14),
                height=60,
                corner_radius=10,
                fg_color="#3B3B3B",  # 深灰色卡片感
                hover_color="#505050",
                command=lambda r=row: self.open_image(r.name, r.img)
            )
            btn.grid(row=idx // 4, column=idx % 4, padx=10, pady=10, sticky="ew")

    def open_image(self, name, binary):
        if not binary: return
        
        # 彈出視窗美化
        top = ctk.CTkToplevel(self)
        top.title(f"英雄檔案 - {name}")
        top.attributes("-topmost", True) # 確保視窗在最上層
        
        try:
            img_data = Image.open(io.BytesIO(binary))
            # 使用 CTkImage 處理高解析度縮放
            ctk_img = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(400, 400))
            
            img_label = ctk.CTkLabel(top, image=ctk_img, text="")
            img_label.pack(padx=30, pady=20)
            
            name_label = ctk.CTkLabel(top, text=name, font=("Microsoft JhengHei", 24, "bold"))
            name_label.pack(pady=(0, 20))
        except:
            pass

    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = ModernHeroBrowser()
    app.mainloop()