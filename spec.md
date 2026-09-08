# Specyfikacja techniczna

Ten szablon opisuje obowiązujące wymagania i decyzje projektu docelowego. Nie potwierdza wdrożenia: stan realizacji sprawdzaj w ROADMAP, STATUS i kodzie. Wspólne reguły utrzymania opisuje [kontrakt flow](.agents/skills/codex-flow-run-roadmap/references/flow-contract.md).

## Cel

- Problem:
- Użytkownicy:
- Oczekiwany rezultat:
- Poza zakresem:

## Zakres funkcjonalny

Opisz najważniejsze przypadki użycia, przepływy oraz jawne ograniczenia bez niepotrzebnych szczegółów implementacyjnych. Planowane zmiany powiąż ze źródłowym PRD i milestone’em; wyraźnie odróżnij je od wdrożonego zachowania.

## Architektura i przepływ danych

Opisz komponenty, ich odpowiedzialności, granice oraz przepływ danych na poziomie potrzebnym do podejmowania decyzji.

## Decyzje techniczne

Każda istotna decyzja powinna zawierać:

- Decyzja:
- Uzasadnienie:
- Konsekwencje:
- Dotyczy PRD / milestone'u:
- Zastępuje / zastąpiona przez (jeśli dotyczy):

Dokumentuj tutaj nowe zależności, zmianę granic komponentów, sposobu uruchamiania lub istotnego zachowania systemu.

## Dokumenty szczegółowe

Gdy specyfikacja rośnie, zachowaj tutaj krótki indeks aktualnych dokumentów zamiast kopiować ich pełną treść:

- Obszary domenowe i kontrakty: `docs/spec/`
- Samodzielne decyzje techniczne: `docs/decisions/`

Dokumenty szczegółowe są częścią aktualnej specyfikacji, a nie archiwum. Linkuj tylko pliki istniejące i potrzebne do zrozumienia systemu.

## Jakość i kryteria akceptacji

- Każdy milestone ma mierzalne kryteria akceptacji.
- Testy nie używają prawdziwych sekretów ani niestabilnych usług zewnętrznych.
- Walidacje odpowiadają ryzyku zmiany i są zapisywane w `STATUS.md`.
- Wymagane review i znane problemy blokujące rozstrzygaj przed publikacją zgodnie z kontraktem flow.

## Zasady ewolucji

- ROADMAP aktualizuj przy zmianie milestone’u, zależności lub przyszłego planu. Małe, jasne zadania nie wymagają tworzenia PRD ani milestone’u tylko dla formalności.
- Trwałe zmiany zachowania lub architektury aktualizują `spec.md`.
- README aktualizuj tylko przy zmianie sposobu użycia, uruchamiania lub konfiguracji.
- Refaktory wykonuj w zakresie bieżącego zadania albo jako osobny milestone.

## Status specyfikacji

- Data utworzenia:
- Ostatnia aktualizacja:
- Aktualny zakres obowiązywania:
