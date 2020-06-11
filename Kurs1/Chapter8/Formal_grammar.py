﻿Регулярные выражения - разновидность формальной граматики.
В формальной грамматике существует набор допустимых символов. который называется алфовитом грамматики. 
Также существует набор символов который допустим, но не относится алфовиту. 
Такие символы называют "Нетерминальные символы". Обозначают в "< >". Пример "<НАЧАЛО>".
Обычно "Нетерминальные символы" обозначают с большой буквы. Среди "Нетерминальных символов" выбирается
один, который обозначается как главный (стартовый). После этого задаются правила, согласно которым каждая
последовательность символов слева от стрелки заменяется на какую-то последовательность символов справа от стрелки.


Пример:


<НАЧАЛО>            ->  <ИМЯ-ПЕРЕМЕННОЙ>
<НАЧАЛО>            ->  <ИМЯ-ПЕРЕМЕННОЙ><ЗНАК-ОПЕРАЦИИ><ИМЯ-ПЕРЕМЕННОЙ>
<ЗНАК-ОПЕРАЦИИ>     ->  +           #Строки с 16-19 можно заменить на одну
<ЗНАК-ОПЕРАЦИИ>     ->  -           #<ЗНАК-ОПЕРАЦИИ>     ->  + | - | * | /
<ЗНАК-ОПЕРАЦИИ>     ->  *           #Но так писать пока мы не имеем права, т.к.
<ЗНАК-ОПЕРАЦИИ>     ->  /           #мы не определили, что знак "|" означает "или"
<ИМЯ-ПЕРЕМЕННОЙ>    ->  <БУКВА>
<ИМЯ-ПЕРЕМЕННОЙ>    ->  <ИМЯ-ПЕРЕМЕННОЙ><БУКВА>
<ИМЯ-ПЕРЕМЕННОЙ>    ->  <ИМЯ-ПЕРЕМЕННОЙ><ЦЫФРА>
<БУКВА>             ->  A
                        .
                        .
<БУКВА>             ->  Z
<ЦЫФРА>             ->  0
                        .
                        .
<ЦЫФРА>             ->  9

После применения прав на строке №14 мы должны будем применить правило либо №20, либо №21, либо №22.
Выбор правила абсолютно произвольный. Процесс продолжается минимум до тех пор у нас на экране не останется
ни одного "Нетерминального символа". 
Можно немного усложнить:
01                  ->  !
т.е. последовательность "01" заменяется на восклицательный знак. При этом это правило мы применять не обязаны.
Если мы в строке обнаружим сочетание "01", то на наше усмотрение, что мы будем делаеть дальше: остановиться или идти дальше.
Этим и отличается "Формальная грамматика" от "Нормальных алгоритмов". В Python очень часто используются всякие способы для 
формализации алгоритмов. Например как нужно написать программу, которая будет определеённым образом обрабатывать наборы строк, 
для этого и используются "Нормальные алгоритмы"
Мы не обязаны применять то или иное правило только при условии, что на доске не будет ни одного терминального символа.
В строке №36 мы ввели правило замены последовательности двух символов на один. Если это правило убрать и у нас всегда от стрелки
слева будет один символ, неважно терминальный или нет, как правило не "Нетерминального символа", то такая грамматика как правило 
применяется для языков программирования и называется "Контекстно свободной грамматикой". Смысл её в том, что один тот же смысловой
термин (Нетерминальный символ) означает одно и тоже не в зависимости от того, где он встречается. Для языков программирования, имя 
это всегда имя, а имя переменной или имя функции это зависит от ситуации.

Делаем обратную задачу берем выражение
    AS1+S12 
по нему легко можно понять как оно построено, в частности применено правило №15 за ним №20 и т.д. И если мы сумеем последовательно
вычислить какие правила были применимы, то что мы получим называется "Деревом синтаксического разбора". Для построения 
"Дерева синтаксического разбора" необходимо понять, какие последовательно правила были применены к нашей строке. Так как порядок
применения правил произволен, то синтаксический разбор на такой грамматике дело трудоёмкое. Поэтому для обработки строки, пришедшей 
к нам на вход мы должны были бы описать формальную грамматику, желательно контекстно свободную, потом заставить наш интерпретатор при 
помощи какой то встроенной библиотеки попытаться угадать, а строка попавшая к нам на вход вообще соответствует нашей формальной грамматике,
какие части той входной строки каким нетерминальным символам сооветствует. Такого рода разбор дело весьма трудоёмкое (это можно посмотреть
по скорости компиляции даже не очень большого файла). имено по этому возникает задача, прежде чем осуществлять разбор определить входная
строка правильная или нет. Для такой цели придумали разновидность контекстно свободной грамматики. В частности мы удалим из ранее
представленной формальной грамматики всё, что не касается <ИМЯ-ПЕРЕМЕННОЙ>:

<НАЧАЛО>            ->  <ИМЯ-ПЕРЕМЕННОЙ>
<ИМЯ-ПЕРЕМЕННОЙ>    ->  A
                        .
                        .
<ИМЯ-ПЕРЕМЕННОЙ>    ->  Z
<ИМЯ-ПЕРЕМЕННОЙ>    ->  A<ИМЯ-ПЕРЕМЕННОЙ>
                        .
                        .
<ИМЯ-ПЕРЕМЕННОЙ>    ->  Z<ИМЯ-ПЕРЕМЕННОЙ>

Теперь слева от стрелки у нас один символ, а справа от стрелки у нас стоит либо один символ либо два, но первый символ всегда терминальный а 
второй нет. Но при этом полностью потерялся смысл выражения (не понятно что эти буквы означают). Если удаётся описать входную строку грамматикой
такого вида, иногда это удаётся, то такая грамматика носит название "Регулярная грамматика". Ничего более, чем понять правильный входной текст или
ненравильный. Поэтому при построении компиляторов, всегда есть актуальная задача, если нам дана некая формальная грамматика, то можно ли построить
регулярную грамматику, которая даёт тот же набор строк. Но всё таки возможности регулярной грамматики очень ограничены и способ записи очень не удобен,
поэтому придумали упрощенный способ записи регулярных грамматик и плюс к этому разрешили некие вольности, т.е. не только запись вида:
<ИМЯ-ПЕРЕМЕННОЙ>    ->  А<ИМЯ-ПЕРЕМЕННОЙ>
    но и такую запись
<ИМЯ-ПЕРЕМЕННОЙ>    ->  АА
т.е. состаящую из двух терминальных символов. Разрешили в некоторых случаях писать два нетерминальных символа подряд, т.е. плюс к этому ещё некие вольности
и мы получили то что называется "Регулярными выражениями". Регулярное выражение - это некий вид контекстно свободной грамматики, которая в целом стремится 
быть регулярной, но допускает незначительные вольности, т.е. она не строго регулярная (Эти вольности определяются удобствами). на самом деле форм 
регулярных выражений очень много. та из них, которая которая используется как правило называется "Posix регулярные выражения", т.е. это регулярные выражения
соответствующие Posix стандарту. Posix стандарт характерен тем, что он некоторые нетерминальные символыграмматики записывает одноимённым способом,
например записывается символьная строка (pattern) 
 