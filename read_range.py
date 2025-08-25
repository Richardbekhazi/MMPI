import tkinter as tk
from tkinter import messagebox

# → map Excel columns K–T to Arabic letters
ARABIC_MAP = {
    'K': 'أ', 'L': 'ب', 'M': 'ج', 'N': 'ح',
    'O': 'د', 'P': 'ز', 'Q': 'ط', 'R': 'ه',
    'S': 'و', 'T': 'ي'
}

def parse_cellrefs(range_str):
    """
    Turn "K2:K3,K5,K7" into a list of (column, row) tuples:
    [('K',2), ('K',3), ('K',5), ('K',7)]
    """
    refs = []
    for part in range_str.split(','):
        part = part.strip().upper()
        if not part:
            continue
        if ':' in part:
            start, end = part.split(':')
            col1 = ''.join(filter(str.isalpha, start))
            row1 = int(''.join(filter(str.isdigit, start)))
            col2 = ''.join(filter(str.isalpha, end))
            row2 = int(''.join(filter(str.isdigit, end)))
            if col1 != col2:
                messagebox.showerror("Invalid range",
                                     f"Can’t span columns in one range: {part}")
                return []
            for r in range(row1, row2+1):
                refs.append((col1, r))
        else:
            col = ''.join(filter(str.isalpha, part))
            row = int(''.join(filter(str.isdigit, part)))
            refs.append((col, row))
    return refs

def convert_refs(refs):
    """
    Map each (col, row) to e.g. 'أ1' where
    letter = ARABIC_MAP[col]
    number = row - 1
    """
    out = []
    for col, row in refs:
        if col not in ARABIC_MAP:
            out.append(f"{col}{row} → (no mapping for column)")
            continue
        arabic = ARABIC_MAP[col]
        num = row - 1
        out.append(f"{arabic}{num}")
    return out

class RangeMapperGUI:
    def __init__(self, master):
        master.title("Excel-Range → Arabic Mapping")
        tk.Label(master, text="Enter Excel ranges:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.entry = tk.Entry(master, width=60)
        self.entry.grid(row=1, column=0, padx=4)
        tk.Button(master, text="Convert", command=self.on_convert).grid(row=1, column=1, padx=4)

        self.output = tk.Text(master, width=60, height=15)
        self.output.grid(row=2, column=0, columnspan=2, padx=4, pady=4)

        # New: count label
        self.count_var = tk.StringVar(value="Count: 0")
        tk.Label(master, textvariable=self.count_var).grid(row=3, column=0, sticky="w", padx=4, pady=(0,4))

    def on_convert(self):
        self.output.delete('1.0', tk.END)
        text = self.entry.get().strip()
        if not text:
            self.count_var.set("Count: 0")
            return
        refs = parse_cellrefs(text)
        if not refs:
            self.count_var.set("Count: 0")
            return
        mapped = convert_refs(refs)
        for line in mapped:
            self.output.insert(tk.END, line + "\n")
        # update count
        self.count_var.set(f"Count: {len(mapped)}")

if __name__ == "__main__":
    root = tk.Tk()
    RangeMapperGUI(root)
    root.mainloop()
