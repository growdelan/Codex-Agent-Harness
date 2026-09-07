# Codex Flow — lekki harness dla projektów Python

Szablon współpracy z Codexem: trwałe zasady, planowanie z PRD, małe milestone'y, walidacja i review. Główna rozmowa implementuje wszystkie otwarte milestone’y, a następnie sprawdza cały wynik w tym samym wątku.

## Użycie szablonu

Skopiuj `.agents/`, `.codex/`, `docs/`, `prd/`, `scripts/`, `AGENTS.md`, `ROADMAP.md`, `STATUS.md` i `spec.md` do projektu. Nie nadpisuj jego istniejących ustaleń. Pliki `STATUS.md`, `ROADMAP.md` i `spec.md` pozostają pustymi szablonami do wypełnienia w docelowym projekcie. Dopasuj komendy i konwencje do technologii; domyślny profil to Python z `uv`.

Dla nowego produktu:

1. `$codex-flow-create-prd` — wywiad i zapis wymagań w `prd/`.
2. `$codex-flow-plan-from-prd` — specyfikacja i mierzalna roadmapa. Milestone 0 ustanawia uruchamialny projekt i rzeczywistą walidację.
3. `$codex-flow-implement-milestone` — jeden wskazany milestone; albo `$codex-flow-run-roadmap` — wszystkie otwarte milestone’y bez commitów, potem review w tym samym wątku.
4. `$codex-flow-publish` — synchronizacja dokumentacji i przygotowanie, commit lub push zgodnie z poleceniem.

Małe, jasno określone zadanie wykonuj bez obowiązkowego PRD i milestone'u: oczekiwany wynik → zmiana → adekwatna walidacja. Review odbywa się w bieżącym wątku; niezależnego custom reviewera można zlecić osobno. Trwałe decyzje i niedomkniętą pracę zapisz w dokumentacji.

## Skille

| Skill | Zastosowanie |
|---|---|
| `codex-flow-resume` | Odtworzenie faktycznego stanu z checkpointu i Git bez zmian w plikach |
| `codex-flow-create-prd` | Wywiad produktowy, jedno pytanie naraz, pierwszy lub kolejny PRD |
| `codex-flow-plan-from-prd` | PRD → specyfikacja i małe, weryfikowalne milestone'y |
| `codex-flow-implement-milestone` | Implementacja jednego wskazanego milestone'u i walidacja |
| `codex-flow-review` | Review wskazanego zakresu w bieżącym wątku, bez delegowania |
| `codex-flow-address-review` | Weryfikacja uwag i minimalne zasadne poprawki |
| `codex-flow-run-roadmap` | Cała roadmapa → review całości → maksymalnie 3 rundy poprawek |
| `codex-flow-compact-context` | Porządkowanie dokumentów bez utraty aktywnych ustaleń |
| `codex-flow-publish` | Synchronizacja dokumentacji i publikacja w autoryzowanym zakresie |

## Agenci i autonomiczna praca

- Główny agent implementuje, waliduje, naprawia zasadne problemy i utrzymuje stan projektu.
- `reviewer` — niezależne review read-only, `gpt-6-astra`, reasoning `medium`. Uruchamiany wyłącznie na jawne polecenie użytkownika; `run-roadmap` nigdy go nie wywołuje.
- `implementer` — opcjonalne zamknięte zadania, gdy delegowanie daje konkretną korzyść; `gpt-6-astra`, reasoning `low`.
- `planner` — opcjonalna niezależna analiza wymagań i planu, read-only; `gpt-6-astra`, reasoning `medium`.

Przebieg i warunki zatrzymania pętli definiuje [run-roadmap](.agents/skills/codex-flow-run-roadmap/SKILL.md). Aktualizuje ona `STATUS.md` i statusy roadmapy na bieżąco. Pełna redakcja specyfikacji i README może poczekać do finalizacji; wymagane artefakty produktu są realizowane wraz z milestone'em.

Najpierw powstają implementacje wszystkich otwartych milestone’ów, a po walidacji `codex-flow-review` ocenia cały worktree względem stałej bazy `review_base`, w tym staged, unstaged i nowe pliki. Jeśli są poprawki, `codex-flow-address-review` je wprowadza i review całości jest ponawiane — maksymalnie trzy rundy poprawek łącznie. Całość odbywa się w tym samym wątku, bez stagingu, commitów i pusha.

Checkpoint zawiera stałą bazę porównania, fazę, listę wyników milestone’ów, review, licznik rund, walidację, blokery i następny krok. Implementacja oczekująca na review ma wynik `implemented_pending_review` w checkpointie i status `in_progress` w roadmapie; `done` otrzymuje po pozytywnej ocenie. Blokady nie są pomijane: pętla realizuje pozostałe niezależne elementy i zatrzymuje się przed review całości, jeśli nie można dokończyć całej roadmapy. Checkpoint pozostaje w worktree i zachowuje zbiorczy stan aż do osobnej publikacji. Przy powrocie `$codex-flow-resume` porównuje dokumentację z Git, uwzględnia pracę rozpoczętą i nie polega wyłącznie na historii rozmowy.

## Walidacja

Uruchom `./scripts/verify.sh`. Skrypt sprawdza rozmiar dokumentów i dostępność `uv`, następnie uruchamia testy `unittest`, jeśli istnieje katalog `tests/`. Dodatkowe kontrole należy skonfigurować jawnie w docelowym projekcie.

Sam kod wyjścia `0` nie potwierdza, że wykonano kontrole produktu: brak katalogu `tests/` powoduje pominięcie testów, a discovery może znaleźć zero przypadków. Agent powinien sprawdzić rzeczywisty wynik i zgłosić brak wykonanych kontroli zamiast uznać go za pozytywną walidację produktu.

W Milestone 0 dostosuj walidację do testów, smoke testu, lintowania lub builda właściwych dla projektu. Nie dodawaj pustych testów, żeby uzyskać zielony wynik.

## Pamięć i limity kontekstu

- `AGENTS.md`: trwałe reguły repozytorium.
- `spec.md`: aktualne zachowanie i decyzje; szczegóły w `docs/spec/` i `docs/decisions/`.
- `ROADMAP.md`: zakres, kryteria, walidacja, zależności i statusy `planned`, `in_progress`, `done`, `blocked`.
- `STATUS.md`: krótki checkpoint i najbliższy krok; podczas `run-roadmap` zbiorczy stan pozostaje w worktree.

`./scripts/check-context-size.sh` ostrzega po przekroczeniu 150 linii / 12 KB dla STATUS, 350 / 30 KB dla ROADMAP i 500 / 40 KB dla spec. Ostrzeżenie nie blokuje walidacji. Progi można zmienić zmiennymi `STATUS_MAX_LINES`, `STATUS_MAX_BYTES`, `ROADMAP_MAX_LINES`, `ROADMAP_MAX_BYTES`, `SPEC_MAX_LINES`, `SPEC_MAX_BYTES`.

Kompakcja następuje podczas planowania lub na jawne polecenie. Ukończone szczegóły roadmapy trafiają do `docs/archive/roadmap/`; aktualna specyfikacja pozostaje poza archiwum. Resume czyta tylko kontekst potrzebny do następnej decyzji.

## Zasady commitów i publikacji

`codex-flow-run-roadmap` nie wykonuje stagingu, commitów ani pusha na żadnym etapie. Zakończenie roadmapy i review pozostawia zmiany w worktree. Commit i push wymagają osobnego polecenia publikacji.

`$codex-flow-publish`: „przygotuj” synchronizuje dokumentację bez stagingu i commita, „commit” tworzy commit bez pusha, „push” lub „opublikuj” wykonuje push i potrzebny commit po walidacji. Jeśli korzystasz z `github:yeet`, uruchom go po przygotowaniu przez publish. Żaden workflow nie włącza do commita zmian spoza uzgodnionego zakresu.
