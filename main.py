print("Inicialitzant sistema META-F⁴ / D₄...")

import pandas as pd
import yfinance as yf
from d4_core.core_d4 import D4Core

tickers = ["AENA.MC", "BTC-USD"]
data = {t: yf.download(t, period="1mo")["Close"] for t in tickers}

df = pd.DataFrame(data)
corr = df.corr().iloc[0, 1]

print(f"Correlació AENA vs BTC: {corr:.4f}")

# Inicialitza el nucli D₄
d4 = D4Core()

# Selecciona la sèrie d'AENA per a prova
aena_series = df["AENA.MC"].dropna()

# Predicció simple (placeholder)
pred = d4.predict(aena_series)

# Simulem una validació amb l'últim valor real
last_real = aena_series.iloc[-1]
score = d4.validate(pred, last_real)

print(f"Predicció D₄ (AENA): {pred:.2f}")
print(f"Valor real: {last_real:.2f}")
print(f"Precisió (validació simple): {score:.4f}")
print("Nucli D₄ integrat correctament.")
