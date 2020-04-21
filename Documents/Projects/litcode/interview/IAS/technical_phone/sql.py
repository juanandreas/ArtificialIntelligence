"""
-- Assume you have a table name ADS_FEB with these columns
-- |ADS_DATE   |HOUR      | CAMPAIGN_ID           | ADS                    |
-- |2017-02-01 | 01       | 122                   | 20                     |
-- |2017-02-01 | 02       | 122                   | 90                     |
-- |2017-02-02 | 01       | 122                   | 10                     |
-- |2017-02-07 | 01       | 126                   | 10                     |
-- |2017-02-07 | 02       | 126                   | 10                     |
-- |2017-02-07 | 03       | 126                   | 10                     |
-- |2017-02-08 | 04       | 126                   | 20                     |
-- |2017-02-08 | 05       | 126                   | 20                     |
-- |2017-02-08 | 06       | 126                   | 20                     |
-- |2017-02-08 | 07       | 126                   | 60                     |


1. provide number of ads for each day for each campaign id? 
result should have ads_date, campaign id, total number ads

2. provide number of ads for each day for each campaign id, 
but exclude all campaigns that had less than 100 ads per day?
"""

import pandas as pd
import pandasql as ps

df = pd.DataFrame(
    [[1, 1, 122, 20],
    [1, 1, 122, 90],
    [2, 1, 122, 10],
    [7, 1, 126, 10],
    [7, 1, 126, 10],
    [7, 1, 126, 10],
    [8, 2, 126, 20],
    [8, 2, 126, 20],
    [8, 2, 126, 20],
    [8, 2, 126, 60]],
    columns=["ADS_DATE", "HOUR", "CAMPAIGN_ID", "ADS"]
)

query = """
SELECT ADS_DATE, CAMPAIGN_ID, SUM (ADS)
FROM df
GROUP BY CAMPAIGN_ID, ADS_DATE
having sum (ADS) >= 100
"""
print(ps.sqldf(query, locals()))

