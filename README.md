# Projekts
Projekts par recepšu izvēlēšanos dažādām vajadzībām.
## Projekta uzdevums
Projekta uzdevums ir atvieglināt ēdienu recepšu izvēli katrai cilvēku grupai, vai nu tie vēlas būt uz kaloriju deficīta, vai saglabāt savu sākotnējo svaru ēdot veselīgi, vai nu arī iegūt muskuļu masu ēdot bagātākus kaloriju ēdienus ar vairāk proteīna.
## Par izmantotajām bibliotēkām
### import requests
Šī bibliotēka ļauj piekļūt tīmekļa lapas saturam, manā gadījumā HTML saturam. Ar šīs bibliotēkas palīdzību es spēju apstrādāt HTTP statusa kodus, piemēram, piekļūt pie headers. "requests" bibliotēka saņem šo HTML kodu un tad saglaba to html.text, kurš pēctam nogādā šo informāciju manai otrajai izmantotajai bibliotēkai "BeautifulSoup". Ja netiktu izmantota šī bibliotēka, tad mana programma nespētu ielādēt tīmekļa lapas, no kurām es iegūstu receptes.
### from bs4 import BeautifulSoup
Šī bibliotēka ļauj analizēt un apstrādāt HTML datus Python valodā. Ar "BeautifulSoup" palīdzību es spēju izmantot metodes .find(), .find_all(), .text, .attrs, ar kuru palīdzību var viegli izpētīt un analizēt datus. Manā kodā šī bibliotēka ir domāta, lai atrastu vairākus HTML elementus, piemēram "div", "h2", "h3", "p", zem kuriem slēpjas informācija, kura man ir vajadzīga. 
Tātad "requests" bibliotēka iegūst HTML kodu no tīmekļa, bet "BeautifulSoup" apstrādā HTML un izvelk no tā datus. Bez "requests" bibliotēkas nebūtu iespējams piekļūt vajadzīgajām lapām, bet bez "BeautifulSoups" es nespētu apstrādāt šos HTML datus.
## Programmatūras izmantošanas metodes
Šī programma piedāvā lietotājam izvēlēties sev piemēroto diētu, piemēram, svara samazināšanu (cutting), svara uzturēšanu (maintaining) un svara palielināšanu (bulking). Receptes iegūst no konkrētām mājaslapām atkarībā no izvēlētā diētas veida, un izmanto "requests" bibliotēku, lai ielādētu tīmekļa saturu un "BeautifulSoup", lai analizētu HTML kodu un izvilktu vajadzīgo informāciju. Tiek lietotājam parādītas 7 pirmās receptes ar aprakstiem, un tad lietotājs var izvēlēties vienu no receptēm (ievadot skaitli no 1 līdz 7), lai saņemtu tiešo saiti uz pilno recepti. Šo programmatūru var praktiski pielietot savā personīgajā uztura plānā, kur katru dienu lietotājs izvēlās savu mērķi un iegūst idejas ēdienreizēm bez nepieciešamības pašam meklēt. 
