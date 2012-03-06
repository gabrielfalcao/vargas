# vargas - tempo relativo em português, para Python

## versão 0.1

## o que é?

Uma lib que retorna o tempo relativo por extenso, idealizando a
não-dependência das configurações de locale do ambiente.

recebe um objeto
[datetime](http://docs.python.org/library/datetime.html#datetime.datetime)
e automaticamente calcula o delta comparado com a data e hora atuais.

## funcionalidades

retorna 2 possibilidades de strings, uma mais formal outra
informal. Mas o padrão é a "informal".

## modo de usar


    >>> from vargas import TempoRelativo
    >>> decorrido = TempoRelativo(datetime.strptime("23:43:44 26/12/2010", "%H:%M:%S %d/%m/%Y"))

    >>> print decorrido.ha
    há pouco mais de 1 minuto

## exemplos

vamos considerar as seguintes variáveis:

    from datetime import datetime, timedelta

    ha_30_segundos = datetime.now() - timedelta(seconds=30)
    ha_1_minuto_e_30_segundos = datetime.now() - timedelta(seconds=90)
    ha_5_minutos = datetime.now() - timedelta(minutes=5)
    ha_1_hora = datetime.now() - timedelta(minutes=60)
    ha_2_dias_e_3_horas = datetime.now() - timedelta(minutes=(60 * 48) + 180)

temos:

    >>> from vargas import TempoRelativo
    >>> decorrido = TempoRelativo(ha_30_segundos)
    >>> print decorrido.ha
    há menos de um minuto

    >>> print decorrido.atras
    alguns segundos atrás


    >>> from vargas import TempoRelativo
    >>> decorrido = TempoRelativo(ha_1_minuto_e_30_segundos)
    >>> print decorrido.ha
    há pouco mais de 1 minuto

    >>> print decorrido.atras
    1 minuto e 30 atrás


    >>> from vargas import TempoRelativo
    >>> decorrido = TempoRelativo(ha_5_minutos)
    >>> print decorrido.ha
    há 5 minutos

    >>> print decorrido.atras
    5 minutos atrás


    >>> from vargas import TempoRelativo
    >>> decorrido = TempoRelativo(ha_1_hora)
    >>> print decorrido.ha
    há 1 hora

    >>> print decorrido.atras
    1 hora atrás


    >>> from vargas import TempoRelativo
    >>> decorrido = TempoRelativo(ha_2_dias_e_3_horas)
    >>> print decorrido.ha
    há 2 dias e 3 horas

    >>> print decorrido.atras
    2 dias e 3 horas atrás


# rodando testes

instale a dependência "sure":

    sudo pip install -r requirements.pip

depois basta rodar o make:

    make test


# contribuições

É simples!

Mande testes + código no pull request

# TODO

   Extender para outros idiomas, mas sem usar GNU/gettext.

   Lembrando sempre que o propósito desta lib é ser **livre** de configurações de
   [locale](http://www.gnu.org/s/libc/manual/html_node/Locales.html).

# licença

    <vargas - tempo relativo em português brasileiro, para python>
    Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

