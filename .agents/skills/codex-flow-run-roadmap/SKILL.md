---
name: codex-flow-run-roadmap
description: Wykonaj wykonalne milestone'y z ROADMAP.md w głównej rozmowie, z niezależnym reviewerem i trwałym checkpointem. Jawne uruchomienie tego workflow autoryzuje lokalny commit po każdym zatwierdzonym milestone'ie, bez pusha. Użyj na prośbę o realizację całej roadmapy lub autonomiczną pracę do ukończenia planu albo blokera.
---

# Wykonanie roadmapy

## Przygotowanie

1. Przeczytaj `AGENTS.md`, `STATUS.md`, aktywne milestone'y z `ROADMAP.md` i potrzebne fragmenty `spec.md`. Sprawdź rozmiar kontekstu i stan Git. Nie czytaj archiwum domyślnie.
2. Porównaj checkpoint w `STATUS.md` ze stanem repo i historią Git. Wznów uzgodniony milestone `in_progress`, następnie zbierz rzeczywiste milestone'y `planned` w kolejności zależności. Jeśli checkpoint wskazuje `approved`, ale commit nie powstał, najpierw potwierdź zgodność worktree z ocenionym zakresem i dokończ zapis/commit w autoryzowanym trybie. Nie wykonuj ponownie zatwierdzonej pracy tylko dlatego, że roadmapa nie została jeszcze zsynchronizowana. Pomijaj wpisy szablonowe; blokadę zależności zgłoś, nie obchodź jej.
3. Pokaż kolejność i przypomnij, że ten workflow obejmuje lokalne commity. Jawne zlecenie wykonania roadmapy jest zgodą na te commity; nie pytaj ponownie. Jeśli użytkownik wykluczył commity, wykonuj pracę bez nich i zapisuj ten tryb w checkpointach.
4. Ustal bazowy commit i istniejące zmiany użytkownika. Nie nadpisuj ich ani nie włączaj ich do commitów.

## Podział odpowiedzialności

Główny agent implementuje, waliduje, rozpatruje uwagi i utrzymuje checkpoint. Nie deleguj implementacji wyłącznie po to, żeby główny agent czekał na raport. Opcjonalny `implementer` służy do zamkniętego zadania, gdy delegowanie daje konkretną korzyść, np. niezależnej pracy równoległej albo izolacji dużej ilości szczegółów. Przekaż mu zakres i własność plików; pamiętaj, że agenci współdzielą repo.

Review wykonuje osobny custom agent `reviewer`. Dla każdego milestone'u utwórz nowego reviewera z wymaganiami, bazą porównania, pełnym diffem milestone'u i wynikami walidacji. Zachowaj tego samego reviewera do sprawdzenia poprawek tego milestone'u. Nie uruchamiaj review równolegle ze zmianami ocenianych plików. Gdy reviewer jest niedostępny, zapisz blokadę zamiast zastępować niezależne review samooceną.

Pełną aktualizację `spec.md` i README można odłożyć do finalizacji przez `$codex-flow-publish`. Zapisuj jednak na bieżąco w checkpointach nowe decyzje i fakty do uwzględnienia w dokumentacji oraz przekazuj je kolejnemu milestone'owi. Brak redakcyjnej aktualizacji dokumentacji nie blokuje review. Brak instrukcji, kontraktu lub innego artefaktu będącego kryterium akceptacji milestone'u jest częścią jego zakresu i podlega review.

## Pętla milestone'ów

1. Potwierdź cel, zakres, kryteria akceptacji, walidację i zależności. Zapisz checkpoint rozpoczęcia w `STATUS.md` oraz status `in_progress` w `ROADMAP.md`.
2. Wykonaj `$codex-flow-implement-milestone` w głównej rozmowie. Dla oddelegowanego fragmentu odbierz i zweryfikuj wynik. Uruchom adekwatne kontrole produktu; pominięcie kontroli nie oznacza pozytywnej walidacji.
3. Przekaż reviewerowi cały diff milestone'u, wymagania i wyniki kontroli. Wymagaj decyzji `DECISION: APPROVED` albo `DECISION: CHANGES_REQUIRED`.
4. Przy `CHANGES_REQUIRED` zweryfikuj każde znalezisko i użyj `$codex-flow-address-review` do zasadnych poprawek. Przekaż temu samemu reviewerowi pełny aktualny diff, wcześniejsze znaleziska, odpowiedzi i nową walidację. Maksymalnie trzy rundy poprawek; po ich wyczerpaniu zapisz blokadę i zatrzymaj pętlę.
5. Po `APPROVED` i spełnieniu kryteriów zapisz wynik review, walidacje i status `done`. Sprawdź końcowy diff, stage'uj tylko uzgodniony zakres i wykonaj lokalny commit milestone'u, jeśli autoryzowany. Uwzględnij jego checkpoint i zmianę roadmapy w commicie. Jeśli nie da się oddzielić zmian użytkownika, zatrzymaj się przed stagingiem.
6. Sprawdź wynik commita i stan repo. Przejdź do następnego milestone'u bez ponownego pytania. Po ostatnim milestone'ie uruchom pełną dostępną walidację integracji; jej niepowodzenie zapisz jako blokadę finalizacji, nawet jeśli wcześniejsze review były pozytywne.

## Trwały checkpoint

Aktualizuj `STATUS.md` przy rozpoczęciu milestone'u, po review, przy jego zakończeniu i przed planowanym zatrzymaniem. Zachowuj krótki stan, bez pełnych logów:

- bieżący milestone i tryb commitowania;
- commit bazowy milestone'u oraz opis wcześniejszych zmian użytkownika;
- wynik `in_progress`, `approved`, `blocked` lub `not_started`, decyzja review i liczba rund poprawek;
- komendy walidacji, wyniki i pominięcia z przyczyną;
- nierozwiązane problemy i trwałe decyzje oczekujące na synchronizację dokumentacji;
- następny krok i sposób odnalezienia commita.

Checkpoint zapisany w commicie milestone'u wskazuje **commit zawierający ten checkpoint** jako commit wyniku; nie próbuj wpisywać jego własnego SHA przed utworzeniem commita. Przy wznowieniu ustal ten SHA z historii Git i potwierdź zakres. Bez commita zapisz jawnie, że wynik pozostaje w worktree, wraz z zakresem plików. Sam brak checkpointu po awarii nie jest dowodem braku wykonanej pracy: porównaj także Git i kod.

Nie nadpisuj odłożonych decyzji i wyników wcześniejszych milestone'ów, dopóki nie zostały odzwierciedlone w dokumentacji lub utrwalone w commitach możliwych do odnalezienia. `STATUS.md` pozostaje krótkim indeksem, a historia checkpointów pozostaje w Git. W trybie bez commitów zachowaj zwięzłe wyniki każdego zakończonego milestone'u aż do finalizacji.

## Zatrzymanie i zakończenie

Zatrzymaj pracę przy zmianie zakresu wymagającej decyzji, blokadzie zależności, nieskutecznej walidacji wykraczającej poza zakres, wyczerpaniu rund review lub nieoczekiwanych zmianach. Zapisz konkretną blokadę w `STATUS.md` i właściwy status w `ROADMAP.md`. Zmianę polecenia użytkownika uwzględnij zgodnie z jej treścią.

Na końcu podaj zwięzły handoff do `$codex-flow-publish`: wykonane i pozostałe milestone'y, odnośniki do commitów/checkpointów, decyzje review, walidacje, blokery i fakty do synchronizacji dokumentacji. Nie polegaj wyłącznie na historii rozmowy. Ostrzeżenia rozmiaru zgłoś jako osobny krok kompakcji. Nigdy nie wykonuj pusha bez osobnego jawnego polecenia.
