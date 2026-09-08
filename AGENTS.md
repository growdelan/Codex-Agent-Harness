# AGENTS.md

## Język

- Komunikuj się z użytkownikiem wyłącznie po polsku.
- Dodawaj komentarze w kodzie tylko wtedy, gdy wyjaśniają nieoczywistą logikę.

## Kontekst projektu

- Obowiązujące wymagania i trwałe decyzje zapisuj w `spec.md`; stan wdrożenia potwierdzaj w roadmapie i kodzie.
- Wspólne zasady statusów, checkpointów, review i publikacji definiuje [kontrakt flow](.agents/skills/codex-flow-run-roadmap/references/flow-contract.md). Skille opisują kroki poszczególnych zadań.
- Plan i statusy prac utrzymuj w `ROADMAP.md`.
- Bieżący stan, ostatnią walidację, blokery i następny krok zapisuj w `STATUS.md`.
- Czytaj tylko pliki potrzebne do aktualnej decyzji. Przy kontynuacji zacznij od `STATUS.md` i właściwego fragmentu `ROADMAP.md`.
- Traktuj limity kontekstu jako progi ostrzegawcze: `STATUS.md` 150 linii / 12 KB, `ROADMAP.md` 350 linii / 30 KB, `spec.md` 500 linii / 40 KB.
- Gdy dokument przekracza próg, wykonaj kompakcję automatycznie tylko podczas `$codex-flow-plan-from-prd` albo jawnie uruchomionego `$codex-flow-compact-context`. W pozostałych workflow zgłoś ją jako osobny rekomendowany krok i nie rozszerzaj bieżącego diffu.
- Nie czytaj `docs/archive/` podczas zwykłego resume, planowania ani implementacji, chyba że bieżąca decyzja wymaga historii.
- Ukończone szczegóły roadmapy archiwizuj w `docs/archive/roadmap/`; szczegóły aktualnej specyfikacji dziel między `docs/spec/` i `docs/decisions/`, zachowując `spec.md` jako indeks obowiązujących wymagań i decyzji.

## Środowisko Python

- Używaj `uv` do środowiska i zależności. Dodawaj zależności przez `uv add <pakiet>`.
- Nie twórz alternatywnych virtualenvów ani zależności „na zapas”.
- Uzasadniaj nowe zależności w sekcji `## Decyzje techniczne` w `spec.md` albo linkowanym z niej dokumencie szczegółowym.
- Kod aplikacji trzymaj w `src/`, a testy w `tests/`.
- Preferuj jeden główny entrypoint opisany w `README.md`.

## Implementacja

- Ustal zakres i kryteria akceptacji przed większą lub niejasną zmianą.
- Wprowadzaj małe, precyzyjne zmiany bez szerokich refaktorów „przy okazji”.
- Nie rozszerzaj zakresu milestone'u bez uzasadnienia i aktualizacji planu.
- Nie przechowuj sekretów w repo. Używaj zmiennych środowiskowych i dokumentuj je w `README.md`.
- Stosuj 4 spacje, `snake_case` dla modułów i funkcji oraz `PascalCase` dla klas.

## Walidacja i review

- Używaj komend zdefiniowanych przez repo. Podstawowa komenda tego szablonu to `./scripts/verify.sh`.
- Testy i smoke testy nie mogą wymagać prawdziwych sekretów ani niestabilnych usług zewnętrznych.
- Dodawaj test jednostkowy tylko wtedy, gdy chroni ważne zachowanie, realną regresję albo prawdopodobny błąd; każdy nowy test musi wskazywać konkretną, realistyczną awarię, którą wykrywa.
- Preferuj rozszerzenie istniejącego testu i najmniejszy reprezentatywny zestaw przypadków zamiast tworzenia podobnych testów dla każdej kombinacji danych.
- Dla stabilnie odtwarzalnego błędu dodaj minimalny test regresyjny, jeśli istniejący test nie chroni już tego zachowania.
- Nie testuj getterów, stałych, prostych przypisań, zachowania frameworka, szczegółów implementacji ani mocków, które potwierdzają wyłącznie własną konfigurację.
- Nie dodawaj testów dla czysto hipotetycznych przypadków bez realnej drogi wystąpienia. Brak nowego testu jest poprawny dla dokumentacji, kosmetyki, prostego okablowania i zachowania już wystarczająco pokrytego.
- Nie traktuj liczby testów ani pokrycia jako celu. Review nie może żądać dodatkowego testu bez wskazania wartościowego zachowania lub realistycznego ryzyka, które pozostaje niechronione.
- Po istotnej zmianie zapisz w `STATUS.md` wykonaną walidację i jej wynik.
- Nie używaj `STATUS.md` jako dziennika. Zachowuj bieżący stan, ostatnią istotną walidację, aktywne ryzyka i następny krok.
- Dla ryzykownych lub większych zmian wykonaj samoocenę diffu. Niezależne review wykonuje osobny agent wyłącznie na jawne zlecenie użytkownika, poza `run-roadmap`. Zasady wymaganej oceny przed publikacją określa kontrakt flow.
- Nie ukrywaj nieprzechodzącej walidacji ani problemów blokujących.

## Git i dokumentacja

- Nie wykonuj commita ani pusha bez jawnego polecenia użytkownika.
- Przed publikacją sprawdź `git status --short`, diff i wynik walidacji.
- Aktualizuj `README.md` tylko wtedy, gdy zmienia się uruchamianie, konfiguracja, użycie lub ważne zachowanie systemu.
- Nie nadpisuj zmian użytkownika ani nie włączaj do commita zmian spoza uzgodnionego zakresu.
