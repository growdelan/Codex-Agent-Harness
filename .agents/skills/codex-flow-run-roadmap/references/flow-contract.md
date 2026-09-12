# Kontrakt Codex Flow

Ten dokument definiuje wspólne reguły workflow. AGENTS.md zawiera stałe zasady projektu, skille — kroki konkretnego zadania, README — instrukcję użycia. Rozbieżności między plikami harnessu zgłaszaj; poprawiaj je tylko w zadaniu dopuszczającym edycję tego zakresu. W resume i review zachowaj read-only; jawne polecenie użytkownika określa zakres pracy i ma pierwszeństwo.

## Review i zakończenie pracy

- `run-roadmap` wykonuje samoocenę całego wyniku po implementacji wszystkich milestone'ów. Wszystkie jego etapy, również skille podrzędne, wykonuje główny agent w jednym wątku, bez subagentów, stagingu, commitów i pusha.
- Niezależne review oznacza ocenę przez osobnego agenta, który nie implementował zmiany. Jest dostępne poza `run-roadmap` wyłącznie na jawne zlecenie użytkownika. Samooceny nie nazywaj niezależnym review.
- Samodzielny milestone wymaga adekwatnej walidacji; większa lub ryzykowna zmiana także samooceny. Dla małej zmiany bez takiego ryzyka review jest opcjonalne. Jawnie zamówione review jest częścią kryteriów zakończenia zadania.
- `publish` sam nie uruchamia review. Brak review nie blokuje zadania, które go nie wymagało. Nie omija jednak wymaganego lub zamówionego review, znanych blokerów ani nieaktualnego zatwierdzenia.
- Etap review jest read-only i zwraca decyzję. Statusy zapisuje agent prowadzący zadanie po otrzymaniu wyniku, również gdy reviewer był niezależny.

## Statusy i cykl życia przebiegu

ROADMAP używa wyłącznie `planned`, `in_progress`, `blocked`, `done`. Przed implementacją prowadzący zapisuje `in_progress`, przy blokadzie `blocked`. Po spełnieniu kryteriów i pozytywnej walidacji zapisuje `done` tylko wtedy, gdy wymagane review jest aktualne i nie ma problemów blokujących. Jeśli review jest wymagane, implementacja pozostaje `in_progress`, a wynik checkpointu to `implemented_pending_review`. Dotyczy to również pojedynczego milestone'u.

Checkpoint opcjonalnej sekcji w STATUS dotyczy jednego nieopublikowanego zakresu: `single-milestone` (także ręczna seria kolejnych milestone’ów) lub `run-roadmap`. Zawiera identyfikator przebiegu, fazę, uzgodnioną listę milestone'ów, stałą bazę `review_base`, oczekiwany HEAD, stan publikacji i licznik rund. Małe zadanie bez milestone'u nie wymaga tej sekcji.

- Nowy przebieg: zapisz aktualny HEAD jako bazę, zakres i licznik `0`. W repo po `git init` bez commita ustaw `expected_head: unborn`, a `review_base` na SHA pustego drzewa z `git hash-object -t tree --stdin < /dev/null` (bez `-w`). Ta baza działa w diffie i narzędziu snapshotu bez tworzenia commita. Uwzględnij nowe pliki, których sam diff nie pokaże. Pomijaj puste szablony; gdy nie ma pracy, zakończ bez tworzenia przebiegu.
- Wznowienie fazy `implementation`, `review`, `fixes` lub `blocked`: zachowaj identyfikator, bazę, zakres i licznik; odtwórz fakty z Git i checkpointu. Przy blokadzie zachowaj także fazę, do której należy wrócić.
- `complete` oznacza ukończoną implementację, walidację i wymagane review, nie commit ani push. Nie wznawiaj ukończonej implementacji. Oczekująca publikacja zachowuje checkpoint.
- Przygotowanie do publikacji nie zamyka checkpointu. Po udanym commicie stan publikacji wynika z Git: commit musi zawierać uzgodniony wynik oraz końcowy checkpoint z `publication: prepared`. Nie twórz kolejnego commita wyłącznie dla zapisania jego własnego SHA. Przy resume porównaj commit, zawartość i zapisany zakres; sam zmieniony HEAD nie dowodzi publikacji. Push weryfikuj osobno względem zdalnej gałęzi.
- Po rozpoznaniu zakończenia poprzedniego zakresu i jego commita rozpocznij nowy przebieg z nową bazą i licznikiem `0`. Samo planowanie kolejnego PRD nie resetuje checkpointu.
- Jawne zlecenie kolejnego milestone’u lub pozostałej roadmapy przed commitem rozszerza istniejący ukończony zakres bez wymogu publikacji: zachowaj ID, bazę, oczekiwany HEAD, poprzednie wyniki, własność zmian i licznik; dopisz zlecone milestone’y oraz ich ścieżki, zapisz fazę `implementation` i unieważnij zatwierdzenie łącznego wyniku. Nie pytaj ponownie o tak zlecone rozszerzenie. Implementuj tylko nową pracę, a potem zweryfikuj integrację i oceń cały połączony zakres od tej samej bazy. Dawne wyniki pozostają historią dowodów, nie aktualnym zatwierdzeniem nowej całości; jeśli zmieniasz ich zachowanie, otwórz ponownie odpowiednie kryteria i statusy. Limit trzech rund w `run-roadmap` nie zeruje się wskutek rozszerzenia. Aktywnego lub zablokowanego zakresu nie rozszerzaj domyślnie; najpierw rozstrzygnij jego bieżący stan.
- Nieoczekiwany HEAD, brak dowodów publikacji lub zmiany nakładające się na wynik wymagają wyjaśnienia. Nie przesuwaj automatycznie bazy.

## Własność zmian i zakres review

Na starcie odczytaj `git status --short`, `git diff` i `git diff --cached` oraz nowe pliki. Zapisz dokładne ścieżki początkowych zmian użytkownika i ich stan; dla plików istniejących zachowaj skrót treści, a dla usuniętych informację o usunięciu. Dla wcześniejszych zmian w indeksie zachowaj także skrót ich diffu, aby wykryć zmianę indeksu przy niezmienionym worktree. Nie zapisuj treści sekretów w checkpointie.

Domyślnie pracuj na rozłącznych ścieżkach: pliki z wcześniejszymi zmianami użytkownika nie należą do przebiegu i nie mogą być zmieniane, oceniane jako własny wynik ani stage'owane. Jeśli zadanie wymaga edycji takiego pliku (również STATUS lub ROADMAP), sprawdź, czy dotychczasowe polecenie już obejmuje wcześniejszą zmianę. Jeśli nie, ustal z użytkownikiem, czy wchodzi ona do zadania, czy zostanie oddzielona; nie pytaj ponownie o już uzgodniony zakres. Pliki szablonu oraz dokumenty planistyczne powstałe w uzgodnionym wcześniejszym kroku mogą już być objęte zleceniem; rozpoznaj ten fakt zamiast automatycznie uznawać je za obce zmiany. Nie wymagaj czystego repo dla niezależnych plików. Przy świadomym włączeniu wcześniejszej zmiany zapisz to w zakresie; wtedy oceniana i publikowana jest cała uzgodniona zmiana tego pliku. Nie próbuj odtwarzać własności nakładających się zmian wyłącznie z nazw plików.

Przed każdym review i publikacją porównaj pełny status z zakresem checkpointu. Uwzględnij wszystkie zmienione i nowe pliki zadania, również usunięcia i zmiany nazw. Każda pozostała zmiana musi być rozpoznana jako cudza albo wyjaśniona; nie pomijaj po cichu nowego pliku spoza zapisanej listy.

Wykonaj `git diff <review_base> -- <ścieżki_zadania>`, sprawdź osobno indeks i odczytaj zawartość nowych plików. Diff obejmuje końcowy worktree względem stałej bazy; nie wystarcza samo `git diff` ani diff commitów. Nie wykonuj stagingu podczas review. Poprawki oceniaj od tej samej bazy.

## Aktualność oceny

Przed i po review oblicz identyfikator ocenianej treści poleceniem `uv run --script scripts/review-snapshot.py <review_base> -- <ścieżki_zadania>`. Skrypt uwzględnia treść, ścieżki, usunięcia, tryb wykonywalny i dowiązania, także nowe pliki. Przekazuj jawne ścieżki względem katalogu repo; dla zmiany nazwy podaj starą i nową. Zapisz listę ścieżek i wynik jako `review_fingerprint`. Zmiana identyfikatora w czasie review unieważnia jego wynik. Skrót potwierdza tożsamość treści, nie jej poprawność.

STATUS jako pamięć operacyjna pozostaje poza fingerprintem, ale podlega kontroli prawdziwości danych. Wyjątek: gdy jego treść sama jest wymaganym artefaktem (np. zmieniany szablon), zamknij wszystkie dopuszczone edycje STATUS i końcowe statusy ROADMAP przed końcowym review. Do czasu wyniku traktuj przygotowane zakończenie jako warunkowe; nie ogłaszaj sukcesu. Reviewer ocenia również STATUS, a końcową decyzję, fazę, raport i fingerprint zwraca wyłącznie w rozmowie. Nie dopisuj ich po ocenie do tego pliku i nie stosuj do niego wyjątku `status-only`. Ten wyjątek zastępuje nakazy zapisu końcowego checkpointu z innych skillów. Przy CHANGES_REQUIRED popraw przygotowane statusy zgodnie z wynikiem; każda poprawka przechodzi ponowne review. Po utracie dowodu w rozmowie nie ufaj wpisanemu `complete`: wykonaj ocenę ponownie. Publikacja również nie edytuje tak ocenionego STATUS tylko dla ustawienia `publication: prepared`; potwierdza commit z jego zawartości i dostępnego wyniku oceny.

Po review wolno bez kolejnej rundy zmienić wyłącznie statusy ukończenia w ROADMAP i operacyjny checkpoint. Prowadzący porównuje tę małą zmianę z ocenioną wersją, potwierdza brak zmiany zakresu, kryteriów i zależności, a następnie zapisuje nowy fingerprint oraz przyczynę `status-only`. Po utracie rozmowy nie uzasadniaj zmiany fingerprintu samą pamięcią o edycji: jeśli nie da się dowieść, że zmiana była wyłącznie operacyjna, ponów ocenę. Każda inna zmiana ocenianej treści wymaga ponownej oceny zmienionego zakresu; w aktywnym `run-roadmap` obowiązuje review całości i jego dotychczasowy limit rund.

Odroczona redakcja specyfikacji lub README podczas `publish` wymaga kontroli zgodności nowych zapisów z zatwierdzonym zachowaniem. Jeśli zmienia wymagania, kontrakty lub ujawnia zmianę implementacji, unieważnia zatwierdzenie i wraca do osobno zleconego review; publish nie uruchamia go sam. Czystą synchronizację prowadzący sprawdza w diffie, zapisuje nowy fingerprint z przyczyną `docs-sync` i nie przedstawia jej jako niezależnego review. Dokumentacja będąca kryterium akceptacji nie może być odraczana.

## Pamięć i kompakcja

Do publikacji chroń: identyfikator i fazę przebiegu, bazę i oczekiwany HEAD, zakres i własność zmian, wyniki wszystkich milestone'ów, wymaganie review, ostatnią decyzję i fingerprint, łączny licznik rund, nierozwiązane uwagi z identyfikatorami, istotne uzasadnienia odrzuceń, walidację i odłożone decyzje. Zachowuj ostatni raport zwięźle w STATUS; zastępuj wcześniejsze pełne raporty wynikiem ich rozwiązania. Nie twórz osobnych plików raportów bez potrzeby wskazanej przez użytkownika.

Próg rozmiaru jest ostrzeżeniem, nie pozwoleniem na usunięcie aktywnego checkpointu. Dane niecommitowanego przebiegu nie mają gwarantowanej kopii w Git. Kompakcja zachowuje je także w fazie `complete`, jeśli wynik nie został jeszcze opublikowany.

## Wymagania i małe zadania

spec.md opisuje obowiązujące wymagania i decyzje, nie potwierdza ich wdrożenia. Planowana zmiana wskazuje źródłowe PRD i milestone; stan wdrożenia wynika z ROADMAP, STATUS i kodu. Zastąpione decyzje oznacz odnośnikiem do następcy, nie pozostawiaj dwóch sprzecznych aktualnych reguł.

ROADMAP zawiera mapowanie PRD → milestone'y i stan planowania (`partial` lub `planned`) oraz nierozstrzygnięty zakres. `planned` w tym indeksie oznacza uwzględnienie wymagań w planie, nie ukończenie implementacji. Ponowne planowanie tego samego PRD aktualizuje istniejący zakres zamiast go dublować. Nowy PRD nie zmienia bez uzgodnienia zakresu aktywnego przebiegu.

Małe, jasne zadanie może przejść bez PRD i milestone'u: wynik → zmiana → adekwatna walidacja. ROADMAP aktualizuj, jeśli zadanie zmienia istniejący milestone, zależności lub przyszły plan. Trwałe wymagania i decyzje aktualizują spec; STATUS wymaga aktualizacji dla istotnej albo niedomkniętej pracy. Nie twórz milestone'u tylko dla formalności.

## Autoryzacja publikacji

| Polecenie | Dozwolone działanie |
|---|---|
| przygotuj | Synchronizacja dokumentacji i kontrole; bez stagingu, commita i pusha |
| commit | Przygotowanie, staging uzgodnionego zakresu i commit; bez pusha |
| push | Wysłanie istniejących uzgodnionych commitów; bez tworzenia commita i bez edycji dokumentacji tylko na potrzeby tego polecenia |
| opublikuj / commit i push | Przygotowanie, potrzebny commit i push uzgodnionego zakresu |

`push` z niecommitowaną pracą nie publikuje tej pracy: poinformuj o tym i nie twórz commita bez upoważnienia. Jeśli polecenie dotyczy właśnie tej pracy, zgłoś potrzebę commita zamiast wysyłać inny zakres. Jawne ograniczenia użytkownika mają pierwszeństwo.

Przed commitem sprawdź także istniejący indeks. Nie dołączaj cudzych wcześniej stage'owanych plików; nie usuwaj ich z indeksu bez zgody. Jeżeli nie można utworzyć commita wyłącznie uzgodnionego zakresu z zachowaniem pozostałego indeksu, zatrzymaj publikację i wyjaśnij konflikt. Przy mieszanych zmianach w jednym pliku sam wybór ścieżki nie izoluje cudzej pracy.

Przed pushem sprawdź docelowy remote, branch i wszystkie wychodzące commity. Nie wysyłaj nieuzgodnionej historii i nie wykonuj force push jako części domyślnego flow.
