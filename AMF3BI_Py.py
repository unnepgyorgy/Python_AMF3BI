import sys
import math
import random
import tkinter as tk
from tkinter import messagebox
import modul_AMF3BI

# Kötelező saját függvény az osztályon kívül a statisztikai számításokhoz
def statisztikaosszegzes_amf3bi(book_list):
    if not book_list:
        return 0, 0.0, 0
    ossz_db = sum(book["menny"] for book in book_list)
    ossz_ertek = sum(book["ara"] * book["menny"] for book in book_list)
    atlag_ar = ossz_ertek / ossz_db if ossz_db > 0 else 0.0
    return ossz_db, atlag_ar, ossz_ertek

class BookAppAMF3BI:
    def __init__(self, root):
        self.root = root
        self.root.title("Házi könyvtáram Python - AMF3BI")
        self.root.geometry("580x420") 
        self.backend = modul_AMF3BI.KonyvRegiszterAMF3BI()
       
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10, padx=10, fill=tk.X)
        tk.Label(input_frame, text="Cím: ").pack(side=tk.LEFT, padx=2)
        self.mezo_cime = tk.Entry(input_frame, width=18)
        self.mezo_cime.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text="Ára: ").pack(side=tk.LEFT, padx=2)
        self.mezo_ar = tk.Entry(input_frame, width=10)
        self.mezo_ar.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text="Db: ").pack(side=tk.LEFT, padx=2)
        self.mezo_menny = tk.Entry(input_frame, width=6)
        self.mezo_menny.pack(side=tk.LEFT, padx=5)

        self.beszurgomb = tk.Button(input_frame, text="Hozzáad", command=self.uj_konyv)
        self.beszurgomb.pack(side=tk.LEFT, padx=10)
        self.listbox = tk.Listbox(root, width=70, height=12, font=("Courier", 10))
        self.listbox.pack(pady=10)
       
        self.statisztika_gomb = tk.Button(root, text="Házi könyvtáram (AMF3BI)", command=self.statisztikak)
        self.statisztika_gomb.pack(pady=5)
       
        self.infogomb = tk.Button(root, text="Rendszerinfo", command=self.rendszerinfo)
        self.infogomb.pack(pady=5)

        self.load_listbox()

    def load_listbox(self):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, "CÍM                            | ÁRA        | Darabszám")
        self.listbox.insert(tk.END, "-" * 60)
        for konyv in self.backend.mindenkonyv_amf3bi():
            row_text = f"{konyv['cime']:<30} | {konyv['ara']:<10} | {konyv['menny']}"
            self.listbox.insert(tk.END, row_text)
    
    def uj_konyv(self):
        s_konyvcim = self.mezo_cime.get().strip()
        s_konyvar = self.mezo_ar.get().strip()
        s_menny = self.mezo_menny.get().strip()
        
        if not s_konyvar.isdigit() or not s_menny.isdigit():
            messagebox.showerror("Figyelem!!!", "Ár és mennyiség nem numerikus!")
            return
            
        int_ara = int(s_konyvar)
        int_menny = int(s_menny)
        
        if self.backend.uj_konyv_amf3bi(s_konyvcim, int_ara, int_menny):
            self.load_listbox()
            self.mezo_cime.delete(0, tk.END)
            self.mezo_ar.delete(0, tk.END)
            self.mezo_menny.delete(0, tk.END)
        else:
            messagebox.showwarning("Figyelem!", "Nincs üres című könyv !!!")

    def statisztikak(self):
        mindenkonyv = self.backend.mindenkonyv_amf3bi()
        dbszam, atlagertek, teljesertek = statisztikaosszegzes_amf3bi(mindenkonyv)
        v_szam = random.randint(1, 1000)
        gyok = math.sqrt(v_szam)                 
        factrandom = random.randint(1, 10)
        faktorialis = math.factorial(factrandom) 
        hatvany = math.pow(2, 3)
        
        info_text = (
            f"--- KÉRT STATISZTIKÁK ---\n"
            f"Összes könyv darabszáma: {dbszam} db\n"
            f"Átlagos könyv ár: {atlagertek:.2f} HUF\n"
            f"Könyvek teljes értéke: {teljesertek} HUF\n\n"
            f"--- MATH MODUL DEMO ---\n"
            f"Véletlen azám: {v_szam}\n"
            f"math.sqrt(): {gyok:.2f}\n"
            f"math.factorial({factrandom}): {faktorialis}\n"
            f"math.pow(2, 3): {hatvany}"
        )
        messagebox.showinfo("Könyvek összesítése", info_text)

    def rendszerinfo(self):
        info_text = f"Platform: {sys.platform}\nVersion: {sys.version}"
        messagebox.showinfo("System Info", info_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookAppAMF3BI(root)
    root.mainloop()