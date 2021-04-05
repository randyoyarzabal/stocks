VERSION = 'v0.1'
RELEASE_DATE = '2021-Apr-04'
AUTHOR = 'Randy E. Oyarzabal'
GIT_REPO = 'https://github.com/randyoyarzabal/stocks'


def banner(tool):
    return '{} ver. {} ({})'.format(tool.split('.')[0].upper(), VERSION, RELEASE_DATE)
