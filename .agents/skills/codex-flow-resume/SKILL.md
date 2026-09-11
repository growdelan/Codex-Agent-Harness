---
name: codex-flow-resume
description: Odtwórz stan projektu i wskaż następny krok bez zmian w plikach. Użyj na prośbę o status lub rozpoznanie przerwanej pracy; przy zleceniu implementacji rozpoznanie jest etapem wstępnym, po którym kontynuuj zleconą pracę.
---

# Wznowienie projektu

1. Uruchom `./scripts/check-context-size.sh`, a następnie przeczytaj `STATUS.md`.
2. Z `ROADMAP.md` odczytaj tylko milestone'y `in_progress`, `planned`, `blocked` oraz krótki indeks ukończonych prac. Nie czytaj archiwum domyślnie.
3. Potraktuj `spec.md` jako indeks. Doczytaj tylko wskazane sekcje lub dokumenty z `docs/spec/` i `docs/decisions/`, które są potrzebne do najbliższej decyzji.
4. Doczytaj `AGENTS.md`, diff lub kod tylko wtedy, gdy są potrzebne do zweryfikowania bieżącego stanu.
5. Porównaj checkpoint z Git według [kontraktu flow](../codex-flow-run-roadmap/references/flow-contract.md): odróżnij aktywny przebieg, ukończony wynik bez commita i wynik już commitowany. Sprawdź zakres, własność zmian, wymagane review i fingerprint. Zachowaj bazę i licznik aktywnej pracy; nie powtarzaj `implemented_pending_review` ani nie resetuj zakończonego przebiegu przed rozpoznaniem publikacji. Przy brakującym checkpointie ustal fakty z diffu i kodu, bez zgadywania decyzji review. To rozpoznanie read-only: wskaż fazę i następny krok, ale nie implementuj i nie zapisuj zmian.
6. Jeśli skrypt zgłasza przekroczenie limitu, uwzględnij `$codex-flow-compact-context` jako zalecany krok, ale nie modyfikuj plików podczas resume.

Zwróć krótki brief: cel projektu, aktualny zakres, co zrobiono, ostatnią walidację, blokery, najbliższy krok, pliki potrzebne do jego wykonania i ewentualną potrzebę kompakcji.
