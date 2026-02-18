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


def detect_delivery_anomalies(
    df: pd.DataFrame,
    threshold_pct: float = 0.30,
    window_days: int = 14,
    min_periods: int = 14,
) -> pd.DataFrame:
    """
    Pro každý den a každého dopravce:
    - spočítá průměr delivery_time_days v daný den
    - porovná s průměrem z předchozích 14 dní (bez dne "dnes")
    - pokud je nárůst > threshold_pct, označí jako anomálii
    """
    daily_avg = (
        df.groupby(["carrier", "date"], as_index=False)["delivery_time_days"]
        .mean()
        .rename(columns={"delivery_time_days": "avg_delivery_that_day"})
        .sort_values(["carrier", "date"])
    )

    # Rolling průměr za předchozích 14 dní (bez dne "dnes")
    daily_avg["avg_last_14_days"] = (
        daily_avg.groupby("carrier")["avg_delivery_that_day"]
        .apply(lambda s: s.rolling(window_days, min_periods=min_periods).mean().shift(1))
        .reset_index(level=0, drop=True)
    )

    daily_avg["pct_increase"] = (
        (daily_avg["avg_delivery_that_day"] - daily_avg["avg_last_14_days"])
        / daily_avg["avg_last_14_days"]
    )

    alerts = daily_avg[
        (daily_avg["avg_last_14_days"].notna())
        & (daily_avg["pct_increase"] > threshold_pct)
    ].copy()

    if alerts.empty:
        return pd.DataFrame(columns=[
            "carrier",
            "date",
            "avg_delivery_that_day",
            "avg_last_14_days",
            "pct_increase",
            "alert",
        ])

    alerts["pct_increase"] = (alerts["pct_increase"] * 100).round(1)
    alerts["avg_delivery_that_day"] = alerts["avg_delivery_that_day"].round(2)
    alerts["avg_last_14_days"] = alerts["avg_last_14_days"].round(2)
    alerts["alert"] = "ANOMALIE"

    alerts["date"] = alerts["date"].dt.strftime("%Y-%m-%d")
    return alerts[[
        "carrier",
        "date",
        "avg_delivery_that_day",
        "avg_last_14_days",
        "pct_increase",
        "alert",
    ]]


def main():
    df = load_data(DATA_PATH)
    alerts = detect_delivery_anomalies(df, threshold_pct=0.30)

    alerts.to_csv(OUTPUT_PATH, index=False)

    if len(alerts) == 0:
        print("Žádné anomálie nebyly detekovány (žádný den nepřekročil +30 % oproti 14dennímu průměru).")
        return

    print(f"Nalezeno {len(alerts)} anomálií. Výstup uložen do: {OUTPUT_PATH}")
    print(alerts.to_string(index=False))


if __name__ == "__main__":
    main()
