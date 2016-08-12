# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'it'

dateSep = ['/', '-']
usesMeridian = False
uses24 = True

Weekdays = [
    'lunedì', 'martedì', 'mercoledì',
    'giovedì', 'venerdì', 'sabato', 'domenica',
]
shortWeekdays = [
    'lun', 'mar', 'mer',
    'gio', 'ven', 'sab', 'dom',
]
Months = [
    'gennaio', 'febbraio', 'marzo',
    'aprile', 'maggio', 'giugno',
    'luglio', 'agosto', 'settembre',
    'ottobre', 'novembre', 'dicembre',
]
shortMonths = [
    'gen', 'feb', 'mar',
    'apr', 'mag', 'giu',
    'lug', 'ago', 'set',
    'ott', 'nov', 'dic',
]

dateFormats = {
    'full': 'EEEE, dd MMMM yyyy',
    'long': 'dd MMMM yyyy',
    'medium': 'dd-MM-yyyy',
    'short': 'dd-MM-yy',
}

timeFormats = {
    'full': 'HH:mm:ss v',
    'long': 'HH:mm:ss z',
    'medium': 'HH:mm:ss',
    'short': 'HH:mm',
}

dp_order = ['d', 'm', 'y']

# Used to parse expressions like "in 5 hours"
numbers = {
    'zero': 0,
    'uno': 1,
    'una': 1,
    'un': 1,
    'un\'': 1,
    'due': 2,
    'tre': 3,
    'quattro': 4,
    'cinque': 5,
    'sei': 6,
    'sette': 7,
    'otto': 8,
    'nove': 9,
    'dieci': 10,
    'undici': 11,
    'tredici': 13,
    'quattordici': 14,
    'quindici': 15,
    'sedici': 16,
    'diciassette': 17,
    'diciotto': 18,
    'diciannove': 19,
    'venti': 20,
}

decimal_mark = ','

# the short version would be a capital M,
# as I understand it we can't distinguish
# between m for minutes and M for months.

units = {
    'seconds': ['secondo', 'secondi', 'sec', 's'],
    'minutes': ['minuto', 'minuti', 'min', 'm'],
    'hours': ['ora', 'ore', 'h'],
    'days': ['giorno', 'giorni', 'g'],
    'weeks': ['settimana', 'settimane'],
    'months': ['mese', 'mesi'],
    'years': ['anno', 'anni'],
}

re_values = re_values.copy()
re_values.update({
    'specials': 'in|alle|per le| all\'| al',
    'timeseparator': ':',
    'rangeseparator': '-',
    'daysuffix': '',
    'qunits': 'h|m|s|d|w|m|j',
    'now': ['adesso'],
})

# Used to adjust the returned date before/after the source
# still looking for insight on how to translate all of them to german.
Modifiers = {
    'da': 1,
    'dalle': 1,
    'prima': -1,
    'dopo': 1,
    'fa': -1,
    'poi': 1,
    'precendente': -1,
    'fine di': 0,
    'questo': 0,
}

# morgen/abermorgen does not work, see
# http://code.google.com/p/parsedatetime/issues/detail?id=19
dayOffsets = {
    'dopodomani': 2,
    'domani': 1,
    'oggi': 0,
    'ieri': -1,
    'l\'altro ieri': -2,
}

# special day and/or times, i.e. lunch, noon, evening
# each element in the dictionary is a dictionary that is used
# to fill in any value to be replace - the current date/time will
# already have been populated by the method buildSources
re_sources = {
    'mezzogiorno': {'hr': 12, 'mn': 0, 'sec': 0},
    'mezzanotte': {'hr': 0, 'mn': 0, 'sec': 0},
}

small = {
    'zero': 0,
    'uno': 1,
    'un': 1,
    'una': 1,
    'un\'': 1,
    'due': 2,
    'tre': 3,
    'quattro': 4,
    'cinque': 5,
    'sei': 6,
    'sette': 7,
    'otto': 8,
    'nove': 9,
    'dieci': 10,
    'undici': 11,
    'dodici': 12,
    'tredici': 13,
    'quattordici': 14,
    'quindici': 15,
    'sedici': 16,
    'diciassette': 17,
    'diciotto': 18,
    'diciannove': 19,
    'venti': 20,
    'trenta': 30,
    'quaranta': 40,
    'cinquanta': 50,
    'sessanta': 60,
    'settanta': 70,
    'ottanta': 80,
    'novanta': 90
}
