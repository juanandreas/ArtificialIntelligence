import pandas as pd
import pandasql as ps


if __name__ == '__main__':
    df = pd.DataFrame(
        [[1, 200000],
        [1, 400000],
        [2, 300000],
        [2, 200000]],
    columns=['id', 'salary'])

    q1 = """SELECT id FROM df """

    print(ps.sqldf(q1, locals()))