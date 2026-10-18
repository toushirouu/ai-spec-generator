# Generator opisów i specyfikacji produktów

Projekt pomaga zebrać potwierdzone informacje o sprzęcie elektronicznym, przygotować na ich podstawie polski opis oraz specyfikację i złożyć je do pliku Word.

## Jak przygotować dokument

1. **Wskaż dokładny produkt.** Zbierz producenta, pełny kod modelu i wariant, np. numer MPN. Link do strony produktu pomaga rozpocząć badanie, ale nie zastępuje potwierdzenia specyfikacji.
2. **Poproś AI o zbadanie produktu.** Użyj skilla `product-research`. Preferowane są oficjalna strona producenta, karta produktu, instrukcja i karta katalogowa. Każdy parametr ma mieć źródło, lokalizację dowodu i jednostkę, jeśli jej wymaga.
3. **Zapisz dane produktu.** Rekord JSON trafia do `data/processed/`, a metadane wykorzystanych źródeł do `data/sources/`. Te katalogi są lokalne i ignorowane przez Git.
4. **Przygotuj opis.** Użyj skilla `product-description` i wzorca `templates/product-description-template.md`. Opis ma wynikać z potwierdzonych danych. Wstęp i każdy akapit tematyczny powinny mieć 3–4 zdania: nagłówek pokazuje praktyczną korzyść, a akapit wyjaśnia ją prostym językiem i podaje powiązane cechy produktu. Dla SEO naturalnie uwzględnij kategorię, markę, model i kluczowe potwierdzone cechy; unikaj powtarzania fraz. Pisz o danych wprost, bez „producent podaje” i „według producenta”. Każdy akapit łączy się z parametrami przez `based_on`.
5. **Sprawdź dane.** Użyj skilla `technical-validation`. Nie zgaduj braków. Rozróżnij `MISSING`, `CONFLICT` i `NOT_APPLICABLE`. Publikację można przygotować wyłącznie dla statusu `PASS`.
6. **Wygeneruj Worda.** Po uzupełnieniu rekordu i ustawieniu `PASS` uruchom:

   ```powershell
   python -m src.docx_generator "data/processed/id-produktu.json"
   ```

   Plik DOCX pojawi się w `output/` pod nazwą rekordu JSON. Własną konfigurację układu można podać przez `--template`.

## Statusy

- `REVIEW` — potrzebna ręczna weryfikacja, brakuje danych lub źródła nie rozstrzygają informacji.
- `FAIL` — tożsamość produktu lub dane są błędne albo nie można ich wiarygodnie potwierdzić.
- `PASS` — dokładny wariant i dane potrzebne do dokumentu są potwierdzone; nierozstrzygnięte problemy zostały rozwiązane.

Nie zmieniaj statusu na `PASS` wyłącznie po to, by odblokować generowanie. Generator sprawdza status oraz obecność opisu i jego odwołań do parametrów; nie przeprowadza samodzielnie pełnej walidacji technicznej.

## Dane wejściowe

`data/input/products.csv` służy do krótkiej listy produktów. Wymagany nagłówek:

```csv
product_id,manufacturer,catalog_number,variant,product_url,validation_status,parameters_json
```

Przykładowy wiersz można zacząć od statusu `REVIEW` i pustego obiektu parametrów: `"{}"`. Plik wejściowy jest lokalny i ignorowany przez Git.

Polecenie:

```powershell
python -m src.product_data
```

sprawdza strukturę CSV i podstawowy zapis parametrów. Nie wyszukuje informacji w Internecie, nie ocenia poprawności danych technicznych i nie ustala statusu walidacji za człowieka.

## Układ dokumentu

Wygenerowany Word zawiera identyfikację produktu, opis handlowy z nagłówkami wyjaśniającymi praktyczne znaczenie cech, tabelę parametrów z dowodami oraz listę źródeł. Układ konfiguruje `templates/document-template.json`; zasady redakcyjne znajdują się w pozostałych plikach `templates/`. Szablony są częścią projektu i mogą być wersjonowane. Dane produktów, raporty i wygenerowane dokumenty pozostają lokalne.

## Ważne ograniczenia

- Projekt nie ma masowego scrapera ani automatycznego badania produktów.
- Sam skrypt Pythona nie pisze opisu marketingowego. Treść przygotowuje AI zgodnie ze skillem `product-description`, a generator umieszcza ją w Wordzie.
- Nie instaluj dodatkowych pakietów: obecny generator korzysta z biblioteki standardowej Pythona.
- Jeśli model, wariant, źródła lub opis są niekompletne, uzupełnij je przed generowaniem; nie maskuj braków tekstem promocyjnym.
