---
name: codex-flow-review
description: Wykonaj niezależne, read-only review wskazanego diffu pod kątem błędów, regresji, bezpieczeństwa, testów i zgodności z wymaganiami. Użyj po większej lub ryzykownej implementacji albo na prośbę o przegląd kodu.
---

# Niezależne review

1. Jeśli jesteś autorem zmian, przekaż review osobnemu agentowi `reviewer`; nie traktuj samooceny jako niezależnego review. Jeśli otrzymałeś zadanie jako reviewer, wykonaj je sam bez dalszego delegowania.
2. Ustal bazę i zakres porównania. Sprawdź Git, pełny diff i kryteria zadania; oddziel wcześniejsze zmiany użytkownika.
3. Przeczytaj potrzebny kod i wymagania. Oceń poprawność, regresje, bezpieczeństwo, obsługę błędów, wydajność i zbędną złożoność.
4. Oceń wartość testów i adekwatność walidacji. Brak skonfigurowanych lub wykonanych kontroli nie jest ich pozytywnym wynikiem. Nie żądaj nowego testu bez wskazania realistycznej awarii, która pozostaje niechroniona.
5. Sprawdź zgodność z zakresem i dokumentacją. Dla `$codex-flow-run-roadmap` obowiązują opisane w nim zasady odroczonej dokumentacji: uwzględnij przekazane decyzje, a brak redakcyjnej synchronizacji nie blokuje; artefakty wymagane kryteriami akceptacji pozostają w zakresie review.
6. Nie modyfikuj plików. Przy poprawkach oceń cały aktualny diff oraz wcześniejsze znaleziska.

Podaj problemy krytyczne, ważne i drobne, z plikiem, skutkiem, minimalną rekomendacją i informacją o zgodności z zakresem. Drobne uwagi nie blokują. Jeśli nie ma problemów blokujących, napisz: `Review zakończony — brak problemów blokujących.` Zakończ dokładnie jedną decyzją: `DECISION: APPROVED` albo `DECISION: CHANGES_REQUIRED`. Zatwierdzenie wymaga spełnionych kryteriów i wystarczających dowodów; przy brakach nazwij konkretną niezweryfikowaną właściwość.
