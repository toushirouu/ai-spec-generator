---
name: product-description
description: Redaguje po polsku opisy produktów elektronicznych zgodne z SEO, oparte na potwierdzonych danych i wyjaśniające korzyści dla użytkownika.
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
- Wstęp i każdy akapit sekcji rozwiń do 3–4 pełnych zdań. Wyjaśnij prostym językiem konkretną korzyść dla użytkownika, a następnie podaj najważniejsze parametry i zastosowanie. Każde wyjaśnienie musi być proporcjonalnym wnioskiem z danych wskazanych w `based_on`.
- Pisz o potwierdzonych cechach wprost i naturalnie, jak w opisie produktu. Nie dodawaj powtarzalnych sformułowań „producent podaje” ani „według producenta”; pochodzenie informacji jest widoczne w danych i źródłach dokumentu.
- Stosuj podstawowe zasady SEO bez obniżania jakości tekstu: wpleć naturalnie wstępem kategorię produktu, markę, pełny model lub kod katalogowy oraz najważniejsze potwierdzone cechy, których użytkownik może szukać.
- Używaj czytelnych nagłówków opisujących temat i korzyść. Uwzględniaj naturalne synonimy kategorii i nazwy zastosowań tylko wtedy, gdy pasują do produktu i są potwierdzone.
- Nie upychaj powtarzanych fraz, nie twórz sztucznych list słów kluczowych i nie obiecuj pozycji w wynikach wyszukiwania. Nie dopisuj niepotwierdzonych określeń typu „najlepszy”, „gamingowy”, „profesjonalny” ani innych etykiet wyłącznie dla SEO.
- Twórz oryginalne sformułowania; nie kopiuj tekstów producenta ani sprzedawców. Każda fraza SEO musi brzmieć naturalnie i pozostawać zgodna z udokumentowanymi cechami wariantu.
- Nie dopisuj nieudowodnionych obietnic wydajności, czasu pracy, komfortu, trwałości, bezpieczeństwa ani kompatybilności. Nie przedstawiaj interpretacji jako gwarancji.
- Zachowuj istotne warunki wartości maksymalnych, pomiarów, akcesoriów sprzedawanych osobno i konfiguracji zależnych od wariantu, ale nie osłabiaj nimi zwykłych, potwierdzonych parametrów.
- Odróżniaj wyposażenie standardowe od opcjonalnego i konfigurowalnego.
- Nie kopiuj sformułowań z witryn handlowych ani producentów. Strony w `templates/README.md` są referencją układu, nie źródłem treści ani parametrów.
- Pomiń cenę, dostępność, promocje i zachęty zakupowe.
- Gdy potwierdzonych informacji jest mało, przygotuj krótszy opis; nie wypełniaj go ogólnikami.

## Zapis

W rekordzie produktu uzupełnij strukturę:

```json
"description": {
  "lead": "Wstęp identyfikujący kategorię, markę, model i potwierdzone zastosowanie; naturalnie uwzględnia główne frazy wyszukiwane przez klientów.",
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
