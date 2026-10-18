# Wzorzec opisu handlowego produktu

Opis jest redagowany po polsku na podstawie zweryfikowanego rekordu produktu. Generator umieszcza poniższe pola w sekcji „Opis produktu” dokumentu DOCX.

## Struktura danych

```json
"description": {
  "lead": "1–2 zdania identyfikujące produkt i jego główne zastosowanie, oparte na potwierdzonych danych.",
  "lead_based_on": ["parameter_key_1"],
  "sections": [
    {
      "heading": "Potwierdzona cecha i jej praktyczne znaczenie dla użytkownika",
      "body": "Krótki akapit wyjaśniający zastosowanie prostym językiem, a następnie podający potwierdzone parametry i warunki.",
      "based_on": ["parameter_key_1", "parameter_key_2"]
    }
  ]
}
```

## Zasady redakcyjne

- Zacznij od rodzaju urządzenia, nazwy modelu i potwierdzonego zastosowania.
- Dodaj 2–5 krótkich sekcji tematycznych, zależnie od liczby istotnych, potwierdzonych cech. Nie wymuszaj sekcji bez danych.
- Każdy nagłówek sekcji powinien mówić, co dana cecha oznacza dla użytkownika, np. „Płynniejszy obraz podczas przewijania” zamiast samego „Ekran”. Wybierz korzyść lub zastosowanie pasujące do produktu.
- Rozpocznij akapit od prostego wyjaśnienia praktycznego znaczenia, a następnie podaj potwierdzające parametry. Czytelnik ma rozumieć korzyść bez znajomości skrótów technicznych.
- Oddzielaj parametr od wniosku: nie dopisuj zapewnień o wydajności, komforcie, bezpieczeństwie ani kompatybilności, jeśli dane ich nie uzasadniają. Nie przedstawiaj przypuszczenia jako gwarantowanego efektu.
- Stosuj zastrzeżenia dla wartości maksymalnych, deklaracji producenta, opcjonalnych akcesoriów, konfiguracji i wyników zależnych od warunków.
- Wstęp wskazuje pola w `lead_based_on`, a każdy akapit tematyczny — pola w `based_on`. Generator umieści ich etykiety przy akapicie.
- Odróżniaj wyposażenie standardowe od opcjonalnego, konfigurowalnego i zależnego od wariantu.
- Nie umieszczaj ceny, dostępności, promocji ani treści sprzedawcy, chyba że osobny zakres projektu jawnie tego wymaga.
- Unikaj superlatywów, powtórzeń i zapożyczania sformułowań z materiałów referencyjnych.
- Jeśli brak podstaw do opisu marketingowego, pozostaw opis do uzupełnienia i nie wymyślaj treści.

## Przykładowe grupy tematyczne

Wybieraj wyłącznie te, które mają potwierdzone dane: wydajność i platforma, ekran, pamięć i pamięć masowa, łączność, ergonomia, bezpieczeństwo, mobilność, możliwości rozbudowy, zastosowanie. Przykładowo wyjaśnij, jak częstotliwość odświeżania wpływa na odbiór ruchu, jak pojemność pamięci wpływa na liczbę przechowywanych plików albo jak regulacja podstawy ułatwia dopasowanie ustawienia ekranu — wyłącznie gdy dana funkcja jest potwierdzona.
