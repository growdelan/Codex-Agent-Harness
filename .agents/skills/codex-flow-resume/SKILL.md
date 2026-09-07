---
name: codex-flow-resume
description: Odtwórz stan istniejącego projektu po rozpoczęciu nowej sesji lub powrocie do przerwanej pracy. Użyj, gdy użytkownik chce kontynuować projekt, poznać aktualny stan albo ustalić najbliższy bezpieczny krok bez modyfikowania plików.
---

# Wznowienie projektu

1. Uruchom `./scripts/check-context-size.sh`, a następnie przeczytaj `STATUS.md`.
2. Z `ROADMAP.md` odczytaj tylko milestone'y `in_progress`, `planned`, `blocked` oraz krótki indeks ukończonych prac. Nie czytaj archiwum domyślnie.
3. Potraktuj `spec.md` jako indeks. Doczytaj tylko wskazane sekcje lub dokumenty z `docs/spec/` i `docs/decisions/`, które są potrzebne do najbliższej decyzji.
4. Doczytaj `AGENTS.md`, diff lub kod tylko wtedy, gdy są potrzebne do zweryfikowania bieżącego stanu.
5. Porównaj dokumentację i checkpoint z faktycznym stanem repo oraz historią Git. Sprawdź stałą bazę `review_base`, fazę przebiegu, wyniki milestone'ów, commity, review całego zakresu i łączną liczbę rund poprawek. `implemented_pending_review` oznacza zakończoną implementację oczekującą na zbiorcze review: nie implementuj jej ponownie i nie traktuj jako zatwierdzonej. Zachowaj bazę i licznik rund przy wznowieniu. Wznawiaj rozpoczętą pracę; nie powtarzaj zatwierdzonego milestone'u z powodu starego statusu. Jeśli commit się nie udał lub sesja urwała się przed checkpointem, ustal pozostały zakres z diffu i kodu. Nie zgaduj brakującego wyniku review.
6. Jeśli skrypt zgłasza przekroczenie limitu, uwzględnij `$codex-flow-compact-context` jako zalecany krok, ale nie modyfikuj plików podczas resume.

Zwróć krótki brief: cel projektu, aktualny zakres, co zrobiono, ostatnią walidację, blokery, najbliższy krok, pliki potrzebne do jego wykonania i ewentualną potrzebę kompakcji.
