---
name: codex-flow-implement-milestone
description: Implementuj jeden konkretny milestone lub jasno ograniczone zadanie z ROADMAP.md. Użyj, gdy użytkownik wskazuje identyfikator albo nazwę milestone'u i oczekuje zmian w kodzie wraz z walidacją, bez automatycznego commita lub pusha.
---

# Implementacja milestone'u

Statusy, review i checkpointy prowadź według [kontraktu flow](../codex-flow-run-roadmap/references/flow-contract.md). W `run-roadmap` obowiązuje jego zakaz delegowania i zbiorcze review na końcu.

1. Przeczytaj `AGENTS.md`, `STATUS.md`, wskazany fragment `ROADMAP.md` oraz istotne sekcje `spec.md`.
2. Sprawdź pliki kodu i testów związane z zakresem. Nie czytaj niepowiązanych obszarów.
3. Dla większej lub niejasnej zmiany podaj krótko: cel, zakres, poza zakresem, kryteria akceptacji, walidację i warunki zatrzymania.
4. Jeśli użytkownik nie wskazał milestone'u, nie wybieraj samodzielnie spośród kilku sensownych kandydatów. Poproś o decyzję.
5. Prowadzący zadanie zapisuje checkpoint rozpoczęcia i `in_progress` w roadmapie. Zaimplementuj wyłącznie uzgodniony zakres małymi, precyzyjnymi zmianami.
6. Dodaj lub popraw testy odpowiadające ryzyku zmiany.
7. Uruchom komendy walidacyjne z repo, domyślnie `./scripts/verify.sh`.
8. Zaktualizuj `STATUS.md`, jeżeli zmiana jest istotna lub praca pozostaje niedomknięta. Poza `run-roadmap`, gdy wykonujesz osobno zlecony fragment jako subagent, przekaż wynik głównemu agentowi odpowiedzialnemu za wspólny status i roadmapę.

Przy samodzielnym milestone'ie prowadzący uruchamia wymagane review po implementacji i walidacji, a następnie zapisuje `done` zgodnie z kontraktem. Jeśli review oczekuje na wykonanie, zachowuje `implemented_pending_review` i `in_progress`; przy blokadzie zapisuje `blocked`. Subagent przekazuje fakty prowadzącemu zamiast edytować wspólne STATUS i ROADMAP. W `run-roadmap` prowadzący odracza review do końca całej implementacji.

Nie wykonuj commita ani pusha. Podaj zmienione pliki, walidacje, ograniczenia i ewentualne problemy wymagające review.
