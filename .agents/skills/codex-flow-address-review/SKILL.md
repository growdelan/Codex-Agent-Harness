---
name: codex-flow-address-review
description: Wdróż wyłącznie zaakceptowane poprawki wynikające z wcześniejszego review i ponownie zweryfikuj zmieniony zakres. Użyj, gdy istnieje konkretna lista problemów z review, ale nie należy dodawać nowych funkcji ani wykonywać szerokiego refaktoru.
---

# Poprawki po review

1. Przeczytaj pełny raport review, bazę porównania i aktualny zakres zmian. W `run-roadmap` poprawki dotyczą całego przebiegu, także problemów integracji między milestone'ami. Wykonaj je w bieżącym wątku.
2. Zweryfikuj zasadność każdego znaleziska na podstawie kodu i wymagań; uzasadnij odrzucenie błędnej uwagi. Dla każdego zasadnego problemu potwierdź, że poprawka mieści się w bieżącym zakresie. Problemy wymagające nowej funkcji lub decyzji architektonicznej odłóż i wyraźnie zgłoś.
3. Wprowadź minimalne poprawki kodu, testów lub dokumentacji potrzebne do rozwiązania zaakceptowanych problemów.
4. Uruchom walidację zmienionego zakresu, a następnie pełne `./scripts/verify.sh`, jeśli zmiana może wpływać szerzej.
5. Samodzielne użycie tego skilla nie autoryzuje commita ani pusha. W `run-roadmap` po zakończeniu poprawek wróć do prowadzącego go głównego agenta w tym samym wątku: zapisuje checkpoint, wykonuje commit rundy i ponawia review według limitu całego przebiegu. Nie uruchamiaj własnej pętli review ani subagenta reviewera.

Podsumuj naprawione problemy, odłożone elementy, zmienione pliki i wyniki walidacji.
