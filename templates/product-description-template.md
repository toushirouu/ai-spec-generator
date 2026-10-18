# Wzorzec opisu handlowego produktu

Opis jest redagowany po polsku na podstawie zweryfikowanego rekordu produktu. Generator umieszcza poniższe pola w sekcji „Opis produktu” dokumentu DOCX.

## Struktura danych

```json
"description": {
  "lead": "1–2 zdania identyfikujące produkt i jego główne zastosowanie, oparte na potwierdzonych danych.",
  "lead_based_on": ["parameter_key_1"],
  "sections": [
    {
      "heading": "Temat wynikający z cech produktu",
      "body": "Krótki, rzeczowy akapit oparty na parametrach ze specyfikacji.",
      "based_on": ["parameter_key_1", "parameter_key_2"]
    }
  ]
}
```

## Zasady redakcyjne

- Zacznij od rodzaju urządzenia, nazwy modelu i potwierdzonego zastosowania.
- Dodaj 2–5 krótkich sekcji tematycznych, zależnie od liczby istotnych, potwierdzonych cech. Nie wymuszaj sekcji bez danych.
- Łącz cechę ze skutkiem użytkowym tylko wtedy, gdy wynika on z danych. Nie dopisuj zapewnień o wydajności, komforcie, bezpieczeństwie ani kompatybilności bez podstawy.
- Wstęp wskazuje pola w `lead_based_on`, a każdy akapit tematyczny — pola w `based_on`. Generator umieści ich etykiety przy akapicie.
- Odróżniaj wyposażenie standardowe od opcjonalnego, konfigurowalnego i zależnego od wariantu.
- Nie umieszczaj ceny, dostępności, promocji ani treści sprzedawcy, chyba że osobny zakres projektu jawnie tego wymaga.
- Unikaj superlatywów, powtórzeń i zapożyczania sformułowań z materiałów referencyjnych.
- Jeśli brak podstaw do opisu marketingowego, pozostaw opis do uzupełnienia i nie wymyślaj treści.

## Przykładowe grupy tematyczne

Wybieraj wyłącznie te, które mają potwierdzone dane: wydajność i platforma, ekran, pamięć i pamięć masowa, łączność, ergonomia, bezpieczeństwo, mobilność, możliwości rozbudowy, zastosowanie.
