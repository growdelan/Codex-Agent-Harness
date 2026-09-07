---
name: codex-flow-run-roadmap
description: Wykonaj wszystkie otwarte milestone'y z ROADMAP.md, następnie review całości w tym samym wątku i maksymalnie trzy rundy poprawek z ponownym review. Nie wykonuj stagingu, commitów ani pusha i nie wywołuj subagenta reviewera.
---

# Wykonanie roadmapy

## Przygotowanie i zakres

1. Przeczytaj potrzebny kontekst projektu, `STATUS.md`, aktywną roadmapę i istotne wymagania ze specyfikacji. Sprawdź Git i rozmiar kontekstu; nie czytaj archiwum domyślnie.
2. Zbierz wszystkie rzeczywiste otwarte milestone'y: `planned`, `in_progress` oraz `blocked`. Pomiń szablony i zakończone `done`. Dla `blocked` sprawdź, czy blokada nadal istnieje; rozwiązane blokady pozwalają wznowić pracę. Ustal kolejność zależności i nie dodawaj nowych funkcji poza uzgodnioną roadmapą.
3. Porównaj checkpoint z Git. Zapisz stały bazowy commit całego przebiegu (`review_base`), listę milestone'ów oraz początkowe zmiany użytkownika. Nie przesuwaj tej bazy po milestone'ach ani poprawkach. Przy wznowieniu użyj zapisanej bazy i fazy, zamiast rozpoczynać nowy przebieg.
4. Pokaż kolejność i kontynuuj bez dodatkowego potwierdzenia, jeśli zakres jest jasny. Cały workflow pozostawia wynik w worktree: nie wykonuj stagingu, commitów ani pusha, także po poprawkach i przy finalizacji. Publikacja jest osobnym krokiem na jawne polecenie użytkownika.

## Odpowiedzialność i dokumentacja

Główny agent prowadzi implementację i cały cykl review → poprawki w tej samej rozmowie. `run-roadmap` nigdy nie wywołuje custom agenta `reviewer`, także przez inny skill. Nie zastępuj go innym subagentem do review. Custom reviewer jest dostępny tylko na osobne, jawne polecenie użytkownika, poza tą pętlą. Review we własnym wątku jest samooceną, nie niezależnym review.

Opcjonalny `implementer` może wykonać zamknięty fragment implementacji przy konkretnej korzyści z delegowania. Przekaż zakres i własność plików; główny agent odbiera wynik i odpowiada za wspólny checkpoint.

Aktualizuj checkpoint i statusy na bieżąco. Pełną redakcję specyfikacji i README można odłożyć do `$codex-flow-publish`, zachowując decyzje do przekazania dalej. Dokumenty będące kryteriami akceptacji są częścią implementacji i review. Sam brak odroczonej redakcyjnej synchronizacji nie blokuje oceny.

## Faza 1: wszystkie milestone'y

1. Dla każdego wykonalnego milestone'u potwierdź zakres, kryteria i walidację. Zapisz `in_progress` w roadmapie i checkpoint rozpoczęcia.
2. Użyj `$codex-flow-implement-milestone`, uruchom adekwatne kontrole i sprawdź wynik. Brak wykonanych kontroli nie jest pozytywną walidacją.
3. Po implementacji i pozytywnej walidacji zapisz w checkpointie wynik `implemented_pending_review`. Pozostaw zmiany w worktree. W roadmapie pozostaw `in_progress` do końcowego review. Zachowaj zbiorczy checkpoint wszystkich wyników w worktree.
4. Przejdź do kolejnego milestone'u bez review pośredniego i bez pytania o kontynuację. Checkpoint pozwala odróżnić zaimplementowane elementy oczekujące na review od jeszcze nierozpoczętych.
5. Jeśli milestone jest zablokowany, zapisz przyczynę i kontynuuj inne niezależne, wykonalne elementy. Nie realizuj jego zależnych milestone'ów. Gdy nie ma dalszej wykonalnej pracy, a pozostały blokady, zapisz częściowy wynik i zatrzymaj workflow przed review całości. Nie ogłaszaj ukończenia roadmapy.

## Faza 2: review całości i poprawki

1. Po implementacji wszystkich milestone'ów z uzgodnionego zakresu uruchom pełną dostępną walidację integracji. Napraw błędy mieszczące się w zakresie; przy nierozwiązywalnej blokadzie zatrzymaj pracę. Po pozytywnej walidacji zapisz checkpoint fazy `review`, sprawdź pełny zakres zmian w worktree i przejdź do review bez commita. Nie obejmuj oceną wcześniejszych zmian użytkownika.
2. Użyj `$codex-flow-review` w tym samym wątku. Oceniaj cały aktualny zakres względem `review_base`, włącznie z integracją milestone'ów: zmiany staged, unstaged oraz zawartość nowych plików należących do zadania. Sam diff commitów ani samo `git diff` nie obejmują pełnego zakresu. Odczytaj `git diff <SHA_z_review_base> --` (podstaw zapisany SHA), `git status --short` i nowe pliki bez dodawania ich do indeksu. Wyłącz wcześniejsze zmiany użytkownika.
3. Wymagaj `DECISION: APPROVED` albo `DECISION: CHANGES_REQUIRED`. Zapisz raport, oceniony zakres plików, rundę i wynik w checkpointie. Review rozpoczynaj dopiero po zakończeniu całej uzgodnionej implementacji.
4. Jeśli istnieją zasadne poprawki z review, użyj `$codex-flow-address-review` w tym samym wątku, przekazując pełny raport i zakres całego przebiegu. Napraw zasadne problemy, odpowiedz na każde znalezisko i ponów adekwatną walidację. Po pozytywnej walidacji zapisz wynik w checkpointie, następnie ponownie użyj `$codex-flow-review` dla całego zakresu od tej samej bazy.
5. Limit wynosi trzy rundy poprawek łącznie dla całego przebiegu: pierwsze review → poprawki 1 → review → poprawki 2 → review → poprawki 3 → ostatnie review. Wznowienie nie zeruje licznika. Po trzeciej rundzie nie uruchamiaj czwartej. Jeśli weryfikacja uwag nie wymaga zmian, zachowaj uzasadnione odpowiedzi w checkpointie.
6. Po `APPROVED`, pozytywnej walidacji i spełnieniu kryteriów oznacz objęte oceną ukończone milestone'y jako `done`. Zapisz końcowy checkpoint z zakresem ostatniego review i pozostaw wszystkie zmiany niecommitowane. Aktualizacja końcowych statusów nie jest dodatkową rundą poprawek. Nierozwiązane drobne uwagi zgłoś jako nieblokujące; problemy ważne, krytyczne lub brak weryfikacji uniemożliwiają ogłoszenie sukcesu.

## Checkpoint i wznowienie

W `STATUS.md` zachowuj zwięźle: fazę (`implementation`, `review`, `fixes`, `complete` lub `blocked`), `review_base`, listę milestone'ów i ich wyników, zakres zmienionych i nowych plików oraz początkowe zmiany użytkownika, liczbę rund, ostatni raport review lub odnośnik do jego zapisu, walidacje, odłożone decyzje i następny krok. Nie dodawaj nowych statusów do schematu ROADMAP: `implemented_pending_review` jest wynikiem checkpointu.

Checkpoint w worktree jest trwałym źródłem wyników wszystkich milestone'ów. Zachowaj zbiorczy stan, raporty i odłożone decyzje aż do osobnej publikacji; nie polegaj na historii commitów z tego przebiegu, ponieważ workflow ich nie tworzy.

Przy wznowieniu porównaj checkpoint z aktualną zawartością zmienionych i nowych plików. Nie powtarzaj zaimplementowanego milestone'u i nie pomijaj oczekującego review. Nie uznawaj wcześniejszego `APPROVED` za aktualne, jeśli oceniany zakres zmienił się od czasu review. Nieoczekiwane zmiany HEAD lub nakładające się zmiany użytkownika wymagają wyjaśnienia przed kontynuacją; nie przesuwaj po cichu bazy. Brak checkpointu po awarii wymaga porównania Git i kodu, nie zgadywania wyniku.

## Zatrzymanie i wynik

Zatrzymaj zależną pracę przy zmianie zakresu wymagającej decyzji, problemie wykraczającym poza zakres, niemożności oddzielenia cudzych zmian lub nieoczekiwanej modyfikacji repo. Zapisz blokadę. Nierozwiązane problemy po trzech rundach zatrzymują finalizację.

Przed ogłoszeniem ukończenia sprawdź, czy nie pozostał żaden otwarty milestone z uzgodnionego zakresu. Nie kończ po pierwszym milestone'ie, nie pomijaj po cichu `blocked` i nie uruchamiaj wszystkich dostępnych skilli bez związku z zadaniem.

Zwróć handoff do `$codex-flow-publish`: zakres i baza, wyniki milestone'ów, zmienione i nowe pliki, końcowa decyzja review całości, liczba rund, walidacje, blokery i fakty do synchronizacji dokumentacji. Ostrzeżenia rozmiaru zgłoś jako osobny krok kompakcji. Commit i push należą do osobnej publikacji, poza tym workflow.
