---
name: docx-generator
description: Tworzy po polsku zgodne z SEO opisy handlowe i specyfikacje techniczne DOCX dla produktów elektronicznych na podstawie zatwierdzonych danych.
---

# Opis handlowy i specyfikacja DOCX

1. Używaj zatwierdzonego wzorca z `templates/`, jeśli został dostarczony. Generator ma być niezależny od kategorii produktu; nie wpisuj do jego kodu etykiet ani założeń właściwych dla pojedynczego modelu.
2. Przed generowaniem dokumentu do publikacji sprawdź status walidacji. Kontynuuj wyłącznie dla `PASS`; dla `REVIEW` i `FAIL` wstrzymaj publikację.
3. Twórz dwie sekcje: opis produktu z wprowadzeniem i tematycznymi akapitami oraz specyfikację techniczną w grupach właściwych dla kategorii. Wstęp i każdy akapit opisu powinny mieć 3–4 zdania. Nagłówki sekcji łączą cechę z jej praktycznym znaczeniem dla użytkownika; tekst wyjaśnia konkretną korzyść prostym językiem i podaje potwierdzające parametry. Pisz o potwierdzonych cechach wprost, bez „producent podaje” i „według producenta”. Opis przygotuj zgodnie z SEO: naturalnie uwzględnij kategorię, markę, dokładny model i najważniejsze potwierdzone cechy, ale unikaj upychania fraz i sztucznych list słów kluczowych. Buduj go wyłącznie na zatwierdzonych faktach i wskazuj pola źródłowe przez `based_on`.
4. Umieść dostępne dane identyfikacyjne produktu oraz parametry z jednostkami. Etykiety i opcjonalne grupy parametrów pobieraj z rekordu danych; nieznane pola prezentuj na podstawie ich nazw.
   Zachowaj czytelną hierarchię tytułu i nagłówków oraz naturalne brzmienie treści. Nie gwarantuj wyników SEO ani nie dodawaj niepotwierdzonych określeń marketingowych.
5. Zapewnij identyfikowalne odniesienia do źródeł. Nie dopisuj wartości bez dowodu i nie ukrywaj braków ani konfliktów.
   Zachowaj zastrzeżenia, gdy są ważne dla użytkownika: dla wartości maksymalnych, warunków pomiaru, elementów opcjonalnych i różnic między wariantami. Nie zamieniaj wniosków redakcyjnych w gwarancje efektu.
6. Dokument i opisy przygotuj po polsku; nie deklaruj zgodności z normą, certyfikacji ani obsługi technologii bez odpowiedniego dowodu.
7. Zapisuj gotowy dokument w `output/`, a raporty walidacji w `reports/`.

Jeśli wzorzec DOCX lub zatwierdzone dane nie są dostępne, zgłoś brak zamiast tworzyć pozornie gotowy dokument.
