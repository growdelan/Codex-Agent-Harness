---
name: codex-flow-run-roadmap
description: Wykonaj wszystkie otwarte milestone'y z ROADMAP.md, tworząc jeden commit po implementacji i walidacji całej roadmapy. Następnie wykonaj review całego zakresu w tym samym wątku i maksymalnie trzy rundy poprawek z commitami. Nie wywołuj subagenta reviewera. Jawne uruchomienie autoryzuje lokalne commity, bez pusha.
---

# Wykonanie roadmapy

## Przygotowanie i zakres

1. Przeczytaj potrzebny kontekst projektu, `STATUS.md`, aktywną roadmapę i istotne wymagania ze specyfikacji. Sprawdź Git i rozmiar kontekstu; nie czytaj archiwum domyślnie.
2. Zbierz wszystkie rzeczywiste otwarte milestone'y: `planned`, `in_progress` oraz `blocked`. Pomiń szablony i zakończone `done`. Dla `blocked` sprawdź, czy blokada nadal istnieje; rozwiązane blokady pozwalają wznowić pracę. Ustal kolejność zależności i nie dodawaj nowych funkcji poza uzgodnioną roadmapą.
3. Porównaj checkpoint z Git. Zapisz stały bazowy commit całego przebiegu (`review_base`), listę milestone'ów oraz początkowe zmiany użytkownika. Nie przesuwaj tej bazy po milestone'ach ani poprawkach. Przy wznowieniu użyj zapisanej bazy i fazy, zamiast rozpoczynać nowy przebieg.
4. Pokaż kolejność. Jawne zlecenie wykonania roadmapy obejmuje jeden lokalny commit po zaimplementowaniu i zwalidowaniu wszystkich milestone'ów oraz każdej rundzie poprawek. Nie pytaj ponownie. Jeśli użytkownik wykluczył commity, zachowaj ten tryb i dokładny zakres zmian w checkpointach.

## Odpowiedzialność i dokumentacja

Główny agent prowadzi implementację i cały cykl review → poprawki w tej samej rozmowie. `run-roadmap` nigdy nie wywołuje custom agenta `reviewer`, także przez inny skill. Nie zastępuj go innym subagentem do review. Custom reviewer jest dostępny tylko na osobne, jawne polecenie użytkownika, poza tą pętlą. Review we własnym wątku jest samooceną, nie niezależnym review.

Opcjonalny `implementer` może wykonać zamknięty fragment implementacji przy konkretnej korzyści z delegowania. Przekaż zakres i własność plików; główny agent odbiera wynik i odpowiada za wspólny checkpoint.

Aktualizuj checkpoint i statusy na bieżąco. Pełną redakcję specyfikacji i README można odłożyć do `$codex-flow-publish`, zachowując decyzje do przekazania dalej. Dokumenty będące kryteriami akceptacji są częścią implementacji i review. Sam brak odroczonej redakcyjnej synchronizacji nie blokuje oceny.

## Faza 1: wszystkie milestone'y

1. Dla każdego wykonalnego milestone'u potwierdź zakres, kryteria i walidację. Zapisz `in_progress` w roadmapie i checkpoint rozpoczęcia.
2. Użyj `$codex-flow-implement-milestone`, uruchom adekwatne kontrole i sprawdź wynik. Brak wykonanych kontroli nie jest pozytywną walidacją.
3. Po implementacji i pozytywnej walidacji zapisz w checkpointie wynik `implemented_pending_review`. Nie wykonuj jeszcze commita. W roadmapie pozostaw `in_progress` do końcowego review. Zachowaj zbiorczy checkpoint wszystkich wyników w worktree.
4. Przejdź do kolejnego milestone'u bez review pośredniego i bez pytania o kontynuację. Checkpoint pozwala odróżnić zaimplementowane elementy oczekujące na review od jeszcze nierozpoczętych.
5. Jeśli milestone jest zablokowany, zapisz przyczynę i kontynuuj inne niezależne, wykonalne elementy. Nie realizuj jego zależnych milestone'ów. Gdy nie ma dalszej wykonalnej pracy, a pozostały blokady, zapisz częściowy wynik i zatrzymaj workflow przed zbiorczym commitem oraz review. Nie ogłaszaj ukończenia roadmapy.

## Faza 2: review całości i poprawki

1. Po implementacji wszystkich milestone'ów z uzgodnionego zakresu uruchom pełną dostępną walidację integracji. Napraw błędy mieszczące się w zakresie; przy nierozwiązywalnej blokadzie zatrzymaj pracę. Po pozytywnej walidacji zapisz checkpoint fazy `review`, sprawdź pełny diff i wykonaj jeden zbiorczy commit implementacji wraz z checkpointem. Dopiero wtedy przejdź do review. Nie włączaj cudzych zmian i nie twórz pustego commita.
2. Użyj `$codex-flow-review` w tym samym wątku. Oceniaj cały zakres od `review_base` do aktualnego HEAD, włącznie z integracją milestone'ów; nie ograniczaj się do ostatniego commita ani pustego worktree. W trybie bez commitów uwzględnij też staged, unstaged i nowe pliki należące do zadania. Wyłącz wcześniejsze zmiany użytkownika.
3. Wymagaj `DECISION: APPROVED` albo `DECISION: CHANGES_REQUIRED`. Zapisz raport, oceniony HEAD/zakres i wynik w checkpointie. Review rozpoczynaj dopiero po zakończeniu całej uzgodnionej implementacji.
4. Jeśli istnieją zasadne poprawki z review, użyj `$codex-flow-address-review` w tym samym wątku, przekazując pełny raport i zakres całego przebiegu. Napraw zasadne problemy, odpowiedz na każde znalezisko i ponów adekwatną walidację. Po pozytywnej walidacji zapisz wynik oraz osobny commit rundy poprawek, następnie ponownie użyj `$codex-flow-review` dla całego zakresu od tej samej bazy.
5. Limit wynosi trzy rundy poprawek łącznie dla całego przebiegu: pierwsze review → poprawki 1 → review → poprawki 2 → review → poprawki 3 → ostatnie review. Wznowienie nie zeruje licznika. Po trzeciej rundzie nie uruchamiaj czwartej. Nie twórz pustego commita, jeśli weryfikacja uwag nie wymaga zmian; zachowaj odpowiedzi w checkpointie.
6. Po `APPROVED`, pozytywnej walidacji i spełnieniu kryteriów oznacz objęte oceną ukończone milestone'y jako `done`. Zapisz końcowy checkpoint z identyfikatorem ostatniego ocenionego commita i utrwal zmienione statusy osobnym lokalnym commitem finalizacyjnym, jeśli są zmiany. To nie jest dodatkowa runda poprawek. Nierozwiązane drobne uwagi zgłoś jako nieblokujące; problemy ważne, krytyczne lub brak weryfikacji uniemożliwiają ogłoszenie sukcesu.

## Checkpoint i wznowienie

W `STATUS.md` zachowuj zwięźle: fazę (`implementation`, `review`, `fixes`, `complete` lub `blocked`), `review_base`, listę milestone'ów i ich wyników, tryb commitowania, zbiorczy commit implementacji i commity poprawek, liczbę rund, ostatni raport review lub odnośnik do jego zapisu, walidacje, odłożone decyzje i następny krok. Nie dodawaj nowych statusów do schematu ROADMAP: `implemented_pending_review` jest wynikiem checkpointu.

Checkpoint zapisany we własnym commicie identyfikuje wynik jako „commit zawierający ten checkpoint”; jego SHA ustal z Git przy wznowieniu. Po błędzie commita porównaj worktree z checkpointem i dokończ zapis przed dalszą fazą. Nie powtarzaj zaimplementowanego milestone'u i nie pomijaj oczekującego review. Brak checkpointu po awarii wymaga porównania Git i kodu, nie zgadywania wyniku.

Przed zbiorczym commitem checkpoint w worktree jest trwałym źródłem wyników wszystkich milestone'ów; nie usuwaj wcześniejszych wpisów. Po commitach historię checkpointów można odczytać z Git. Nie usuwaj odłożonych decyzji i raportów potrzebnych dalszej pracy. W trybie bez commitów zachowaj zwięzły zbiorczy stan aż do finalizacji.

## Zatrzymanie i wynik

Zatrzymaj zależną pracę przy zmianie zakresu wymagającej decyzji, problemie wykraczającym poza zakres, niemożności oddzielenia cudzych zmian lub nieoczekiwanej modyfikacji repo. Zapisz blokadę. Nierozwiązane problemy po trzech rundach zatrzymują finalizację.

Przed ogłoszeniem ukończenia sprawdź, czy nie pozostał żaden otwarty milestone z uzgodnionego zakresu. Nie kończ po pierwszym milestone'ie, nie pomijaj po cichu `blocked` i nie uruchamiaj wszystkich dostępnych skilli bez związku z zadaniem.

Zwróć handoff do `$codex-flow-publish`: zakres i baza, wyniki milestone'ów, commity, końcowa decyzja review całości, liczba rund, walidacje, blokery i fakty do synchronizacji dokumentacji. Ostrzeżenia rozmiaru zgłoś jako osobny krok kompakcji. Nie wykonuj pusha bez osobnego jawnego polecenia.
