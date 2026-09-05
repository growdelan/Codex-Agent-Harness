# Codex Flow — lekki harness dla projektów Python

Szablon współpracy z Codexem: trwałe zasady, planowanie z PRD, małe milestone'y, walidacja i niezależne review. Główna rozmowa implementuje; osobny reviewer sprawdza wynik.

## Użycie szablonu

Skopiuj `.agents/`, `.codex/`, `docs/`, `prd/`, `scripts/`, `AGENTS.md`, `ROADMAP.md`, `STATUS.md` i `spec.md` do projektu. Nie nadpisuj jego istniejących ustaleń. Pliki `STATUS.md`, `ROADMAP.md` i `spec.md` pozostają pustymi szablonami do wypełnienia w docelowym projekcie. Dopasuj komendy i konwencje do technologii; domyślny profil to Python z `uv`.

Dla nowego produktu:

1. `$codex-flow-create-prd` — wywiad i zapis wymagań w `prd/`.
2. `$codex-flow-plan-from-prd` — specyfikacja i mierzalna roadmapa. Milestone 0 ustanawia uruchamialny projekt i rzeczywistą walidację.
3. `$codex-flow-implement-milestone` — jeden wskazany milestone; albo `$codex-flow-run-roadmap` — cała wykonalna roadmapa z niezależnym review i lokalnymi commitami.
4. `$codex-flow-publish` — synchronizacja dokumentacji i przygotowanie, commit lub push zgodnie z poleceniem.

Małe, jasno określone zadanie wykonuj bez obowiązkowego PRD i milestone'u: oczekiwany wynik → zmiana → adekwatna walidacja. Większa lub ryzykowna zmiana wymaga niezależnego review. Trwałe decyzje i niedomkniętą pracę zapisz w dokumentacji.

## Skille

| Skill | Zastosowanie |
|---|---|
| `codex-flow-resume` | Odtworzenie faktycznego stanu z checkpointu i Git bez zmian w plikach |
| `codex-flow-create-prd` | Wywiad produktowy, jedno pytanie naraz, pierwszy lub kolejny PRD |
| `codex-flow-plan-from-prd` | PRD → specyfikacja i małe, weryfikowalne milestone'y |
| `codex-flow-implement-milestone` | Implementacja jednego wskazanego milestone'u i walidacja |
| `codex-flow-review` | Niezależne review przez osobnego agenta |
| `codex-flow-address-review` | Weryfikacja uwag i minimalne zasadne poprawki |
| `codex-flow-run-roadmap` | Implementacja w głównej rozmowie, review, checkpoint i lokalny commit każdego milestone'u |
| `codex-flow-compact-context` | Porządkowanie dokumentów bez utraty aktywnych ustaleń |
| `codex-flow-publish` | Synchronizacja dokumentacji i publikacja w autoryzowanym zakresie |

## Agenci i autonomiczna praca

- Główny agent implementuje, waliduje, naprawia zasadne problemy i utrzymuje stan projektu.
- `reviewer` — niezależne review read-only, `gpt-6-astra`, reasoning `medium`. Nowy agent dla każdego milestone'u, ten sam agent do kolejnych rund poprawek.
- `sol_implementer` — opcjonalne zamknięte zadania, gdy delegowanie daje konkretną korzyść; `gpt-5.6-sol`, reasoning `medium`.
- `planner` — opcjonalna niezależna analiza wymagań i planu, read-only.

Przebieg i warunki zatrzymania pętli definiuje [run-roadmap](.agents/skills/codex-flow-run-roadmap/SKILL.md). Aktualizuje ona `STATUS.md` i statusy roadmapy na bieżąco. Pełna redakcja specyfikacji i README może poczekać do finalizacji; wymagane artefakty produktu są realizowane wraz z milestone'em.

Checkpoint zawiera bazę porównania, review, walidację, blokery i następny krok. Commit milestone'u utrwala także jego checkpoint. Przy powrocie `$codex-flow-resume` porównuje dokumentację z Git, uwzględnia pracę rozpoczętą i nie polega wyłącznie na historii rozmowy.

## Walidacja

Uruchom `./scripts/verify.sh`. Skrypt sprawdza rozmiar dokumentów i dostępność `uv`, następnie uruchamia testy `unittest`, jeśli istnieje katalog `tests/`. Dodatkowe kontrole należy skonfigurować jawnie w docelowym projekcie.

Sam kod wyjścia `0` nie potwierdza, że wykonano kontrole produktu: brak katalogu `tests/` powoduje pominięcie testów, a discovery może znaleźć zero przypadków. Agent powinien sprawdzić rzeczywisty wynik i zgłosić brak wykonanych kontroli zamiast uznać go za pozytywną walidację produktu.

W Milestone 0 dostosuj walidację do testów, smoke testu, lintowania lub builda właściwych dla projektu. Nie dodawaj pustych testów, żeby uzyskać zielony wynik.

## Pamięć i limity kontekstu

- `AGENTS.md`: trwałe reguły repozytorium.
- `spec.md`: aktualne zachowanie i decyzje; szczegóły w `docs/spec/` i `docs/decisions/`.
- `ROADMAP.md`: zakres, kryteria, walidacja, zależności i statusy `planned`, `in_progress`, `done`, `blocked`.
- `STATUS.md`: krótki checkpoint i najbliższy krok; historyczne checkpointy pozostają w Git.

`./scripts/check-context-size.sh` ostrzega po przekroczeniu 150 linii / 12 KB dla STATUS, 350 / 30 KB dla ROADMAP i 500 / 40 KB dla spec. Ostrzeżenie nie blokuje walidacji. Progi można zmienić zmiennymi `STATUS_MAX_LINES`, `STATUS_MAX_BYTES`, `ROADMAP_MAX_LINES`, `ROADMAP_MAX_BYTES`, `SPEC_MAX_LINES`, `SPEC_MAX_BYTES`.

Kompakcja następuje podczas planowania lub na jawne polecenie. Ukończone szczegóły roadmapy trafiają do `docs/archive/roadmap/`; aktualna specyfikacja pozostaje poza archiwum. Resume czyta tylko kontekst potrzebny do następnej decyzji.

## Zasady commitów i publikacji

Zwykła implementacja nie autoryzuje commita. Jawne zlecenie `$codex-flow-run-roadmap`, także równoważne polecenie wykonania całej roadmapy, obejmuje lokalny commit każdego zatwierdzonego milestone'u; możesz wyraźnie wykluczyć commity. Push wymaga osobnego polecenia.

`$codex-flow-publish`: „przygotuj” synchronizuje dokumentację bez stagingu i commita, „commit” tworzy commit bez pusha, „push” lub „opublikuj” wykonuje push i potrzebny commit po walidacji. Jeśli korzystasz z `github:yeet`, uruchom go po przygotowaniu przez publish. Żaden workflow nie włącza do commita zmian spoza uzgodnionego zakresu.
