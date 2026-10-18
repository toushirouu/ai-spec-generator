---
name: product-description
description: Redaguje po polsku opis handlowy laptopa, komputera, monitora lub innego produktu elektronicznego na podstawie potwierdzonych danych.
---

# Przygotowanie opisu produktu

## Wejście

Używaj zweryfikowanego rekordu z `data/processed/`. Przed redakcją sprawdź dokładny model, wariant, status walidacji i dowody parametrów.

## Zasady

- Pisz po polsku, zwięźle i rzeczowo. Wzorzec treści znajduje się w `templates/product-description-template.md`.
- Nie twórz opisu do publikacji dla rekordu ze statusem `REVIEW` lub `FAIL`.
- Opisuj tylko cechy potwierdzone dla dokładnego modelu i wariantu. Nie przenoś danych z rodziny, wariantu opcjonalnego ani podobnego produktu.
- Powiąż każdy akapit z polami technicznymi przez `based_on`, np. `"based_on": ["display_resolution", "display_refresh_rate"]`.
- Nagłówek każdej sekcji opisowej łącz zrozumiałą cechę z jej znaczeniem dla użytkownika; unikaj nagłówków będących samą nazwą kategorii, np. „Procesor” lub „Ekran”.
- W akapicie najpierw wyjaśnij prostym językiem, co potwierdzona funkcja daje w praktyce, a potem podaj najważniejsze parametry i ograniczenia. Każde takie wyjaśnienie musi być proporcjonalnym wnioskiem z danych wskazanych w `based_on`.
- Nie dopisuj nieudowodnionych obietnic wydajności, czasu pracy, komfortu, trwałości, bezpieczeństwa ani kompatybilności. Nie przedstawiaj interpretacji jako gwarancji.
- Podawaj warunki dla wartości maksymalnych, wyników deklarowanych przez producenta, akcesoriów sprzedawanych osobno i konfiguracji zależnych od wariantu.
- Odróżniaj wyposażenie standardowe od opcjonalnego i konfigurowalnego.
- Nie kopiuj sformułowań z witryn handlowych ani producentów. Strony w `templates/README.md` są referencją układu, nie źródłem treści ani parametrów.
- Pomiń cenę, dostępność, promocje i zachęty zakupowe.
- Gdy potwierdzonych informacji jest mało, przygotuj krótszy opis; nie wypełniaj go ogólnikami.

## Zapis

W rekordzie produktu uzupełnij strukturę:

```json
"description": {
  "lead": "Krótki wstęp identyfikujący produkt i jego potwierdzone zastosowanie.",
  "lead_based_on": ["parameter_key"],
  "sections": [
    {
      "heading": "Nagłówek łączący potwierdzoną cechę z praktyczną korzyścią",
      "body": "Proste wyjaśnienie znaczenia funkcji, poparte parametrami i warunkami z dowodów.",
      "based_on": ["parameter_key"]
    }
  ]
}
```

Nie zmieniaj parametrów ani ich statusów w ramach redakcji opisu. Nierozstrzygnięte dane przekaż do walidacji technicznej.
