import time
import requests
import pandas as pd
import json

# Načtení JSON souboru
with open("RSSZ-cela-CR.jsonld", "r", encoding="utf-8") as f:
    data = json.load(f)

school_list = data.get("list", [])
df_schools = pd.json_normalize(school_list)

pd.set_option('display.max_columns', None)


def fetch_ukazatele(obdobi: str, ico: str) -> pd.DataFrame:
    url = f"https://monitor.statnipokladna.gov.cz/api/ukazatele?obdobi={obdobi}&ic={ico}"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"ICO {ico} vrací chybu 404 – data nenalezena.")
        print(f"URL: {url}")
        print("Error:", response.text)
        return pd.DataFrame()  # Vrátíme prázdný DataFrame

    response.raise_for_status()
    data = response.json()
    row = {"ico": ico, "obdobi": obdobi}
    for key, info in data.items():
        row[key] = info["value"]
    print("✅ Data pro ICO", ico, "načtena.")
    return pd.DataFrame([row])


obdobi = "1012"
results = []
i = 0

for ico in df_schools["ico"]:
    i += 1
    print(f"ICO {ico} ({i}/{len(df_schools)})")
    try:
        df_result = fetch_ukazatele(obdobi, ico)
        if not df_result.empty:
            results.append(df_result)
    except requests.HTTPError as e:
        print(f"Chyba při získávání dat pro ICO {ico}: {e}")

    if i % 100 == 0:
        if results:
            df_all_tmp = pd.concat(results, ignore_index=True)
            df_all_tmp.to_csv(f"tmp_{obdobi}.csv", index=False)
            print("Dočasný soubor tmp.csv uložen.")


if results:
    df_all = pd.concat(results, ignore_index=True)
else:
    df_all = pd.DataFrame()

df_all.to_csv(f"fincnce_{obdobi}.csv", index=False)
