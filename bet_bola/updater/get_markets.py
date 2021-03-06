from core.models import Cotation, Game, Market
from .market_translations import MARKET_TRANSLATIONS
import re
import decimal

def get_translated_cotation_with_header_goals(cotation_name):
    TRANSLATE_TABLE = {
        'Over': 'Acima',
        'Under':'Abaixo',
        'Home':'Casa',
        'Away':'Fora',
        'Score Draw': 'Empate',
        'No Goal': 'Nenhum Gol'
    }

    cotation_translated = cotation_name.strip()
    for header in TRANSLATE_TABLE.keys():
        cotation_translated = re.sub('\\b' + header + '\\b', TRANSLATE_TABLE.get(header, header), cotation_translated)
    return cotation_translated.strip()


def get_translated_cotation_with_header_name(cotation_name):
    TRANSLATE_TABLE = {
        'Yes':'Sim',
        'No':'Não',
        'Draw':'Empate',
        '2nd Half':'2° Tempo',
        '1st Half':'1° Tempo',
    }
    cotation_translated = cotation_name.strip()
    for header in TRANSLATE_TABLE.keys():
        cotation_translated = re.sub('\\b' + header + '\\b', TRANSLATE_TABLE.get(header, header), cotation_translated)
    return cotation_translated.strip()


def get_translated_cotation_with_header_name_special(cotation_name):
    TRANSLATE_TABLE = {
        'Home': 'Casa',
        'Away': 'Fora',
        'To Win to Nil':'Ganhar sem tomar Gol',
        'To Win Either Half': 'Ganhar Qualquer Etapa',
        'To Win Both Halves': 'Ganhar Ambas Etapas',
        'To Score in Both Halves': 'Marcar em Ambas Etapas'
    }

    cotation_translated = cotation_name.strip()
    for header in TRANSLATE_TABLE.keys():
        cotation_translated = re.sub('\\b' + header + '\\b', TRANSLATE_TABLE.get(header, header), cotation_translated)
    return cotation_translated.strip()



def get_translated_cotation_with_opp(cotation_name):
    TRANSLATE_TABLE = {
        'or': 'ou',
        '1X':'Casa/Empate',
        'X2':'Empate/Fora',
        '12':'Casa/Fora',
        'Over': 'Acima',
        'Under':'Abaixo',
        'Draw':'Empate',
        'No Goal': 'Sem Gols',
        'Yes': 'Sim',
        'No': 'Não',
        'Goals':'Gols',
        'goals':'Gols',
        'Both Teams':'Ambos os Times',
        'Only':'Apenas',
        'No Goals': 'Sem Gols',
        '1st Half': '1° Tempo',
        '2nd Half': '2° Tempo',
        'Tie':'Igual',
        'Even': 'Par',
        'Odd':'Ímpar',
        'Home':'Casa',
        'Away':'Fora',
        'X':'Empate'
    }
    cotation_translated = cotation_name.strip()
    for header in TRANSLATE_TABLE.keys():
        cotation_translated = re.sub('\\b' + header + '\\b', TRANSLATE_TABLE.get(header, header), cotation_translated)
    return cotation_translated.strip()
  

def get_translated_cotation_with_opp_standard(cotation_name):
    TRANSLATE_TABLE = {
        '1':'Casa',
        '2': 'Fora',
        'X':'Empate',
    }
    
    cotation_translated = cotation_name.strip()
    for header in TRANSLATE_TABLE.keys():
        cotation_translated = re.sub('\\b' + header + '\\b', TRANSLATE_TABLE.get(header, header), cotation_translated)
    return cotation_translated.strip()


def extract_goals_from_string(string):
    total_goals = re.findall(r"[-+]?\d*\.\d+|\d+", string)
    return total_goals[-1] if total_goals else None


def cotation_with_header_goals(cotations, market_name, game_id):
    for cotation in cotations:

        try:
            price = decimal.Decimal(cotation['odds'])
        except decimal.InvalidOperation:
            price = 0

        total_goals = extract_goals_from_string(cotation['goals'].strip())
        if total_goals:
            obj, created = Cotation.objects.update_or_create(
                name=get_translated_cotation_with_header_goals(cotation['header'] + ' ' + cotation['goals']),
                game=Game.objects.get(pk=game_id),
                total_goals=total_goals,
                market=Market.objects.get_or_create(
                    name=MARKET_TRANSLATIONS.get(market_name, market_name),
                )[0],
                defaults={
                    'price': price
                }
            )

def cotation_with_header_opp(cotations, market_name, game_id):
    for cotation in cotations:

        try:
            price = decimal.Decimal(cotation['odds'])
        except decimal.InvalidOperation:
            price = 0

        Cotation.objects.update_or_create(
            name=get_translated_cotation_with_opp(cotation['header']) + ' ' + cotation['opp'],
            game=Game.objects.get(pk=game_id),
            market=Market.objects.get_or_create(
                name=MARKET_TRANSLATIONS.get(market_name, market_name),
            )[0],
            defaults={
                'price': price
            }
        )


def cotation_with_header_name(cotations, market_name, game_id):
    for cotation in cotations:

        try:
            price = decimal.Decimal(cotation['odds'])
        except decimal.InvalidOperation:
            price = 0

        Cotation.objects.update_or_create(
            name=get_translated_cotation_with_header_name(cotation['header'] + ' - ' + cotation['name']),
            game=Game.objects.get(pk=game_id),
            market=Market.objects.get_or_create(
                name=MARKET_TRANSLATIONS.get(market_name, market_name),
            )[0],
            defaults={
                'price': price
            }
        )


def cotation_with_header_name_special(cotations, market_name, game_id):
    allowed = ('To Win to Nil','To Win Either Half','To Win Both Halves','To Score in Both Halves')
    for cotation in cotations:

        try:
            price = decimal.Decimal(cotation['odds'])
        except decimal.InvalidOperation:
            price = 0

        if cotation['name'] in allowed:
            Cotation.objects.update_or_create(
                name=get_translated_cotation_with_header_name_special(cotation['header'] + ' - ' + cotation['name']),
                game=Game.objects.get(pk=game_id),
                market=Market.objects.get_or_create(
                    name=MARKET_TRANSLATIONS.get(market_name, market_name),
                )[0],
                defaults={
                    'price': price
                }
            )



def cotation_without_header(cotations, market_name, game_id, need_extract=False):

    for cotation in cotations:
        
        try:
            price = decimal.Decimal(cotation['odds'])
        except decimal.InvalidOperation:
            price = 0
        
        if need_extract:
            total_goals = extract_goals_from_string(cotation['opp'])
            if total_goals:
                Cotation.objects.update_or_create(
                    name=get_translated_cotation_with_opp(cotation['opp']),
                    game=Game.objects.get(pk=game_id),
                    total_goals=total_goals,
                    market=Market.objects.get_or_create(
                        name=MARKET_TRANSLATIONS.get(market_name, market_name)
                    )[0],
                    defaults={
                        'price': price
                    }
                )
        else:
            Cotation.objects.update_or_create(
                name=get_translated_cotation_with_opp(cotation['opp']),
                game=Game.objects.get(pk=game_id),
                market=Market.objects.get_or_create(
                    name=MARKET_TRANSLATIONS.get(market_name, market_name)
                )[0],
                defaults={
                    'price': price
                }
            )

def cotation_without_header_standard(cotations, market_name, game_id):

    for cotation in cotations:

        try:
            price = decimal.Decimal(cotation['odds'])
        except decimal.InvalidOperation:
            price = 0

        Cotation.objects.update_or_create(
            name=get_translated_cotation_with_opp_standard(cotation['opp']),
            game=Game.objects.get(pk=game_id),
            market=Market.objects.get_or_create(
                name=MARKET_TRANSLATIONS.get(market_name, market_name)
            )[0],
            defaults={
                'price': price
            }
        )



