---
name: codex-flow-address-review
description: Wdróż wyłącznie zaakceptowane poprawki wynikające z wcześniejszego review i ponownie zweryfikuj zmieniony zakres. Użyj, gdy istnieje konkretna lista problemów z review, ale nie należy dodawać nowych funkcji ani wykonywać szerokiego refaktoru.
---

# Poprawki po review

1. Przeczytaj pełny raport review, bazę porównania i aktualny zakres zmian. W `run-roadmap` poprawki dotyczą całego przebiegu, także problemów integracji między milestone'ami. Wykonaj je w bieżącym wątku. Stosuj [kontrakt flow](../codex-flow-run-roadmap/references/flow-contract.md); w `run-roadmap` obowiązują jego ograniczenia.
2. Zweryfikuj zasadność każdego znaleziska na podstawie kodu i wymagań; uzasadnij odrzucenie błędnej uwagi. Dla każdego zasadnego problemu potwierdź, że poprawka mieści się w bieżącym zakresie. Problemy wymagające nowej funkcji lub decyzji architektonicznej zgłoś krótko w rozmowie jako poza zakresem; nie twórz dla nich plików ani osobnego backlogu.
3. Wprowadź minimalne poprawki kodu i testów potrzebne do rozwiązania zaakceptowanych problemów. Dokumentację zmieniaj, gdy jest przedmiotem zaakceptowanej uwagi lub wymaga minimalnej synchronizacji bezpośrednio wynikającej z naprawy (np. konfiguracja, użycie, decyzja techniczna). Nie dokumentuj przebiegu napraw jako nowej specyfikacji.
4. Uruchom walidację zmienionego zakresu, a następnie pełne `./scripts/verify.sh`, jeśli zmiana może wpływać szerzej.
5. Samodzielne użycie tego skilla nie autoryzuje commita ani pusha. W `run-roadmap` po zakończeniu poprawek wróć do prowadzącego go głównego agenta w tym samym wątku: zapisuje checkpoint i ponawia review pełnego worktree bez stagingu, commita ani pusha według limitu całego przebiegu. Nie uruchamiaj własnej pętli review ani subagenta reviewera.

## Wynik bez dodatkowych plików

- Wynik podaj wyłącznie w rozmowie, zwięźle: naprawione identyfikatory uwag, wynik walidacji i ewentualny bloker. Dla odrzuconej uwagi dodaj krótkie uzasadnienie. Nie powtarzaj pełnego raportu review, listy wszystkich plików ani logów komend.
- Nie twórz plików z podsumowaniami, raportami review, dowodami walidacji, logami ani odłożonymi uwagami — także w `docs/spec/`, `validate/` lub innych katalogach. Wyjątkiem jest jawna prośba użytkownika o taki artefakt.
- Walidację uruchamiaj normalnie, ale nie przekierowuj jej wyjścia do nowych plików raportowych w repo i nie dodawaj generatorów raportów. Jeśli narzędzie wymaga plików tymczasowych, użyj lokalizacji tymczasowej poza repo, o ile jest konfigurowalna; nie zmieniaj potrzebnych kontroli tylko po to, by wyłączyć ich standardowe artefakty.
- Jeśli nadrzędny workflow wymaga checkpointu, ogranicz go do krótkiej aktualizacji istniejącego `STATUS.md`: wynik rundy, walidacja, aktywny bloker oraz istotne uzasadnienia rozwiązania lub odrzucenia uwag. Zachowaj pozostałe chronione pola checkpointu. Nie zakładaj dodatkowego pliku ani odnośnika do nowego raportu. Raport dla użytkownika podaj w rozmowie; nie zostawiaj wyłącznie w niej informacji potrzebnej do wznowienia przebiegu.
