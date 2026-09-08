---
name: codex-flow-plan-from-prd
description: Utwórz lub zaktualizuj spec.md i ROADMAP.md na podstawie pierwszego albo przyrostowego PRD z katalogu prd, bez implementowania kodu. Użyj, gdy użytkownik wskazuje PRD i chce otrzymać spójną specyfikację, mierzalne milestone'y, ryzyka i walidacje.
---

# Planowanie z PRD

Znaczenie specyfikacji, mapowanie PRD i granice aktywnego przebiegu określa [kontrakt flow](../codex-flow-run-roadmap/references/flow-contract.md).

1. Ustal wskazany plik PRD. Jeśli użytkownik go nie podał, wybierz go tylko wtedy, gdy w `prd/` istnieje jeden oczywisty kandydat.
2. Uruchom `./scripts/check-context-size.sh`. Przeczytaj PRD, `STATUS.md`, aktywne milestone'y w `ROADMAP.md` oraz indeks i istotne części `spec.md`. Nie czytaj archiwum ani niepowiązanych dokumentów domenowych.
3. Przed rozszerzeniem dokumentacji wykonaj krótką kontrolę higieny kontekstu. Jeśli `STATUS.md` zawiera zamkniętą historię albo `ROADMAP.md` zachowuje pełne szczegóły milestone'ów `done`, które nie są już potrzebne aktywnym zależnościom, uporządkuj je zgodnie z `$codex-flow-compact-context`. Zrób to niezależnie od ostrzeżenia o rozmiarze; przekroczenie progu zawsze wymaga uporządkowania przed dalszym rozbudowywaniem pliku. Nie usuwaj aktualnej prawdy tylko po to, by zmieścić się w limicie.
4. Rozpoznaj, czy PRD inicjuje projekt, czy rozszerza istniejący zakres. Sprawdź indeks PRD w ROADMAP: już zaplanowany zakres aktualizuj zamiast tworzyć duplikaty. Nie zmieniaj zamrożonego zakresu aktywnego przebiegu bez uzgodnienia; nowe niezależne wymagania mogą czekać w planie kolejnego przebiegu.
5. Zaktualizuj `spec.md`: cel, zachowanie, architekturę i tylko uzasadnione decyzje techniczne. Powiąż planowane zmiany ze źródłowym PRD i milestone’em; nie przedstawiaj ich jako wdrożonych. Decyzje zastąpione oznacz odnośnikiem do następcy, zachowując uzasadnienie.
6. Zaktualizuj `ROADMAP.md`. Każdy milestone musi mieć status, cel, mierzalne kryteria akceptacji, zakres, poza zakresem, walidację oraz ryzyka lub zależności.
7. Jeśli PRD inicjuje nowy projekt i roadmapa nie zawiera jeszcze Milestone 0, utwórz go jako najmniejszy uruchamialny „hello world” właściwy dla docelowego rodzaju projektu. Ma potwierdzać działanie środowiska, głównego entrypointu, podstawowej struktury projektu i repozytoryjnej komendy walidacyjnej. Zapisz w zakresie i kryteriach Milestone 0 obowiązek skonfigurowania rzeczywistej kontroli produktu w `scripts/verify.sh` podczas implementacji; brak testów lub brak skonfigurowanych kontroli nie może być dowodem ukończenia Milestone 0. Dostosuj rezultat do interfejsu projektu, na przykład proste wyjście CLI, pojedynczy endpoint API, renderującą się stronę albo import i wywołanie biblioteki. Nie umieszczaj w Milestone 0 funkcjonalności biznesowej, prawdziwych usług zewnętrznych, sekretów ani fundamentów niewymaganych do jego uruchomienia.
8. Nie traktuj milestone'ów jak epików ani kategorii prac. Każdy milestone ma dostarczać jeden mały, spójny rezultat, który można zaimplementować, zweryfikować i zreviewować jako niezależną zmianę. Jeśli zakres łączy kilka niezależnych rezultatów, rozdzielnych funkcji lub osobno weryfikowalnych zmian, rozbij go na mniejsze milestone'y i zapisz ich zależności. Nie rozbijaj go na mechaniczne kroki, które samodzielnie nie dają weryfikowalnego rezultatu.
9. Po utworzeniu roadmapy skontroluj granulację każdego milestone'u: jego ukończenie musi dać się jednoznacznie potwierdzić wskazaną walidacją, a kryteria akceptacji nie mogą ukrywać kilku niezależnych celów. Nie stosuj sztywnego limitu czasu, liczby plików ani liczby testów jako miary wielkości.
10. Nie zgaduj brakujących wymagań. Zapisz konkretne `TODO: [pytanie]` albo poproś użytkownika o decyzję, jeśli wpływa ona na plan.
11. Zaktualizuj indeks PRD → milestone’y w ROADMAP: `planned` oznacza pełne uwzględnienie w planie, `partial` wskazuje nierozstrzygnięty zakres. Nie oznaczaj wdrożenia na podstawie samego planu.
12. Nie zmieniaj kodu aplikacji, testów, zależności ani skryptów walidacyjnych. Aktualizuj tylko dokumentację planistyczną; STATUS tylko w zakresie kompakcji lub krótkiego następnego kroku, bez resetowania aktywnego checkpointu.

Podsumuj użyty PRD, zmienione dokumenty, milestone'y, ryzyka, TODO i rekomendowany następny krok.
