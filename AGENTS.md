# Zasady projektu

## Cel i język
- Projekt tworzy specyfikacje techniczne produktów elektronicznych, w szczególności laptopów, podzespołów komputerowych, monitorów i sprzętu gamingowego.
- Dokumentację, raporty i komunikaty dla użytkownika przygotowuj po polsku.
- Dane i kod zapisuj w formatach możliwych do odczytu maszynowego.

## Badanie i źródła
- Preferuj oficjalne strony producentów, karty produktów, specyfikacje, instrukcje, arkusze danych i deklaracje producenta.
- Potwierdź dokładny numer katalogowy oraz wariant produktu przed przypisaniem parametrów.
- Każdy ustalony parametr musi mieć źródło; dodaj jednostkę, gdy parametr jej wymaga.
- Opis handlowy twórz wyłącznie z potwierdzonych danych i wiąż każdy akapit z parametrami źródłowymi.
- Nagłówki sekcji opisu łączą istotną cechę z jej praktycznym znaczeniem dla użytkownika. Wyjaśniaj korzyści na podstawie potwierdzonych parametrów, bez nieuzasadnionych obietnic.
- Wstęp i każdy akapit tematyczny opisu powinny zawierać zwykle 3–4 pełne zdania: cechę, jej konkretną korzyść dla użytkownika oraz parametry, które tę korzyść uzasadniają.
- Pisz o potwierdzonych cechach produktu bez dystansujących wstawek typu „producent podaje” lub „według producenta”. Zachowuj zwykły, rzeczowy ton opisu produktu; zastrzeżenia dodawaj tylko tam, gdzie wynikają z warunków pomiaru, zakresu działania albo opcjonalności wyposażenia.
- Redaguj opisy z myślą o SEO: naturalnie użyj kategorii, marki, dokładnego modelu i najważniejszych potwierdzonych cech. Unikaj upychania fraz, duplikowania tekstu i określeń niepopartych danymi; nie obiecuj pozycji w wyszukiwarce.
- Oddzielaj fakt techniczny od wniosku użytkowego. Zachowuj zastrzeżenia dla wartości maksymalnych, warunków pomiaru, akcesoriów opcjonalnych i różnic między wariantami.
- Nie zgaduj ani nie uzupełniaj brakujących wartości na podstawie podobnych produktów.
- Rozróżniaj `MISSING` (brak danych), `CONFLICT` (źródła są sprzeczne) i `NOT_APPLICABLE` (pole nie dotyczy produktu).
- Zgodność z normą, certyfikację lub obsługę technologii deklaruj wyłącznie, gdy dostępny dowód dotyczy dokładnie badanego produktu i wariantu.
- Zachowuj adres, tytuł, datę dostępu i lokalizację/identyfikator kopii każdego źródła.

## Walidacja i publikacja
- Walidacja ma status `PASS`, `REVIEW` albo `FAIL`; niejednoznaczności wymagają co najmniej `REVIEW`.
- Nie generuj dokumentu przeznaczonego do publikacji, jeżeli status walidacji to `REVIEW` lub `FAIL`.
- Raportuj brakujące dane, konflikty i pola nieadekwatne oddzielnie.
- Zmiany w schematach danych muszą mieć odpowiadające im testy.

## Zakres i bezpieczeństwo
- Przetwarzaj produkty jawnie podane w danych wejściowych; nie uruchamiaj masowego scrapera.
- Nie instaluj pakietów ani nie wykonuj operacji poza repozytorium bez zgody użytkownika.
- Preferuj bibliotekę standardową Pythona, dopóki zależność zewnętrzna nie jest konieczna i zatwierdzona.
