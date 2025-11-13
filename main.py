print("Inicialitzant sistema META-F⁴ / import pandas as pd
import yfinance as yf

tickers = ["AENA.MC", "BTC-USD"]
data = {t: yf.download(t, period="1mo")["Close"] for t in tickers}

df = pd.DataFrame(data)
corr = df.corr().iloc[0, 1]

print(f"Correlació AENA vs BTC: {corr:.4f}")
print("Sistema D₄ operatiu dins Docker.")
