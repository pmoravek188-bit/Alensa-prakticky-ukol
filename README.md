# Výběrové řízení – Senior Data Analyst, Alensa

Vypracované úkoly podle zadání (případová studie e-shop, DE trh).

---

## Obsah složky

| Soubor | Popis |
|--------|--------|
| **Úkol 1 – Příprava dat** | |
| `01_prompt_pro_vygenerovani_datasetu.txt` | Prompt použitý pro AI k vygenerování dummy dat |
| `orders_marketing_logistics_de.csv` | Dataset: objednávky, marketing (ROAS/CPA), náklady na produkty a dopravu, delivery_time_days, vratky, marže |
| **Úkol 2 – Automatizace a alerting** | |
| `02_prompt_pro_python_skript.txt` | Prompt pro návrh Python skriptu |
| `02_anomaly_alert_delivery_time.py` | Skript (pandas): detekce dní, kdy průměrná doba doručení u dopravce stoupla >30 % oproti 14dennímu průměru |
| `02_alerts_vysledky.csv` | Výstup skriptu – nalezené anomálie (po spuštění) |
| `02_jak_dorucit_alert_byznysu.md` | Stručný popis: jak doručit alert byznysu (Slack, e-mail, dashboard) |
| **Úkol 3 – Datová vizualizace** | |
| `03_prompt_ai_brainstorming_dashboard.txt` | Prompt pro brainstorming KPI a layoutu dashboardu |
| `03_navrh_dashboardu.md` | Návrh dashboardu: KPI, grafy, filtry, Mermaid wireframe |
| `03_dashboard_wireframe.html` | Wireframe dashboardu v HTML – lze otevřít v prohlížeči |
| **Úkol 4 – Executive Summary** | |
| `04_executive_summary_email_cmo.md` | E-mail pro CMO (max 4 věty), prompt a finální zpráva |

---

## Jak spustit skript (Úkol 2)

V terminálu ze složky `Alensa`:

```bash
python3 02_anomaly_alert_delivery_time.py
```

Výstup: `02_alerts_vysledky.csv` + výpis anomálií v konzoli.

---

## Poznámka k využití AI

Ke všem úkolům byly použity AI nástroje; kompletní prompty jsou v souborech `*_prompt*.txt` a v dokumentech u příslušných úkolů. Finální výstupy byly zredigovány a přizpůsobeny zadání (srozumitelnost, byznysový přínos, údernost).
