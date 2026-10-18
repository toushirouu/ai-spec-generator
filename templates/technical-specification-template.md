# Wzorzec specyfikacji technicznej

Każdy dokument zawiera identyfikację produktu, opis handlowy (jeżeli został przygotowany), specyfikację i źródła. Generator bierze konfigurację układu z `document-template.json`, a pola z rekordu JSON produktu.

## Identyfikacja produktu

- Producent
- Rodzina / seria / model
- Dokładny kod producenta (MPN) i wariant
- EAN/GTIN, jeśli został potwierdzony
- Kategoria i przeznaczenie, jeśli są potwierdzone

## Tabela parametrów

| Grupa | Parametr | Wartość | Jednostka | Źródło i lokalizacja dowodu |
|---|---|---|---|---|
| Kategoria właściwa dla produktu | Pole potwierdzone | Wartość potwierdzona | Jeżeli dotyczy | Identyfikator źródła i sekcja/strona |

Grupy są zależne od produktu. Przykładowo laptop może mieć sekcje procesora, ekranu, pamięci, dysku, grafiki, komunikacji, portów, baterii i obudowy; monitor — obrazu, złączy, funkcji, regulacji i zasilania; komputer stacjonarny — procesora, grafiki, pamięci, dysków, płyty głównej, zasilacza i obudowy.

## Zasady danych

- Każda wartość ma źródło i lokalizację dowodu; dodaj jednostkę, jeżeli dotyczy.
- Brak, konflikt źródeł i pole nieadekwatne są odrębnymi stanami (`MISSING`, `CONFLICT`, `NOT_APPLICABLE`).
- Nie pokazuj pola nieadekwatnego jako pustej wartości. Braki i konflikty wymagają rozwiązania przed statusem `PASS`.
- Nie deklaruj zgodności, certyfikacji ani funkcji na podstawie rodziny produktu — dowód musi dotyczyć konkretnego wariantu.
- Nie dopisuj ceny, dostępności ani parametrów pochodzących tylko z podobnego modelu.
