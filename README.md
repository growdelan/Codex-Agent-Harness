# Codex Flow — lekki harness dla projektów Python

Szablon współpracy z Codexem: wymagania z PRD, małe milestone’y, walidacja i review. Możesz wykonać pojedynczy milestone albo całą roadmapę w jednym wątku. Pliki tego repozytorium są elementami szablonu; nie zapisuj w nich stanu prac nad samym harnessem.

## Instalacja w projekcie

1. Skopiuj `.agents/`, `.codex/`, `prd/`, `scripts/`, `AGENTS.md`, `ROADMAP.md`, `STATUS.md` i `spec.md`. Scal istniejące ustalenia zamiast je nadpisywać. Szablony pamięci wypełniaj dopiero dla produktu docelowego; foldery `docs/spec/`, `docs/decisions/` i `docs/archive/roadmap/` twórz, gdy pojawią się potrzebne dokumenty.
2. Scal reguły z [.gitignore](.gitignore), szczególnie `.venv/`, cache i `.env`; pozostaw możliwość śledzenia `.env.example`. Przenieś do README projektu potrzebne instrukcje workflow i walidacji. Nie zastępuj jego opisu produktu tym README.
3. Zainstaluj `uv` według [instrukcji producenta](https://docs.astral.sh/uv/getting-started/installation/) i sprawdź `uv --version`. Narzędzia harnessu używają Pythona 3.11+ przez `uv`, bez zewnętrznych bibliotek. Dostosuj konwencje i walidację produktu do jego technologii.
4. Sprawdź prawa wykonywania skryptów `.sh` po kopiowaniu i uruchom `./scripts/verify-harness.sh`. W Milestone 0 skonfiguruj rzeczywistą walidację produktu w `scripts/verify.sh`.

## Flow

1. `$codex-flow-create-prd` — wywiad i pierwszy lub kolejny dokument w `prd/`.
2. `$codex-flow-plan-from-prd` — wymagania, mapowanie PRD i mierzalna roadmapa. Dla nowego projektu planuje Milestone 0: uruchamialny rezultat i rzeczywistą walidację; nie implementuje go.
3. `$codex-flow-implement-milestone` — wskazany milestone; albo `$codex-flow-run-roadmap` — wszystkie otwarte milestone’y, potem samoocena całości i maksymalnie trzy rundy poprawek.
4. `$codex-flow-publish` — przygotowanie, commit lub push w jawnym zakresie autoryzacji.

Małe, jasne zadanie może pominąć PRD i milestone: oczekiwany wynik → zmiana → adekwatna walidacja. Szczegóły statusów, własności zmian, checkpointu i autoryzacji określa [kontrakt flow](.agents/skills/codex-flow-run-roadmap/references/flow-contract.md); kolejność i warunki zatrzymania całej pętli — [run-roadmap](.agents/skills/codex-flow-run-roadmap/SKILL.md).

## Skille i agenci

| Skill | Zastosowanie |
|---|---|
| `codex-flow-resume` | Odtworzenie stanu i następnego kroku, bez edycji plików |
| `codex-flow-create-prd` | Wywiad produktowy i zapis PRD |
| `codex-flow-plan-from-prd` | PRD → specyfikacja, indeks źródeł i milestone’y |
| `codex-flow-implement-milestone` | Implementacja jednego milestone’u i walidacja |
| `codex-flow-address-review` | Minimalne zasadne poprawki po review |
| `codex-flow-run-roadmap` | Cała roadmapa → samoocena → maksymalnie trzy rundy poprawek |
| `codex-flow-compact-context` | Porządkowanie dokumentacji z ochroną aktywnego checkpointu |
| `codex-flow-publish` | Kontrole i publikacja w uzgodnionym zakresie |

`run-roadmap` nie deleguje żadnego etapu i pozostawia wynik bez stagingu, commita i pusha. Poza nim dostępni są opcjonalni agenci: implementer do zamkniętej implementacji, planner do analizy read-only oraz reviewer do niezależnej oceny wyłącznie na jawne polecenie użytkownika. Konfiguracje ról znajdują się w [.codex/agents](.codex/agents).

## Walidacja

- `./scripts/verify-harness.sh` sprawdza składnię skryptów shellowych harnessu, rozmiary pamięci, wymagane pola konfiguracji dziewięciu skillów i trzech agentów harnessu, obsługiwane lokalne linki Markdown. Nie narzuca formatu innym skillom ani agentom projektu. Nie ocenia semantycznej zgodności instrukcji — ta wymaga review.
- `./scripts/verify.sh` uruchamia kontrolę harnessu i jawnie skonfigurowane kontrole produktu. Domyślnie próbuje `unittest`, gdy istnieje katalog `tests/`. W Milestone 0 dopasuj ten fragment do smoke testu, testów, lintowania lub builda projektu.
- Brak `tests/` albo zero znalezionych przypadków nie jest pozytywną walidacją produktu, nawet gdy kod wyjścia wynosi `0`.
- `scripts/review-snapshot.py` identyfikuje treść jawnie wskazanych plików do porównania z ocenioną wersją; jego użycie i wyjątki dokumentacyjne opisuje kontrakt flow.

## Pamięć i publikacja

`spec.md` opisuje obowiązujące wymagania i decyzje; stan wdrożenia wynika z ROADMAP, STATUS i kodu. ROADMAP mapuje PRD na milestone’y. STATUS jest krótkim checkpointem, z opcjonalną sekcją przebiegu. Szczegóły specyfikacji trafiają do `docs/spec/` i `docs/decisions/`, a ukończone nieaktywne plany do `docs/archive/roadmap/`.

Kompakcja działa podczas planowania albo na jawne polecenie. Progi są ostrzegawcze; ich wartości i zmienne do nadpisania są w [check-context-size.sh](scripts/check-context-size.sh). Nie usuwaj nieopublikowanego checkpointu, aby zmieścić się w limicie.

Znaczenie poleceń `przygotuj`, `commit`, `push` i `opublikuj` definiuje tabela w kontrakcie flow. Sam `push` wysyła istniejące commity; nie autoryzuje nowego commita. Publikacja nie uruchamia review, ale respektuje review wymagane przez wcześniejszy workflow i znane blokery.
