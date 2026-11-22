# Data provenance and known transformation

The source file [`balance.txt`](balance.txt) has **400 observations** and **11 columns**. It is a whitespace-delimited export with quoted categorical fields. It appears to be a modified version of the simulated **Credit** dataset used in *An Introduction to Statistical Learning*.

I compared it, row by row, with the [official ISLP project CSV](https://github.com/intro-stat-learning/ISLP/blob/main/ISLP/data/Credit.csv). After stripping padding around string values and allowing insignificant floating-point serialization differences, **all 400 rows match on every one of the other ten variables**: `Income`, `Limit`, `Rating`, `Cards`, `Age`, `Education`, `Gender`, `Student`, `Married` and `Ethnicity`.

**Every one of the 400 `Balance` values differs from the original source.** For example:

| 1-based row | Original ISLP `Balance` | Project `Balance` |
|:--|--:|--:|
| 1 | 333 | 12.2407984760474 |
| 2 | 903 | 23.2833339223376 |
| 3 | 580 | 22.5304088790893 |
| 4 | 964 | 27.652810710665 |
| 5 | 331 | 16.8939784904888 |

The project does not document which transformation or replacement generated these `Balance` values. In particular, the original source defines balance in US dollars, **but that definition cannot be carried over to the altered column without evidence of the transformation**. Therefore, project analysis reports the provided values in *unidentified balance units*, not as verified US-dollar balances.

The original ISLR/ISLP data are described as a **simulated dataset**, so these should not be presented as observational results from a representative population of actual credit-card customers.

## Reproduction of comparison

1. Download the official ISLP `Credit.csv` from the link above.
2. Read `balance.txt` with `pd.read_csv('balance.txt', sep=r'\s+')`.
3. Load the original `Credit.csv` using `pd.read_csv('Credit.csv')`.
4. Compare the 400 observations in the same order, with numeric tolerance for floating-point representation and stripped string categories; exclude `ID` (not present in the project file).
5. Compare `Balance` separately and treat the transformations as **unknown**.

Reference documentation: [ISLR Credit Card Balance Data](https://rdrr.io/cran/ISLR/man/Credit.html) and [ISLP Credit Card Balance Data](https://islp.readthedocs.io/en/latest/datasets/Credit.html).

The comparisons in this file were conducted for the research-portfolio audit on 22 November 2026; they do not establish who made the alteration or why.