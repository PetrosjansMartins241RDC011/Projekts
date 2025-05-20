# Automatizēta ēdiena recepšu izvēlēšanās savam mērķim
## Projekta uzdevums
Projekta uzdevums ir atvieglot ēdienu recepšu izvēli atbilstoši lietotāja uztura mērķiem - vai tas būtu kaloriju deficīts svara samazināšanai (cutting), esošā svara saglabāšana veselīgā uzturā (maintaining), vai muskuļu masas palielināšana, ēdot kalorijām un proteīniem bagātākus ēdienus (bulking). Ar šīs programmatūras palīdzību tiek automatizēta ēdiena recepšu meklēšana un atlasīšana no dažādām tīmekļa vietnēm, kas palīdz lietotājiem ātrāk un ērtāk atrast piemērotus ēdienu pagatavošanas variantus savām vajadzībām. 
## Par izmantotajām bibliotēkām
### import requests
Šī bibliotēka ļauj piekļūt tīmekļa lapas saturam, manā gadījumā HTML saturam. Ar šīs bibliotēkas palīdzību es spēju apstrādāt HTTP statusa kodus, piemēram, piekļūt pie headers. "requests" bibliotēka saņem šo HTML kodu un tad saglaba to html.text, kurš pēctam nogādā šo informāciju manai otrajai izmantotajai bibliotēkai "BeautifulSoup". Ja netiktu izmantota šī bibliotēka, tad mana programma nespētu ielādēt tīmekļa lapas, no kurām es iegūstu receptes.
### from bs4 import BeautifulSoup
Šī bibliotēka ļauj analizēt un apstrādāt HTML datus Python valodā. Ar "BeautifulSoup" palīdzību es spēju izmantot metodes .find(), .find_all(), .text, .attrs, ar kuru palīdzību var viegli izpētīt un analizēt datus. Manā kodā šī bibliotēka ir domāta, lai atrastu vairākus HTML elementus, piemēram "div", "h2", "h3", "p", zem kuriem slēpjas informācija, kura man ir vajadzīga. 
Tātad "requests" bibliotēka iegūst HTML kodu no tīmekļa, bet "BeautifulSoup" apstrādā HTML un izvelk no tā datus. Bez "requests" bibliotēkas nebūtu iespējams piekļūt vajadzīgajām lapām, bet bez "BeautifulSoups" es nespētu apstrādāt šos HTML datus.
## Projektā izmantotās datu struktūras
### ALL_the_URLs
Šī vārdnīca glabā iekšā visas izmantotās tīmekļa adreses, piemēram, adresi uz "cutting", "maintaining" un "bulking". Nodrošina ērtu un dinamisku piekļuvi datiem pēc lietotāja izvēles.
### get_cutting_recipes()
Šī funkcija iegūst diētu receptes cilvēkiem, kuri vēlas samazināt savu svaru. Funkcija ar "BeautifulSoup" palīdzību analizē iegūto HTML saturu un atrod visus HTML elementus ar klasēm, kurāš glabājas receptes.
### get_maintaining_recipes()
Šī funkcija iegūst diētu receptes cilvēkiem, kuri vēlas uzturēt savu svaru. Funkcijas ideja ir tāda pati, kā funkcijai "get_cutting_recipes()" un izpilda to pašu tikai atrodot citas diētas receptes.
### get_bulking_recipes()
Šī funkcija iegūst diētu receptes cilvēkiem, kuri vēlas palielināt savu svaru. Funkcijas ideja ir tāda pati, kā funkcijai "get_cutting_recipes()".
### display_recipes(recipes)
Funkcija izvada diētu receptes sarakstu uz ekrāna. Šī funkcija pieņem kā argumentu "recipes" un izmanto "enumerate()", lai katrai receptei varētu pievienot kārtas numuru.
### main()
Šī ir galvenā programmas funkcija, kas vada visu programmas darbību. Tā izdrukā izvēlni ar trim iespējām: cutting, maintaining, bulking. Pieprasa lietoāja ievadi, pārbauda vai lietotājs ir pareizi ievadījis tekstu kodā, atkarībā no izvēles izsauc attiecīgi vajadzīgo get_..._recipes() funkciju. Izdrukā iegūtās diētas receptes ar display_recipes() funkcijas palīdzību. Prasa lietotājam izvēlēties konkrētu recepti no 1 līdz 7. Un visbeigās parāda tīmekļa vietni uz izvēlēto diētas recepti.
## Programmatūras izmantošanas metodes
Šī programma piedāvā lietotājam izvēlēties sev piemēroto diētu, piemēram, svara samazināšanu (cutting), svara uzturēšanu (maintaining) un svara palielināšanu (bulking). Receptes iegūst no konkrētām mājaslapām atkarībā no izvēlētā diētas veida, un izmanto "requests" bibliotēku, lai ielādētu tīmekļa saturu un "BeautifulSoup", lai analizētu HTML kodu un izvilktu vajadzīgo informāciju. Tiek lietotājam parādītas 7 pirmās receptes ar aprakstiem, un tad lietotājs var izvēlēties vienu no receptēm (ievadot skaitli no 1 līdz 7), lai saņemtu tiešo saiti uz pilno recepti. Šo programmatūru var praktiski pielietot savā personīgajā uztura plānā, kur katru dienu lietotājs izvēlās savu mērķi un iegūst idejas ēdienreizēm bez nepieciešamības pašam meklēt. 
