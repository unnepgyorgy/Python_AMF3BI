# Házi Könyvtáram Alkalmazás (XML, Ár és Darabszám Kezelés)
## Hallgató adatai
* Ünnep György Péter
* Neptun kód: AMF3BI
## Feladat rövid leírása
Egy egyszerû könyv nyilvántartó alkalmazás, Név, darabszám, mennyiség adatokkal. 
A program az adatokat (cím, ár, darabszám) XML formátumban tárolja. 
Egyszerû statisztikát számol ki (összes darabszám, átlagos ár, teljes érték), 
és bemutatja a feladatleírásban elõírt Python modulok mûködését.

## Modulok és függvények felsorolása

### 1. `modul_AMF3BI.py` (Saját modul)
* Osztály: KonyvRegiszterAMF3BI   - Az XML alapú fájlkezelésért felel.
  * __init__(filename)                - XML fájl alap .
  * betolt_konyvek_amf3bi()           - Beolvassa a könyvek adatait az XML-bõl.
  * uj_konyv_amf3bi(cime, ara, menny) - Új könyvet visz fel a listába és az XML fájlba.
  * mindenkonyv_amf3bi()              - Visszaadja az osztályban tárolt könyvek listáját.

### 2. `main.py` (Program)
* Saját függvény (osztályon kívül):
* *  statisztikaosszegzes_amf3bi(mindenkonyv)	- Elvégzi a kért matematikai számításokat:
*		1. Összes könyv darabszáma
*		2. Könyvek átlagos ára
*		3. Könyvtár teljes értéke (ár * mennyiség összege)
*
* **Osztály:** `BookAppAMF3BI`	- A grafikus felület és eseménykezelés osztálya.
  * `__init__(root)`			- Létrehozza az bevitelt, a formázott listadobozt és a gombokat.
  * `load_listbox()`			- Megjeleníti az elmentett könyveket.
  * `uj_konyv()`				- Kezeli az új könyv hozzáadását és a lista frissítésével.
  * `statisztikak()`			- Megjeleníti a számítások eredményét és a `math` modul 3 függvényét (`math.sqrt()`, `math.factorial()`, `math.pow()`).