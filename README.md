# Wizualizacja i Eksploracja Danych

Repozytorium z rozwiązaniami ćwiczeń laboratoryjnych.

## Struktura

Każde ćwiczenie ma ten sam układ:

```
cw-XX/
├── zadania/        # materiały (pptx, dane wejściowe)
└── rozwiazania/    # notebooki / skrypty
```

| Folder | Temat |
|--------|--------|
| `cw-01` | Przygotowanie danych (Wine) |
| `cw-02` | EDA — Black Friday (`train.csv`) |
| `cw-03` | EDA — House Prices |
| `cw-04` | Selekcja zmiennych (Iris) |
| `cw-05` | Selekcja cech — χ² |
| `cw-06` | Matplotlib |
| `cw-07` | Selekcja zmiennych — Random Forest |

## Setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook
```

Notebooki ładują dane ścieżkami względnymi (`../zadania/...`) — uruchamiaj je z katalogu `rozwiazania/` albo przez Jupyter z otwartym folderem projektu.
