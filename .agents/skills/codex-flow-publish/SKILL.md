---
name: codex-flow-publish
description: Przygotuj zakończoną zmianę do publikacji, aktualizując dokumentację, weryfikując diff i walidację oraz wykonując commit lub push wyłącznie wtedy, gdy użytkownik jawnie o to poprosił. Użyj dla poleceń typu przygotuj zmianę, zrób commit, push albo opublikuj.
---

# Publikacja zmiany

1. Ustal dokładny poziom autoryzacji z polecenia użytkownika: przygotowanie, commit albo push. Nie rozszerzaj go.
2. Sprawdź `git status --short`, pełny diff oraz obecność zmian użytkownika spoza zakresu.
3. Jeśli zmiana pochodzi z `$codex-flow-run-roadmap`, odczytaj trwały checkpoint w `STATUS.md`, roadmapę i cały zakres zmian worktree, w tym nowe pliki; handoff rozmowy jest pomocniczy. Potwierdź wyniki milestone'ów i aktualny zakres plików oraz końcowe review całego zakresu od `review_base`, łączną liczbę rund poprawek, walidacje i blokery. Nie wymagaj commitów implementacji ani poprawek: `run-roadmap` ich nie tworzy. Potwierdź, że aktualne zmiany odpowiadają ostatniemu review; późniejsze zmiany zachowania wymagają ponownej oceny. Nie uznawaj częściowego wykonania za ukończenie całej roadmapy. Nie zgaduj brakujących wyników.
4. Upewnij się, że nie ma nierozwiązanych problemów blokujących i że adekwatna walidacja przeszła. W razie potrzeby uruchom `./scripts/verify.sh`.
5. Jednorazowo zaktualizuj `ROADMAP.md` i `STATUS.md` zgodnie z checkpointami i stanem faktycznym. Zmień `spec.md` lub `README.md` tylko wtedy, gdy zmieniły się decyzje, zachowanie, uruchamianie albo konfiguracja.
6. Sprawdź spójność zaktualizowanych `ROADMAP.md`, `STATUS.md`, `spec.md` i `README.md` z diffem implementacyjnym, wynikami review i walidacją.
7. Uruchom `./scripts/check-context-size.sh`. Jeśli występują ostrzeżenia, zgłoś `$codex-flow-compact-context` jako osobny rekomendowany krok; nie rozszerzaj publikowanego diffu o kompakcję, chyba że użytkownik jawnie objął ją zakresem zmiany.
8. Jeśli użytkownik poprosił tylko o przygotowanie, zatrzymaj się przed stagingiem i commitem.
9. Jeśli użytkownik poprosił o commit, stage'uj wyłącznie pliki z uzgodnionego zakresu i utwórz logiczny commit.
10. Wykonaj push tylko na jawne polecenie `push`, `opublikuj` lub równoważne i tylko do właściwego remote/brancha. Jeśli użytkownik chce użyć `github:yeet`, zakończ synchronizację i walidację przed przekazaniem mu stagingu, commita, pusha i utworzenia draft PR.

Nie twórz pustych commitów, nie ukrywaj nieprzechodzącej walidacji i nie włączaj cudzych zmian do publikacji. Podaj zaktualizowane dokumenty, walidacje oraz faktyczny status commita i pusha.
