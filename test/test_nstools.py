# local dependencies
from nstools import *

def test_get_nations_stats():
    headers = {'User-Agent':'UserAgent Example'}
    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=north_kalandia&q=census;scale=all;mode=score"
    stats = get_nation_stats(url, headers)
    print(stats)
    assert 'status code' not in stats

