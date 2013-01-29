# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# <vargas - tempo relativo em português brasileiro, para python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from sure import expect
from vargas import TempoRelativo
from datetime import datetime, timedelta


def test_vargas_should_ter_um_numero_de_versao():
    u"vargas deveria ter um numero de versao"
    import vargas
    expect(vargas.version).to.equal("0.1")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_menos_de_1_minuto_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha menos de 1 minuto atras"
    relative_time = datetime.now() - timedelta(seconds=55)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há menos de um minuto")
    expect(decorrido.atras).to.equal(u"alguns segundos atrás")
    expect(unicode(decorrido)).to.equal(u"há menos de um minuto")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_minuto_e_meio_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 minuto e meio atras"
    relative_time = datetime.now() - timedelta(seconds=90)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há pouco mais de 1 minuto")
    expect(decorrido.atras).to.equal(u"1 minuto e 30 segundos atrás")
    expect(unicode(decorrido)).to.equal(u"há pouco mais de 1 minuto")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_minuto_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 minuto atras"
    relative_time = datetime.now() - timedelta(minutes=1)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 minuto")
    expect(decorrido.atras).to.equal(u"1 minuto atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 minuto")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_minutos_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 minutos atras"
    relative_time = datetime.now() - timedelta(minutes=4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 minutos")
    expect(decorrido.atras).to.equal(u"4 minutos atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 minutos")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_55_minutos_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 55 minutos atras"
    relative_time = datetime.now() - timedelta(minutes=55)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 55 minutos")
    expect(decorrido.atras).to.equal(u"55 minutos atrás")
    expect(unicode(decorrido)).to.equal(u"há 55 minutos")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_hora_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 hora atras"
    relative_time = datetime.now() - timedelta(minutes=60)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 hora")
    expect(decorrido.atras).to.equal(u"1 hora atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 hora")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_horas_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 horas atras"
    relative_time = datetime.now() - timedelta(minutes=60 * 4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 horas")
    expect(decorrido.atras).to.equal(u"4 horas atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 horas")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_dia_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 dia atras"
    relative_time = datetime.now() - timedelta(minutes=60 * 24)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 dia")
    expect(decorrido.atras).to.equal(u"1 dia atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 dia")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_dias_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 dias atras"
    relative_time = datetime.now() - timedelta(minutes=(60 * 24) * 4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 dias")
    expect(decorrido.atras).to.equal(u"4 dias atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 dias")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_hora_e_24_minutos_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 hora e 24 minutos atras"
    relative_time = datetime.now() - timedelta(minutes=84)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 hora e 24 minutos")
    expect(decorrido.atras).to.equal(u"1 hora e 24 minutos atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 hora e 24 minutos")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_horas_atras_3min():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 horas e e minutos atras"
    relative_time = datetime.now() - timedelta(minutes=(60 * 4) + 3)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 horas e 3 minutos")
    expect(decorrido.atras).to.equal(u"4 horas e 3 minutos atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 horas e 3 minutos")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_pouco_mais_de_1_hora_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 hora atras"
    relative_time = datetime.now() - timedelta(minutes=61)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há pouco mais de 1 hora")
    expect(decorrido.atras).to.equal(u"1 hora e 1 minuto atrás")
    expect(unicode(decorrido)).to.equal(u"há pouco mais de 1 hora")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_hora_e_meia():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 hora atras"
    relative_time = datetime.now() - timedelta(minutes=90)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 hora e meia")
    expect(decorrido.atras).to.equal(u"1 hora e 30 minutos atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 hora e meia")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_semana_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 semana atras"
    relative_time = datetime.now() - timedelta(minutes=60 * 24 * 7)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 semana")
    expect(decorrido.atras).to.equal(u"1 semana atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 semana")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_semanas_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 semanas atras"
    relative_time = datetime.now() - timedelta(minutes=(60 * 24 * 7) * 4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 semanas")
    expect(decorrido.atras).to.equal(u"4 semanas atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 semanas")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_mes_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 mês atras"
    relative_time = datetime.now() - timedelta(minutes=60 * 24 * 30)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 mês")
    expect(decorrido.atras).to.equal(u"1 mês atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 mês")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_meses_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 meses atras"
    relative_time = datetime.now() - timedelta(minutes=(60 * 24 * 30) * 4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 meses")
    expect(decorrido.atras).to.equal(u"4 meses atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 meses")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_mes_atras_com_31_dias():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 mês atras"
    relative_time = datetime.now() - timedelta(minutes=60 * 24 * 31)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 mês")
    expect(decorrido.atras).to.equal(u"1 mês atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 mês")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_mess_atras_com_31_dias():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 meses atras"
    relative_time = datetime.now() - timedelta(minutes=(60 * 24 * 31) * 4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 meses")
    expect(decorrido.atras).to.equal(u"4 meses atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 meses")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_1_ano_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 1 ano atras"
    relative_time = datetime.now() - timedelta(minutes=60 * 24 * 365)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 1 ano")
    expect(decorrido.atras).to.equal(u"1 ano atrás")
    expect(unicode(decorrido)).to.equal(u"há 1 ano")


def test_tempo_should_descrever_quando_difereca_de_tempo_ocorreu_ha_4_anos_atras():
    u"TempoRelativo deveria descrever quando diferenca de tempo ocorreu ha 4 anos atras"
    relative_time = datetime.now() - timedelta(minutes=(60 * 24 * 365) * 4)
    decorrido = TempoRelativo(relative_time)
    expect(decorrido.ha).to.equal(u"há 4 anos")
    expect(decorrido.atras).to.equal(u"4 anos atrás")
    expect(unicode(decorrido)).to.equal(u"há 4 anos")
