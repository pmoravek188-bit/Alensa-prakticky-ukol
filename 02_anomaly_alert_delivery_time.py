#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Úkol 2: Detekce anomálií v dodací lhůtě (delivery_time_days).
Skript identifikuje dny, kdy průměrná doba doručení u daného dopravce
stoupla o více než 30 % oproti průměru za posledních 14 dní.
"""

import pandas as pd
from pathlib import Path

# Cesta k datům (skript předpokládá běh ze složky Alensa)
DATA_PATH = Path(__file__).parent / "orders_marketing_logistics_de.csv"
OUTPUT_PATH = Path(__file__).parent / "02_alerts_vysledky.csv"

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df

def detect_delivery_anomalies(df: pd.DataFrame, threshold_pct: float = 0.30) -> pd.DataFrame:
    """
    Pro každý den a každého dopravce: porovná průměrnou delivery_time_days
    daného dne s průměrem za předchozích 14 dní. Pokud je nárůst > threshold_pct, je to anomálie.
    """
    results = []
    carriers = df["carrier"].unique()
    min_date = df["date"].min()
    
    for carrier in carriers:
        carrier_df = df[df["carrier"] == carrier].copy()
        carrier_df = carrier_df.sort_values("date")
        
        # Pro každý den: průměrná doba doručení v ten den
        daily_avg = carrier_df.groupby("date")["delivery_time_days"].mean().reset_index()
        daily_avg.columns = ["date", "avg_delivery_that_day"]
        
        for i, row in daily_avg.iterrows():
            day = row["date"]
            avg_today = row["avg_delivery_that_day"]
            # Průměr za předchozích 14 dní (včetně předchozího dne, ne včetně dne „dnes“)
            window_start = day - pd.Timedelta(days=14)
            window_end = day - pd.Timedelta(days=1)
            past_data = carrier_df[(carrier_df["date"] >= window_start) & (carrier_df["date"] <= window_end)]
            
            if len(past_data) == 0:
                continue
            avg_last_14 = past_data["delivery_time_days"].mean()
            if avg_last_14 <= 0:
                continue
            pct_change = (avg_today - avg_last_14) / avg_last_14
            if pct_change > threshold_pct:
                results.append({
                    "carrier": carrier,
                    "date": day.strftime("%Y-%m-%d"),
                    "avg_delivery_that_day": round(avg_today, 2),
                    "avg_last_14_days": round(avg_last_14, 2),
                    "pct_increase": round(pct_change * 100, 1),
                    "alert": "ANOMALIE",
                })
    
    return pd.DataFrame(results)

def main():
    df = load_data(DATA_PATH)
    alerts = detect_delivery_anomalies(df, threshold_pct=0.30)
    
    if len(alerts) == 0:
        print("Žádné anomálie nebyly detekovány (žádný den nepřekročil +30 % oproti 14dennímu průměru).")
        return
    
    alerts.to_csv(OUTPUT_PATH, index=False)
    print(f"Nalezeno {len(alerts)} anomálií. Výstup uložen do: {OUTPUT_PATH}")
    print(alerts.to_string(index=False))

if __name__ == "__main__":
    main()
