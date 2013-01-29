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
from __future__ import unicode_literals

from datetime import datetime
version = '0.1'

plural_de = lambda singular, plural, numero: numero > 1 and plural or singular


class Restante(object):
    def __init__(self, valor, unidade):
        self.valor = valor
        self.unidade = unidade

    @property
    def pouco_mais_de_1_minuto(self):
        if self.valor < 5 and self.unidade == 'minuto':
            return True
        elif self.valor < 60 and self.unidade == 'segundos':
            return True

        return False

    @property
    def meia_hora(self):
        if self.valor == 30 and self.unidade == 'minutos':
            return True

        return False

    @property
    def string(self):
        if self.valor > 0:
            return " e %d %s" % (self.valor, self.unidade)
        return ""


class TempoRelativo(object):
    possibilidades = (
      (60 * 60 * 24 * 365, lambda n: plural_de('ano', 'anos', n)),
      (60 * 60 * 24 * 30, lambda n: plural_de('mês', 'meses', n)),
      (60 * 60 * 24 * 7, lambda n: plural_de('semana', 'semanas', n)),
      (60 * 60 * 24, lambda n: plural_de('dia', 'dias', n)),
      (60 * 60, lambda n: plural_de('hora', 'horas', n)),
      (60, lambda n: plural_de('minuto', 'minutos', n)),
    )

    def __init__(self, anterior):
        self.now = datetime.now()
        self.anterior = anterior
        self.delta = self.now - self.anterior
        self.decorrido = (self.delta.days * 24 * 60 * 60) + self.delta.seconds

    @property
    def string(self):
        for total, (segundos, unidade_de_tempo) in enumerate(self.possibilidades):
            restante = None
            if self.decorrido >= segundos:
                valor = int(self.decorrido / segundos)
                string = "%d %s" % (valor, unidade_de_tempo(valor))
                extra = float(self.decorrido) / segundos > valor
                proximo = (total + 1)

                if extra:
                    sobra = self.decorrido - (segundos * valor)
                    if len(self.possibilidades) > proximo:
                        segundos_restantes, unidade_restante = self.possibilidades[proximo]
                        valor_restante = sobra / segundos_restantes
                        restante = Restante(valor_restante, unidade_restante(valor_restante))
                    else:
                        restante = Restante(sobra, plural_de('segundo', 'segundos', sobra))

                return string, restante

    @property
    def ha(self):
        if self.decorrido < 60:
            return 'há menos de um minuto'

        string, restante = self.string

        predicado = ""
        if restante:
            if restante.pouco_mais_de_1_minuto:
                predicado = " pouco mais de"
            elif restante.meia_hora:
                string += " e meia"
            else:
                string += restante.string

        return "há%s %s" % (predicado, string)

    @property
    def atras(self):
        if self.decorrido < 60:
            return 'alguns segundos atrás'

        string, restante = self.string

        if restante:
            string += restante.string

        return "%s atrás" % string

    def __unicode__(self):
        return self.ha

    def __repr__(self):
        return self.atras
