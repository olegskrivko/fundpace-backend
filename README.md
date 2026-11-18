# inside the project folder
uv init backend
cd backend
uv add django djangorestframework django-cors-headers
uv run python -m django startproject core .
uv run python manage.py startapp accounts
uv run python manage.py startapp campaigns


### 1. Skriešanas sacensības Latvijā

| Nosaukums | Norises vieta | Aptuvenais laiks | Aptuvenais dalībnieku skaits (2026) | Galvenās distances |
| :--- | :--- | :--- | :--- | :--- |
| **Rimi Rīgas maratons** | Rīga | Maija vidus (3. nedēļas nogale) | ~35 000 – 40 000+ | Maratons, pusmaratons, 10 km, 6 km, jūdze |
| **Stirnu buks** *(seriāls, ~7 posmi)* | Dažādi Latvijas meži / pilsētas | Marts – Oktobris (reizi mēnesī) | ~3 000 – 4 500 katrā posmā | Lūsis (~30 km), Vilks (~20 km), Zaķis (~12 km), Vāvere (~6 km) |
| **Nike Riga Run** | Rīga (Mežaparks) | Septembra sākums | ~6 000 – 8 000 | 10 km, 5 km, stafetes |
| **Sieviešu skrējiens** | Rīga (Mežaparks) | Maija sākums | ~3 500 – 5 000 | 7 km, 5 km (tikai sievietēm) |
| **Valmieras maratons** | Valmiera | Septembra vidus | ~3 000 – 4 000 | Maratons, pusmaratons, 10 km, 5 km |
| **Jelgavas nakts pusmaratons** | Jelgava | Jūlija beigas / Augusta sākums | ~3 000 – 4 000 | Pusmaratons, 10 km, 5 km |
| **Liepājas Jūras svētku pusmaratons** | Liepāja | Jūlija vidus (Jūras svētki) | ~2 500 – 3 500 | Pusmaratons, 10 km, 5 km, jūdze, stafete |
| **Kuldīgas pusmaratons** | Kuldīga | Augusta 1. puse | ~2 700 (2026. gada rekords) | Pusmaratons, 10 km, 5 km |
| **Jūrmalas Krāsu skrējiens (The Color Run)** | Jūrmala (Kauguri) | Augusta beigas | ~2 000 – 3 000 | 5 km (izklaides/festivāla skrējiens) |
| **Ventspils Piedzīvojumu parka maratons** | Ventspils | Jūnija sākums | ~2 000 – 3 000 | Maratons, pusmaratons, 10 km, 5 km |
| **Daugavpils skrējiens** | Daugavpils | Maijs vai Septembris | ~2 000 – 3 000 | 10 km, 5 km |
| **Izskrien Rīgu** *(seriāls, 5 posmi)* | Rīgas apkaimes / parki | Maijs – Augusts (darba dienu vakari) | ~1 500 – 2 200 katrā posmā | 10 km, 5 km |
| **Rojas pusmaratons** | Roja | Jūlija vidus (Zvejnieksvētki) | ~1 000 – 1 500 | Pusmaratons, 10 km, 5 km |
| **Ezerkauliņu Salaspils pusmaratons** | Salaspils | Jūnija vidus | ~1 000 – 1 500 | Pusmaratons, 10 km, 5 km |
| **Cēsis Eco Trail** | Cēsis / Gaujas Nacionālais parks | Augusts | ~1 000 – 1 500 | 80 km, 42 km, 21 km, 13 km |
| **Wings for Life World Run** | Valmiera (App Run) | Maija sākums | ~1 000 – 1 500 | "Ķērājauto" formāts (cik tālu paspēj) |
| **Noskrien Ziemu** *(ziemas taku seriāls)* | Dažādas vietas Latvijā | Janvāris – Marts, Novembris – Decembris | ~800 – 1 200 katrā posmā | ~10 km, ~20 km, ~30 km |
| **Rīga – Valmiera 107 km** | Rīga → Valmiera | Maija sākums | ~300 – 500 | 107 km ultramaratons |

---

### 2. Riteņbraukšanas sacensības Latvijā

| Nosaukums | Norises vieta | Aptuvenais laiks | Aptuvenais dalībnieku skaits (2026) | Disciplīna / Distances |
| :--- | :--- | :--- | :--- | :--- |
| **Siguldas Vienības brauciens** | Sigulda | Septembra 1. svētdiena | ~4 500 – 5 500 | Šoseja (~100 km), MTB (~50 km), Gravel (~60 km), Tautas (~35 km) |
| **Rīgas Velomaratons** | Rīga | Jūnija sākums | ~2 000 – 3 000 | Šoseja / pilsētas brauciens (~30 km, ~15 km) |
| **Rīga – Jūrmala velobrauciens** | Rīga – Jūrmala | Maija beigas / Jūnijs | ~1 500 – 2 500 | Tautas / šosejas brauciens (~35–40 km) |
| **Latvijas Valsts mežu MTB maratons** *(seriāls, ~7 posmi)* | Cēsis, Sigulda, Talsi, Smiltene, Ape u.c. | Aprīlis – Septembris | ~1 200 – 1 800 katrā posmā | MTB / Gravel (garā ~55–65 km, tautas ~35–45 km) |
| **Vivus.lv MTB maratons** *(seriāls, ~7 posmi)* | Tukums, Baldone, Kamparkalns, Ape u.c. | Aprīlis – Septembris | ~900 – 1 400 katrā posmā | MTB (maratons ~50–60 km, pusmaratons ~30–40 km) |
| **Filter Velokauss** *(seriāls, ~6 posmi)* | Biķernieki, Baldone, Salaspils u.c. | Maijs – Augusts | ~400 – 700 katrā posmā | Šoseja (individuālais un grupas brauciens) |
| **Dobeles un Apes gravel sacensības** *(piem., Gravel Weekend)* | Dobele, Ape, Cēsis | Vasaras mēneši | ~300 – 600 | Gravel (70 km – 130 km) |