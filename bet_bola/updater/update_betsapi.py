import requests
import datetime
import math
import time
from core.models import Location, League, Sport, Market, Game, Cotation
from ticket.models import Ticket
from django.db.models import Q , Count
from .countries import COUNTRIES
from .ccs import COUNTRIES
from .sports import SPORTS
from .get_markets import cotation_with_header, cotation_without_header


TOKEN="20445-s1B9Vv6E9VSLU1"

def get_upcoming_events():
    today = datetime.datetime.today().strftime('%Y%m%d')
    #tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y%m%d')
    page = 1
    
    url_base = "https://api.betsapi.com/v1/bet365/upcoming?sport_id=1&token=" + TOKEN + "&day=" + today + "&page="
    url_page = "https://api.betsapi.com/v1/bet365/upcoming?sport_id=1&token=" + TOKEN + "&day=" + today + "&page=" + str(page)

    request = requests.get(url_page)
    data = request.json()
    process_upcoming_events(data)

    if request.status_code == 200 and data['success'] == 1:
        games_total = data['pager']['total']
        per_page = data['pager']['per_page']
        num_pages = math.ceil(int(games_total) / int(per_page))
    
    while page <= num_pages:
        request = requests.get(url_base + str(page))
        process_upcoming_events(request.json())
        page += 1

def get_cc_from_result(game_id):
    print("cc_from_result " + game_id)
    url = "https://api.betsapi.com/v1/bet365/result?token=20445-s1B9Vv6E9VSLU1&event_id=" + game_id
    request = requests.get(url)
    data = request.json()
    if request.status_code == 200 and data['success'] == 1:
        league = data['results'][0].get('league', None)
        if league:
            return league.get('cc', None)
    else:
        print("Get CC from result Failed.")


def get_game_name(game):
    return game['home']['name'] + ' x ' + game['away']['name']

def get_start_date_from_timestamp(game):
    return datetime.datetime.fromtimestamp(int(game['time']))


def get_league_and_create_location(game):
    league, created = League.objects.get_or_create(
        pk=int(game['league']['id']),
        defaults={
            'name': game['league']['name']
        }
    )

    if league.location == None:
        cc = get_cc_from_result(game['id'])
        country_translated = COUNTRIES.get(cc, None)

        if cc == None or country_translated == None:
            league.location = Location.objects.get_or_create(
                cc="inter",
                defaults={
                    'name': COUNTRIES.get('inter', "Internacional")
                }
            )[0]
        else:
            league.location = Location.objects.get_or_create(
                cc=cc,
                defaults={
                    'name': country_translated
                }
            )[0]
        
        league.save()
        return league

def get_sport(game):
    sport = Sport.objects.get_or_create(
        pk=int(game['sport_id']),
        defaults={
            'name': SPORTS.get(game['sport_id'], "Futebol")
        }
    )[0]
    return sport


def process_upcoming_events(data):
    if data['success'] == 1:
        for game in data['results']:
            print(game['id'])
            game_obj, created = Game.objects.get_or_create(
                pk=game['id'],
                defaults={
                    'name': get_game_name(game),
                    'start_date': get_start_date_from_timestamp(game),
                    'league': get_league_and_create_location(game),
                    'sport': get_sport(game),
                    'game_status': int(game['time_status'])
                }
            )

            get_cotations(game['id'])



def get_cotations(game_id):
    print("getting cotations for" + game_id)
    url = "https://api.betsapi.com/v1/bet365/start_sp?token=20445-s1B9Vv6E9VSLU1&FI=" + str(game_id)
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['success'] == 1:
        #print(data)
        if data.get('results', None) and data['results'][0].get('goals', None):
            get_goals_cotations(data['results'][0]['goals'], game_id)



def get_goals_cotations(goals_cotations, game_id):
    if goals_cotations.get('sp', None):
        if goals_cotations['sp'].get('goals_over_under', None):
            cotation_with_header(goals_cotations['sp']['goals_over_under'], 'goals_over_under', game_id)
        if goals_cotations['sp'].get('alternative_total_goals', None):
            cotation_with_header(goals_cotations['sp']['alternative_total_goals'], 'alternative_total_goals', game_id)
        if goals_cotations['sp'].get('2nd_half_goals', None):
            cotation_with_header(goals_cotations['sp']['2nd_half_goals'], '2nd_half_goals', game_id)
        if goals_cotations['sp'].get('first_half_goals', None):
            cotation_with_header(goals_cotations['sp']['first_half_goals'], 'first_half_goals', game_id)
        
        if goals_cotations['sp'].get('result_total_goals', None):
            cotation_without_header(goals_cotations['sp']['result_total_goals'], 'result_total_goals', game_id)
        if goals_cotations['sp'].get('total_goals_both_teams_to_score', None):
            cotation_without_header(goals_cotations['sp']['total_goals_both_teams_to_score'], 'total_goals_both_teams_to_score', game_id)
        if goals_cotations['sp'].get('exact_total_goals', None):
            cotation_without_header(goals_cotations['sp']['exact_total_goals'], 'exact_total_goals', game_id)
        if goals_cotations['sp'].get('number_of_goals_in_match', None):
            cotation_without_header(goals_cotations['sp']['number_of_goals_in_match'], 'number_of_goals_in_match', game_id)
        if goals_cotations['sp'].get('both_teams_to_score', None):
            cotation_without_header(goals_cotations['sp']['both_teams_to_score'], 'both_teams_to_score', game_id)
        if goals_cotations['sp'].get('teams_to_score', None):
            cotation_without_header(goals_cotations['sp']['teams_to_score'], 'teams_to_score', game_id)
        if goals_cotations['sp'].get('both_teams_to_score_in_1st_half', None):
            cotation_without_header(goals_cotations['sp']['both_teams_to_score_in_1st_half'], 'both_teams_to_score_in_1st_half', game_id)
        if goals_cotations['sp'].get('both_teams_to_score_in_2nd_half', None):
            cotation_without_header(goals_cotations['sp']['both_teams_to_score_in_2nd_half'], 'both_teams_to_score_in_2nd_half', game_id)
        if goals_cotations['sp'].get('both_teams_to_score_1st_half_2nd_half', None):
            cotation_without_header(goals_cotations['sp']['both_teams_to_score_1st_half_2nd_half'], 'both_teams_to_score_1st_half_2nd_half', game_id)
        if goals_cotations['sp'].get('exact_1st_half_goals', None):
            cotation_without_header(goals_cotations['sp']['exact_1st_half_goals'], 'exact_1st_half_goals', game_id)
        if goals_cotations['sp'].get('exact_2nd_half_goals', None):
            cotation_without_header(goals_cotations['sp']['exact_2nd_half_goals'], 'exact_2nd_half_goals', game_id)
        if goals_cotations['sp'].get('half_with_most_goals', None):
            cotation_without_header(goals_cotations['sp']['half_with_most_goals'], 'half_with_most_goals', game_id)
        if goals_cotations['sp'].get('home_team_highest_scoring_half', None):
            cotation_without_header(goals_cotations['sp']['home_team_highest_scoring_half'], 'home_team_highest_scoring_half', game_id)
        if goals_cotations['sp'].get('away_team_highest_scoring_half', None):
            cotation_without_header(goals_cotations['sp']['away_team_highest_scoring_half'], 'away_team_highest_scoring_half', game_id)
        if goals_cotations['sp'].get('home_team_exact_goals', None):
            cotation_without_header(goals_cotations['sp']['home_team_exact_goals'], 'home_team_exact_goals', game_id)
        if goals_cotations['sp'].get('away_team_exact_goals', None):
            cotation_without_header(goals_cotations['sp']['away_team_exact_goals'], 'away_team_exact_goals', game_id)
        if goals_cotations['sp'].get('goals_odd_even', None):
            cotation_without_header(goals_cotations['sp']['goals_odd_even'], 'goals_odd_even', game_id)
        if goals_cotations['sp'].get('home_team_odd_even_goals', None):
            cotation_without_header(goals_cotations['sp']['home_team_odd_even_goals'], 'home_team_odd_even_goals', game_id)
        if goals_cotations['sp'].get('away_team_odd_even_goals', None):
            cotation_without_header(goals_cotations['sp']['away_team_odd_even_goals'], 'away_team_odd_even_goals', game_id)
        if goals_cotations['sp'].get('1st_half_goals_odd_even', None):
            cotation_without_header(goals_cotations['sp']['1st_half_goals_odd_even'], '1st_half_goals_odd_even', game_id)
        


