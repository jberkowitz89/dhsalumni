from espn_api.football import League

def get_settings(league: League) -> dict:
    '''
    docstring placeholder
    '''
    settings = league.settings
    attrs = vars(settings)
    attrs['year'] = league.year
    return vars(settings)

def get_draft(league: League) -> list:
    '''
    docstring placeholder
    '''
    draft_picks = list()
    draft = league.draft
    for pick in draft:
        pick_dict = vars(pick)
        pick_dict['team_id'] = pick.team.team_id
        pick_dict['team_name'] = pick.team.team_name
        pick_dict['year'] = league.year
        draft_picks.append(pick_dict)
    return draft_picks

def get_weekly_matchups(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_weeks = list()
    for i in range(len(league.settings.matchup_periods)):
        matchups_lst = league.scoreboard(week=i)
        for matchup in matchups_lst:
            matchup_info = vars(matchup)
            matchup_info['year'] = league.year
            matchup_info['home_team_id'] = matchup_info['home_team'].team_id
            matchup_info['home_team_name'] = matchup_info['home_team'].team_name
            matchup_info['away_team_id'] = matchup_info['away_team'].team_id
            matchup_info['away_team_name'] = matchup_info['away_team'].team_name
            all_weeks.append(matchup_info)
    return all_weeks

def get_teams(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_teams = list()
    for team in league.teams:
        team_info = vars(team)
        team_info['year'] = league.year
        all_teams.append(team_info)
    return all_teams

def get_players(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_players = list()
    for team in league.teams:
        for player in team.roster:
            player_info = vars(player)
            player_info['year'] = league.year
            player_info['team_id'] = team.team_id
            player_info['team_name'] = team.team_name
            all_players.append(player_info)
    return all_players

def get_box_scores(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_box_scores = list()
    if league.year < 2019:
        print('Box scores not available for this year')
        pass
    else:
        for i in range(len(league.settings.matchup_periods)):
            box_scores_lst = league.box_scores(week=i)
            for box_score in box_scores_lst:
                box_score_info = vars(box_score)
                box_score_info['year'] = league.year
                box_score_info['home_team_id'] = box_score_info['home_team'].team_id
                box_score_info['home_team_name'] = box_score_info['home_team'].team_name
                box_score_info['away_team_id'] = box_score_info['away_team'].team_id
                box_score_info['away_team_name'] = box_score_info['away_team'].team_name
                all_box_scores.append(box_score_info)
        return all_box_scores