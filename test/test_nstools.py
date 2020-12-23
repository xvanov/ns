# local dependencies
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from nstools import *

def test_get_nations_stats():
    headers = {'User-Agent':'UserAgent Example'}
    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score"
    stats = get_nation_stats(url, headers)
    print(stats)
    assert 'status code' not in stats

