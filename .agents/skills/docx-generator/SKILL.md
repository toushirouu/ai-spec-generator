---
name: docx-generator
description: Przygotowuje polskie specyfikacje DOCX laptopów, podzespołów komputerowych, monitorów i sprzętu gamingowego na podstawie zatwierdzonych danych.
---

# Generowanie DOCX

1. Używaj zatwierdzonego wzorca z `templates/`, jeśli został dostarczony. Generator ma być niezależny od kategorii produktu; nie wpisuj do jego kodu etykiet ani założeń właściwych dla pojedynczego modelu.
2. Przed generowaniem dokumentu do publikacji sprawdź status walidacji. Kontynuuj wyłącznie dla `PASS`; dla `REVIEW` i `FAIL` wstrzymaj publikację.
3. Umieść dostępne dane identyfikacyjne produktu oraz parametry z jednostkami. Etykiety i opcjonalne grupy parametrów pobieraj z rekordu danych; nieznane pola prezentuj na podstawie ich nazw.
4. Zapewnij identyfikowalne odniesienia do źródeł. Nie dopisuj wartości bez dowodu i nie ukrywaj braków ani konfliktów.
5. Dokument i opisy przygotuj po polsku; nie deklaruj zgodności z normą, certyfikacji ani obsługi technologii bez odpowiedniego dowodu.
6. Zapisuj gotowe specyfikacje w `output/`, a błędy i raporty walidacji w `reports/`.

Jeśli wzorzec DOCX lub zatwierdzone dane nie są dostępne, zgłoś brak zamiast tworzyć pozornie gotowy dokument.
