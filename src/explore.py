import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "paro_por_municipios_2025.csv"

raw_df = pd.read_csv(RAW_FILE , encoding= "latin-1" , sep= ";" , header= 0)


print("Shape:" , raw_df.shape)
print("Columns:" , raw_df.columns)
print(raw_df.head(5))
raw_df.info()
