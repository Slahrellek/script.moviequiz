import xbmcaddon

Q_WHAT_MOVIE_IS_THIS = 30400
Q_WHAT_MOVIE_IS_ACTOR_NOT_IN = 30401
Q_WHAT_YEAR_WAS_MOVIE_RELEASED = 30402
Q_WHAT_TAGLINE_BELONGS_TO_MOVIE = 30403
Q_WHO_DIRECTED_THIS_MOVIE = 30404
Q_WHAT_STUDIO_RELEASED_MOVIE = 30405
Q_WHAT_ACTOR_IS_THIS = 30406
Q_WHO_PLAYS_ROLE_IN_MOVIE = 30407
Q_WHO_VOICES_ROLE_IN_MOVIE = 30408
Q_WHAT_MOVIE_IS_THIS_QUOTE_FROM = 30409
Q_WHAT_MOVIE_IS_THE_NEWEST = 30410
Q_WHAT_MOVIE_IS_NOT_DIRECTED_BY = 30411
Q_WHAT_ACTOR_IS_IN_THESE_MOVIES = 30412
Q_WHAT_ACTOR_IS_IN_MOVIE_BESIDES_OTHER_ACTOR = 30413
Q_WHAT_MOVIE_HAS_THE_LONGEST_RUNTIME = 30414

Q_WHAT_TVSHOW_IS_THIS = 30450
Q_WHAT_SEASON_IS_THIS = 30451
Q_WHAT_EPISODE_IS_THIS = 30452
Q_WHEN_WAS_EPISODE_FIRST_AIRED = 30453
Q_WHEN_WAS_TVSHOW_FIRST_AIRED = 30454
Q_WHO_PLAYS_ROLE_IN_TVSHOW = 30455
Q_WHO_VOICES_ROLE_IN_TVSHOW = 30456

Q_SPECIALS = 30005
Q_SEASON_NO = 30006
Q_FIRST_AIRED_DATEFORMAT = 30007


G_QUESTION_X_OF_Y = 30000
G_GAME_OVER = 30003
G_YOU_SCORED = 30004

M_MOVIE_COLLECTION_TRIVIA = 30110
M_MOVIE_COUNT = 30111
M_ACTOR_COUNT = 30112
M_DIRECTOR_COUNT = 30113
M_STUDIO_COUNT = 30114
M_HOURS_OF_ENTERTAINMENT = 30115

M_TVSHOW_COLLECTION_TRIVIA = 30120
M_TVSHOW_COUNT = 30121
M_SEASON_COUNT = 30122
M_EPISODE_COUNT = 30123

S_DOWNLOADING_IMDB_DATA = 30520
S_RETRIEVED_X_OF_Y_MB = 30521

M_TRANSLATED_BY = 39999

def strings(id, replacements = None):
    string = xbmcaddon.Addon(id = 'script.moviequiz').getLocalizedString(id)
    if replacements is not None:
        return string % replacements
    else:
        return string