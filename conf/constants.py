VERSION = 'v0.2'
RELEASE_DATE = '2022-Jan-09'
AUTHOR = 'Randy E. Oyarzabal'
GIT_REPO = 'https://github.com/randyoyarzabal/stocks'


def banner(tool):
    return '{} ver. {} ({})'.format(tool.split('.')[0].upper(), VERSION, RELEASE_DATE)
