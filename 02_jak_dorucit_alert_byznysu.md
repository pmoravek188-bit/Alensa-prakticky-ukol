# Úkol 2: Jak doručit alert byznysu (logistika + marketing)

**Stručně vlastními slovy:**

Výsledek detekce anomálií bych byznysu doručoval **automatizovaně**, aby manažeři nemuseli nic spouštět ani hledat v reportech.

1. **Slack** – Doporučuji **Slack webhook**: skript na konci zavolá POST na webhook URL (např. kanál #logistika nebo #marketing-alerts). Zpráva by obsahovala: který dopravce, které datum, o kolik % se průměrná doba doručení zhoršila a odkaz na detail (např. Looker/Sheets). Výhoda: okamžitá viditelnost, možnost reagovat v konverzaci, integrace do běžného workflow.

2. **E-mail** – Alternativa pro ty, kdo Slack nepoužívají: denní digest (např. po nočním běhu skriptu) na adresy vedoucího logistiky a marketingu. Předmět např. „Alert DE: zpoždění dopravce X – [datum]“. Tělo: stručná tabulka anomálií + doporučení (zkontrolovat dopravce, zvážit přepnutí části objemů).

3. **Společný dashboard** – Alert by se zároveň zobrazil v dashboardu (Úkol 3) jako „červený“ KPI nebo sekce „Aktivní alerty“, aby CMO a top management viděli anomálie v kontextu marže a ROAS.

**Shrnutí:** Preferoval bych **Slack webhook** pro rychlou reakci logistiky a marketingu; e-mail jako zálohu nebo pro denní souhrn. Výstup skriptu (CSV/JSON) by se buď poslal v příloze, nebo by Slack zpráva odkazovala na předpřipravený report.
