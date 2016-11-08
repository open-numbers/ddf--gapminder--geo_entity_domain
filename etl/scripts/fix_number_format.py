# -*- coding: utf-8 -*-

"""The number in latitude and longitude of country have at least one demical
in the country entity. But after manual edit of country file, CSV editor usually
drop the tailing zeros and make some number don't have decimal point.

We will fix this using this script.
"""

import pandas as pd
from ddf_utils.str import format_float_digits

def fix_number_format():
    fn = '../../ddf--entities--geo--country.csv'

    df = pd.read_csv(fn, dtype=str)
    df.longitude = df.longitude.map(lambda x: format_float_digits(x, 5, keep_decimal=True))
    df.latitude = df.latitude.map(lambda x: format_float_digits(x, 5, keep_decimal=True))

    df.to_csv(fn, index=False)


if __name__ == '__main__':
    fix_number_format()
