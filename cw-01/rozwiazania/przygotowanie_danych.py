# Cw 2 - przygotowanie danych wine
# wejscie: ../zadania/Wine_data_prep.xlsx
# wynik: Wine_data_clean.xlsx + Wine_data_clean.csv

from pathlib import Path
import numpy as np
import pandas as pd

folder = Path(__file__).resolve().parent
wejscie = folder.parent / "zadania" / "Wine_data_prep.xlsx"
wyjscie_xlsx = folder / "Wine_data_clean.xlsx"
wyjscie_csv = folder / "Wine_data_clean.csv"

df = pd.read_excel(wejscie)

# byly spacje w nazwach kolumn (np. "Alcohol ", " Mg")
df.columns = [str(c).strip() for c in df.columns]

# niektore liczby byly jako tekst: "5,1", "3,22", litera "o" zamiast 0
for kol in df.columns:
    for i in range(len(df)):
        v = df.at[i, kol]
        if isinstance(v, str):
            v = v.strip()
            if v.lower() == "o":
                df.at[i, kol] = 0
            else:
                df.at[i, kol] = float(v.replace(",", "."))

for kol in df.columns:
    df[kol] = pd.to_numeric(df[kol], errors="coerce")

# puste komorki uzupelniam srednia z wiersza wyzej i nizej
for kol in df.columns:
    puste = df.index[df[kol].isna()].tolist()
    for i in puste:
        gora = None
        dol = None
        for j in range(i - 1, -1, -1):
            if pd.notna(df.at[j, kol]):
                gora = float(df.at[j, kol])
                break
        for j in range(i + 1, len(df)):
            if pd.notna(df.at[j, kol]):
                dol = float(df.at[j, kol])
                break
        if gora is not None and dol is not None:
            val = (gora + dol) / 2
        elif gora is not None:
            val = gora
        else:
            val = dol
        if kol == "Wine":
            val = int(round(val))
        else:
            val = round(val, 3)
        df.at[i, kol] = val

df["Wine"] = df["Wine"].round().astype(int)

df.to_excel(wyjscie_xlsx, index=False)
# konwersja do csv (wartosci oddzielone przecinkami)
df.to_csv(wyjscie_csv, index=False)
print("zapisano:", wyjscie_xlsx)
print("zapisano:", wyjscie_csv)
print("braki:", int(df.isna().sum().sum()))
