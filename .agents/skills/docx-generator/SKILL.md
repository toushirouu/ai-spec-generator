---
name: docx-generator
description: Tworzy polskie opisy handlowe i specyfikacje techniczne DOCX dla produktów elektronicznych z zatwierdzonych, udokumentowanych danych.
---

# Opis handlowy i specyfikacja DOCX

1. Używaj zatwierdzonego wzorca z `templates/`, jeśli został dostarczony. Generator ma być niezależny od kategorii produktu; nie wpisuj do jego kodu etykiet ani założeń właściwych dla pojedynczego modelu.
2. Przed generowaniem dokumentu do publikacji sprawdź status walidacji. Kontynuuj wyłącznie dla `PASS`; dla `REVIEW` i `FAIL` wstrzymaj publikację.
3. Twórz dwie sekcje: opis produktu z krótkim wprowadzeniem i tematycznymi akapitami oraz specyfikację techniczną w grupach właściwych dla kategorii. Nagłówki sekcji opisu łączą cechę z jej praktycznym znaczeniem dla użytkownika; akapit wyjaśnia je prostym językiem i podaje potwierdzające parametry. Opis buduj wyłącznie na zatwierdzonych faktach i wskazuj pola źródłowe przez `based_on`.
4. Umieść dostępne dane identyfikacyjne produktu oraz parametry z jednostkami. Etykiety i opcjonalne grupy parametrów pobieraj z rekordu danych; nieznane pola prezentuj na podstawie ich nazw.
5. Zapewnij identyfikowalne odniesienia do źródeł. Nie dopisuj wartości bez dowodu i nie ukrywaj braków ani konfliktów.
   Zachowaj zastrzeżenia dla wartości maksymalnych, warunków testu, elementów opcjonalnych i różnic między wariantami. Nie zamieniaj wniosków redakcyjnych w gwarancje efektu.
6. Dokument i opisy przygotuj po polsku; nie deklaruj zgodności z normą, certyfikacji ani obsługi technologii bez odpowiedniego dowodu.
7. Zapisuj gotowy dokument w `output/`, a raporty walidacji w `reports/`.

Jeśli wzorzec DOCX lub zatwierdzone dane nie są dostępne, zgłoś brak zamiast tworzyć pozornie gotowy dokument.
