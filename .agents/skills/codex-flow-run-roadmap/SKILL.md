---
name: codex-flow-run-roadmap
description: Wykonaj wszystkie otwarte milestone'y z ROADMAP.md, następnie review całości w tym samym wątku i maksymalnie trzy rundy poprawek z ponownym review. Nie wykonuj stagingu, commitów ani pusha i nie wywołuj żadnych subagentów.
---

# Wykonanie roadmapy

Wspólne zasady definiuje [kontrakt flow](../codex-flow-run-roadmap/references/flow-contract.md). Cały ten workflow i jego skille podrzędne wykonuj w jednym wątku, bez subagentów, stagingu, commitów i pusha. Review jest samooceną. Jeśli STATUS sam jest ocenianym artefaktem, wyjątek z kontraktu zastępuje poniższe zapisy końcowego checkpointu: przygotuj pliki przed końcową oceną i zwróć końcowy dowód wyłącznie w rozmowie.

## Przygotowanie

1. Przeczytaj STATUS, aktywną roadmapę i istotne wymagania. Sprawdź Git i rozmiar kontekstu; nie czytaj archiwum domyślnie.
2. Dla nowego przebiegu lub jawnego rozszerzenia ukończonej, niecommitowanej pracy zbierz rzeczywiste otwarte milestone'y `planned`, `in_progress`, `blocked`; pomiń szablony i `done`. Sprawdź aktualność blokad i kolejność zależności. Przy zwykłym wznowieniu użyj listy z checkpointu; później dopisane milestone’y nie wchodzą do niej automatycznie. Rozszerzenie na jawne zlecenie zachowuje bazę, wcześniejsze wyniki i licznik według kontraktu. Nie rozszerzaj uzgodnionego zakresu.
3. Rozpoznaj nowy przebieg, wznowienie albo zakończony wynik oczekujący na publikację zgodnie z kontraktem. Zapisz checkpoint przed edycją; rozdziel początkowe zmiany użytkownika. Nie resetuj bazy ani licznika aktywnego przebiegu.
4. Pokaż kolejność i kontynuuj bez dodatkowego potwierdzenia, jeśli zakres jest jasny.

## Implementacja

1. Dla każdego wykonalnego milestone'u potwierdź zakres, kryteria i walidację. Zapisz `in_progress` i checkpoint rozpoczęcia.
2. Użyj `$codex-flow-implement-milestone` i sprawdź wynik kontroli. Brak wykonanych kontroli nie jest pozytywną walidacją.
3. Po udanej implementacji i walidacji zapisz `implemented_pending_review`; w roadmapie pozostaw `in_progress`. Przechowuj zbiorcze wyniki wszystkich milestone'ów.
4. Przejdź do kolejnego milestone'u bez review pośredniego i bez pytania o kontynuację.
5. Przy blokadzie zapisz przyczynę i realizuj inne niezależne elementy. Nie realizuj zależnych. Jeśli pozostały blokady i nie ma wykonalnej pracy, zatrzymaj przebieg przed review całości; nie ogłaszaj ukończenia.

## Review całości i poprawki

1. Po całej implementacji uruchom pełną dostępną walidację integracji. Napraw błędy mieszczące się w zakresie; przy nierozwiązywalnej blokadzie zatrzymaj pracę. Po udanej walidacji zapisz fazę `review`.
2. Wykonaj samoocenę pełnego zakresu od stałej bazy według sekcji kontraktu: [review i zakończenie pracy](references/flow-contract.md#review-i-zakończenie-pracy), [własność zmian i zakres review](references/flow-contract.md#własność-zmian-i-zakres-review) oraz [aktualność oceny](references/flow-contract.md#aktualność-oceny), z kontrolą fingerprintu. Zapisz decyzję, zwięzły raport i ocenione ścieżki w checkpointie.
3. Przy zasadnych uwagach użyj `$codex-flow-address-review`, przekazując pełny ostatni raport i zakres całego przebiegu. Przed rozpoczęciem rundy zwiększ licznik i zapisz fazę `fixes`; po przerwaniu dokończ tę samą rundę. Odpowiedz na wszystkie uwagi, zweryfikuj poprawki i ponów review całości od tej samej bazy.
4. Limit: pierwsze review → poprawki 1 → review → poprawki 2 → review → poprawki 3 → ostatnie review. Wznowienie nie zeruje licznika. Gdy nie potrzeba zmian, zachowaj uzasadnienia odrzuceń i przekaż je do ponownej oceny. Nie uruchamiaj czwartej rundy. Jeśli ostatnie review nadal blokuje ukończenie, zapisz `blocked`, licznik i pozostałe uwagi, a następnie zatrzymaj finalizację.
5. Po aktualnym `APPROVED`, udanej walidacji i spełnieniu kryteriów oznacz objęte oceną milestone'y jako `done`. Skontroluj zmianę samych statusów i odśwież fingerprint zgodnie z kontraktem. Zapisz fazę `complete`, pozostawiając wynik niecommitowany. Drobne uwagi nie blokują; ważne, krytyczne i brak wymaganej weryfikacji blokują ukończenie.

## Dokumentacja i zatrzymanie

Aktualizuj checkpoint i statusy na bieżąco. Redakcję specyfikacji i README można odłożyć do publish, zapisując istotne decyzje w checkpointie. Dokumenty wymagane kryteriami akceptacji powstają podczas implementacji i podlegają review.

Przy wznowieniu stosuj kontrakt: zachowuj bazę, licznik i wyniki, weryfikuj zawartość, nie powtarzaj implementacji oczekującej na review. Zatrzymaj zależną pracę przy nieuzgodnionej zmianie zakresu, nieoddzielonych cudzych zmianach lub nieoczekiwanym stanie repo. Brak checkpointu wymaga odtworzenia faktów, nie zgadywania oceny.

Przed ogłoszeniem ukończenia sprawdź wszystkie milestone'y uzgodnionego zakresu. Zwróć krótki handoff: wyniki, review, rundy, walidację, blokery i odłożone decyzje. Dane do wznowienia i publikacji muszą pozostać w STATUS. Ostrzeżenia rozmiaru zgłoś jako osobny krok kompakcji. Publikacja wymaga osobnego polecenia.
