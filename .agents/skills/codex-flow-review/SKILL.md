---
name: codex-flow-review
description: Wykonaj read-only review w bieżącym wątku wskazanego diffu pod kątem błędów, regresji, bezpieczeństwa, testów i zgodności z wymaganiami. Użyj po większej lub ryzykownej implementacji albo na prośbę o przegląd kodu.
---

# Review zmian

1. Wykonaj review sam w bieżącym wątku, także gdy jesteś autorem zmian. Nie wywołuj ani nie deleguj review subagentowi. Samooceny nie nazywaj niezależnym review; osobny custom reviewer może użyć tego skilla tylko po jawnym zleceniu użytkownika.
2. Ustal bazę i zakres porównania. W `run-roadmap` baza `review_base` obejmuje cały przebieg: oceniaj wszystkie commity od tej bazy do HEAD oraz należące do zadania zmiany niecommitowane, nie tylko ostatni commit. Sprawdź Git, pełny diff i kryteria zadania; oddziel wcześniejsze zmiany użytkownika.
3. Przeczytaj potrzebny kod i wymagania. Oceń poprawność, regresje, bezpieczeństwo, obsługę błędów, wydajność i zbędną złożoność.
4. Oceń wartość testów i adekwatność walidacji. Brak skonfigurowanych lub wykonanych kontroli nie jest ich pozytywnym wynikiem. Nie żądaj nowego testu bez wskazania realistycznej awarii, która pozostaje niechroniona.
5. Sprawdź zgodność z zakresem i dokumentacją. Dla `$codex-flow-run-roadmap` obowiązują opisane w nim zasady odroczonej dokumentacji: uwzględnij przekazane decyzje, a brak redakcyjnej synchronizacji nie blokuje; artefakty wymagane kryteriami akceptacji pozostają w zakresie review.
6. Nie modyfikuj plików. Przy poprawkach oceń cały aktualny zakres od niezmienionej bazy oraz wcześniejsze znaleziska.

Podaj problemy krytyczne, ważne i drobne, z plikiem, skutkiem, minimalną rekomendacją i informacją o zgodności z zakresem. Drobne uwagi nie blokują. Jeśli nie ma problemów blokujących, napisz: `Review zakończony — brak problemów blokujących.` Zakończ dokładnie jedną decyzją: `DECISION: APPROVED` albo `DECISION: CHANGES_REQUIRED`. Zatwierdzenie wymaga spełnionych kryteriów i wystarczających dowodów; przy brakach nazwij konkretną niezweryfikowaną właściwość.
