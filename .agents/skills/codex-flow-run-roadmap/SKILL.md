---
name: codex-flow-run-roadmap
description: Wykonaj wszystkie otwarte milestone'y z ROADMAP.md i zweryfikuj integrację całego wyniku. Nie wykonuj stagingu, commitów ani pusha i nie wywołuj żadnych subagentów.
---

# Wykonanie roadmapy

Wspólne zasady definiuje [kontrakt flow](../codex-flow-run-roadmap/references/flow-contract.md). Cały ten workflow i jego skille podrzędne wykonuj w jednym wątku, bez subagentów, stagingu, commitów i pusha.

## Przygotowanie

1. Przeczytaj STATUS, aktywną roadmapę i istotne wymagania. Sprawdź Git i rozmiar kontekstu; nie czytaj archiwum domyślnie.
2. Dla nowego przebiegu lub jawnego rozszerzenia ukończonej, niecommitowanej pracy zbierz rzeczywiste otwarte milestone'y `planned`, `in_progress`, `blocked`; pomiń szablony i `done`. Sprawdź aktualność blokad i kolejność zależności. Przy zwykłym wznowieniu użyj listy z checkpointu; później dopisane milestone’y nie wchodzą do niej automatycznie. Rozszerzenie na jawne zlecenie zachowuje bazę, wcześniejsze wyniki i licznik według kontraktu. Nie rozszerzaj uzgodnionego zakresu.
3. Rozpoznaj nowy przebieg, wznowienie albo zakończony wynik oczekujący na publikację zgodnie z kontraktem. Zapisz checkpoint przed edycją; rozdziel początkowe zmiany użytkownika. Nie resetuj bazy ani licznika aktywnego przebiegu.
4. Pokaż kolejność i kontynuuj bez dodatkowego potwierdzenia, jeśli zakres jest jasny.

## Implementacja

1. Dla każdego wykonalnego milestone'u potwierdź zakres, kryteria i walidację. Zapisz `in_progress` i checkpoint rozpoczęcia.
2. Użyj `$codex-flow-implement-milestone` i sprawdź wynik kontroli. Brak wykonanych kontroli nie jest pozytywną walidacją.
3. Po udanej implementacji i walidacji zapisz wynik walidacji; w roadmapie pozostaw `in_progress`. Przechowuj zbiorcze wyniki wszystkich milestone'ów.
4. Przejdź do kolejnego milestone'u bez pytania o kontynuację.
5. Przy blokadzie zapisz przyczynę i realizuj inne niezależne elementy. Nie realizuj zależnych. Jeśli pozostały blokady i nie ma wykonalnej pracy, zatrzymaj przebieg; nie ogłaszaj ukończenia.

## Walidacja i zakończenie

1. Po całej implementacji uruchom pełną dostępną walidację integracji. Napraw błędy mieszczące się w zakresie i ponów odpowiednie kontrole; przy nierozwiązywalnej blokadzie zapisz `blocked` i zatrzymaj pracę.
2. Po udanej walidacji i spełnieniu kryteriów oznacz milestone'y jako `done` i zapisz fazę `complete`, pozostawiając wynik niecommitowany. Jawnie zlecone review pozostaje warunkiem zakończenia zgodnie z kontraktem; nie uruchamiaj go automatycznie.

## Dokumentacja i zatrzymanie

Aktualizuj checkpoint i statusy na bieżąco. Redakcję specyfikacji i README można odłożyć do publish, zapisując istotne decyzje w checkpointie. Dokumenty wymagane kryteriami akceptacji powstają podczas implementacji i podlegają walidacji.

Przy wznowieniu stosuj kontrakt: zachowuj bazę, licznik i wyniki, weryfikuj zawartość, nie powtarzaj ukończonej implementacji. Zatrzymaj zależną pracę przy nieuzgodnionej zmianie zakresu, nieoddzielonych cudzych zmianach lub nieoczekiwanym stanie repo. Brak checkpointu wymaga odtworzenia faktów, nie zgadywania oceny.

Przed ogłoszeniem ukończenia sprawdź wszystkie milestone'y uzgodnionego zakresu. Zwróć krótki handoff: wyniki, walidację, blokery i odłożone decyzje. Dane do wznowienia i publikacji muszą pozostać w STATUS. Ostrzeżenia rozmiaru zgłoś jako osobny krok kompakcji. Publikacja wymaga osobnego polecenia.
