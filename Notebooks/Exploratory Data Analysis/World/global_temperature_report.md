Toggle navigation

[Pandas Profiling Report](#top)

-   [Overview](#overview)
-   [Variables](#variables)
-   [Interactions](#interactions)
-   [Correlations](#correlations)
-   [Missing values](#missing)
-   [Sample](#sample)

Overview {.page-header}
========

-   [Overview](#overview-dataset_overview)
-   [Warnings 13](#overview-warnings)
-   [Reproduction](#overview-reproduction)

Dataset statistics

Number of variables

9

Number of observations

3192

Missing cells

7224

Missing cells (%)

25.1%

Duplicate rows

0

Duplicate rows (%)

0.0%

Total size in memory

408.5 KiB

Average record size in memory

131.0 B

Variable types

NUM

8

CAT

1

Warnings

[`LandMaxTemperature`](#pp_var_7050631149182443474) is highly correlated
with `LandAverageTemperature` and 2 other fields

High correlation

[`LandAverageTemperature`](#pp_var_4767428739462326834) is highly
correlated with `LandMaxTemperature` and 2 other fields

High correlation

[`LandMinTemperature`](#pp_var_-6696416535259061525) is highly
correlated with `LandAverageTemperature` and 2 other fields

High correlation

[`LandAndOceanAverageTemperature`](#pp_var_-8221517211577610154) is
highly correlated with `LandAverageTemperature` and 2 other fields

High correlation

[`LandAndOceanAverageTemperatureUncertainty`](#pp_var_8989519429109620280)
is highly correlated with `LandAverageTemperatureUncertainty`

High correlation

[`LandAverageTemperatureUncertainty`](#pp_var_7578052883231535465) is
highly correlated with `LandAndOceanAverageTemperatureUncertainty`

High correlation

[`LandMaxTemperature`](#pp_var_7050631149182443474) has 1200 (37.6%)
missing values

Missing

[`LandMaxTemperatureUncertainty`](#pp_var_-6201146505617089049) has 1200
(37.6%) missing values

Missing

[`LandMinTemperature`](#pp_var_-6696416535259061525) has 1200 (37.6%)
missing values

Missing

[`LandMinTemperatureUncertainty`](#pp_var_-7957790986284982199) has 1200
(37.6%) missing values

Missing

[`LandAndOceanAverageTemperature`](#pp_var_-8221517211577610154) has
1200 (37.6%) missing values

Missing

[`LandAndOceanAverageTemperatureUncertainty`](#pp_var_8989519429109620280)
has 1200 (37.6%) missing values

Missing

[`dt`](#pp_var_-6892863291275787649) has unique values

Unique

Reproduction

Analysis started

2020-10-27 20:12:39.893028

Analysis finished

2020-10-27 20:12:56.816525

Duration

16.92 seconds

Software version

[pandas-profiling
v2.9.0](https://github.com/pandas-profiling/pandas-profiling)

Download configuration

[config.yaml](data:text/plain;charset=utf-8,progress_bar%3A%20no%0Atitle%3A%20Pandas%20Profiling%20Report%0Ahtml%3A%0A%20%20%20%20style%3A%0A%20%20%20%20%20%20%20%20primary_color%3A%20%27%232c3e50%27%0A%20%20%20%20%20%20%20%20theme%3A%20flatly%0A%20%20%20%20%20%20%20%20logo%3A%20%27%27%0A%20%20%20%20%20%20%20%20full_width%3A%20no%0A%20%20%20%20minify_html%3A%20yes%0A%20%20%20%20use_local_assets%3A%20yes%0A%20%20%20%20inline%3A%20yes%0A%20%20%20%20navbar_show%3A%20yes%0A%20%20%20%20file_name%3A%20None%0Amemory_deep%3A%20yes%0An_freq_table_max%3A%2025%0An_extreme_obs%3A%2010%0An_obs_unique%3A%2010%0Avars%3A%0A%20%20%20%20image%3A%0A%20%20%20%20%20%20%20%20active%3A%20yes%0A%20%20%20%20%20%20%20%20exif%3A%20yes%0A%20%20%20%20%20%20%20%20hash%3A%20yes%0A%20%20%20%20file%3A%0A%20%20%20%20%20%20%20%20active%3A%20yes%0A%20%20%20%20cat%3A%0A%20%20%20%20%20%20%20%20unicode%3A%20yes%0A%20%20%20%20%20%20%20%20length%3A%20yes%0A%20%20%20%20%20%20%20%20cardinality_threshold%3A%2050%0A%20%20%20%20%20%20%20%20n_obs%3A%205%0A%20%20%20%20%20%20%20%20chi_squared_threshold%3A%200.999%0A%20%20%20%20%20%20%20%20coerce_str_to_date%3A%20no%0A%20%20%20%20%20%20%20%20redact%3A%20no%0A%20%20%20%20num%3A%0A%20%20%20%20%20%20%20%20quantiles%3A%0A%20%20%20%20%20%20%20%20-%200.05%0A%20%20%20%20%20%20%20%20-%200.25%0A%20%20%20%20%20%20%20%20-%200.5%0A%20%20%20%20%20%20%20%20-%200.75%0A%20%20%20%20%20%20%20%20-%200.95%0A%20%20%20%20%20%20%20%20skewness_threshold%3A%2020%0A%20%20%20%20%20%20%20%20low_categorical_threshold%3A%205%0A%20%20%20%20%20%20%20%20chi_squared_threshold%3A%200.999%0A%20%20%20%20bool%3A%0A%20%20%20%20%20%20%20%20n_obs%3A%203%0Adataset%3A%0A%20%20%20%20description%3A%20%27%27%0A%20%20%20%20creator%3A%20%27%27%0A%20%20%20%20author%3A%20%27%27%0A%20%20%20%20copyright_holder%3A%20%27%27%0A%20%20%20%20copyright_year%3A%20%27%27%0A%20%20%20%20url%3A%20%27%27%0Avariables%3A%0A%20%20%20%20descriptions%3A%20%7B%7D%0Ashow_variable_description%3A%20yes%0Apool_size%3A%200%0Asort%3A%20None%0Amissing_diagrams%3A%0A%20%20%20%20bar%3A%20yes%0A%20%20%20%20matrix%3A%20yes%0A%20%20%20%20heatmap%3A%20yes%0A%20%20%20%20dendrogram%3A%20yes%0Acorrelations%3A%0A%20%20%20%20pearson%3A%0A%20%20%20%20%20%20%20%20calculate%3A%20yes%0A%20%20%20%20%20%20%20%20warn_high_correlations%3A%20yes%0A%20%20%20%20%20%20%20%20threshold%3A%200.9%0A%20%20%20%20spearman%3A%0A%20%20%20%20%20%20%20%20calculate%3A%20yes%0A%20%20%20%20%20%20%20%20warn_high_correlations%3A%20no%0A%20%20%20%20kendall%3A%0A%20%20%20%20%20%20%20%20calculate%3A%20yes%0A%20%20%20%20%20%20%20%20warn_high_correlations%3A%20no%0A%20%20%20%20phi_k%3A%0A%20%20%20%20%20%20%20%20calculate%3A%20yes%0A%20%20%20%20%20%20%20%20warn_high_correlations%3A%20no%0A%20%20%20%20cramers%3A%0A%20%20%20%20%20%20%20%20calculate%3A%20yes%0A%20%20%20%20%20%20%20%20warn_high_correlations%3A%20yes%0A%20%20%20%20%20%20%20%20threshold%3A%200.9%0A%20%20%20%20recoded%3A%0A%20%20%20%20%20%20%20%20calculate%3A%20no%0A%20%20%20%20%20%20%20%20warn_high_correlations%3A%20no%0A%20%20%20%20%20%20%20%20threshold%3A%200.0%0Ainteractions%3A%0A%20%20%20%20targets%3A%20%5B%5D%0A%20%20%20%20continuous%3A%20yes%0Acategorical_maximum_correlation_distinct%3A%20100%0Aplot%3A%0A%20%20%20%20image_format%3A%20svg%0A%20%20%20%20dpi%3A%20800%0A%20%20%20%20scatter_threshold%3A%201000%0A%20%20%20%20correlation%3A%0A%20%20%20%20%20%20%20%20cmap%3A%20RdBu%0A%20%20%20%20%20%20%20%20bad%3A%20%27%23000000%27%0A%20%20%20%20missing%3A%0A%20%20%20%20%20%20%20%20cmap%3A%20RdBu%0A%20%20%20%20%20%20%20%20force_labels%3A%20yes%0A%20%20%20%20pie%3A%0A%20%20%20%20%20%20%20%20max_unique%3A%2010%0A%20%20%20%20histogram%3A%0A%20%20%20%20%20%20%20%20x_axis_labels%3A%20yes%0A%20%20%20%20%20%20%20%20bins%3A%2050%0A%20%20%20%20%20%20%20%20max_bins%3A%20250%0Aduplicates%3A%0A%20%20%20%20head%3A%2010%0Asamples%3A%0A%20%20%20%20head%3A%2010%0A%20%20%20%20tail%3A%2010%0Areject_variables%3A%20yes%0Anotebook%3A%0A%20%20%20%20iframe%3A%0A%20%20%20%20%20%20%20%20height%3A%20800px%0A%20%20%20%20%20%20%20%20width%3A%20100%25%0A%20%20%20%20%20%20%20%20attribute%3A%20srcdoc%0A)

Variables {.page-header}
=========

[dt](#pp_var_-6892863291275787649)\
Categorical

`UNIQUE`\

Distinct

3192

Distinct (%)

100.0%

Missing

0

Missing (%)

0.0%

Memory size

25.1 KiB

1780-07-01

 

1

1995-09-01

 

1

1839-08-01

 

1

1884-09-01

 

1

1892-04-01

 

1

Other values (3187)

3187 

Toggle details

-   [Frequencies](#-6892863291275787649bottom--6892863291275787649frequencies)
-   [Length](#-6892863291275787649bottom--6892863291275787649tbl)
-   [Unicode](#-6892863291275787649bottom--6892863291275787649unicode)

-   [Common
    Values](#-6892863291275787649frequencies--6892863291275787649common_values)
-   [Overview](#-6892863291275787649frequencies--6892863291275787649tbl)

Value

Count

Frequency (%)

 

1780-07-01

1

\< 0.1%

 

1995-09-01

1

\< 0.1%

 

1839-08-01

1

\< 0.1%

 

1884-09-01

1

\< 0.1%

 

1892-04-01

1

\< 0.1%

 

1891-06-01

1

\< 0.1%

 

1881-02-01

1

\< 0.1%

 

1750-11-01

1

\< 0.1%

 

1992-02-01

1

\< 0.1%

 

1810-07-01

1

\< 0.1%

 

1752-08-01

1

\< 0.1%

 

1754-07-01

1

\< 0.1%

 

1947-06-01

1

\< 0.1%

 

1865-08-01

1

\< 0.1%

 

1879-08-01

1

\< 0.1%

 

1761-07-01

1

\< 0.1%

 

1818-03-01

1

\< 0.1%

 

1801-07-01

1

\< 0.1%

 

1970-08-01

1

\< 0.1%

 

1945-01-01

1

\< 0.1%

 

1814-04-01

1

\< 0.1%

 

1921-05-01

1

\< 0.1%

 

1949-06-01

1

\< 0.1%

 

1822-01-01

1

\< 0.1%

 

1867-12-01

1

\< 0.1%

 

Other values (3167)

3167

99.2%

 

2020-10-27T15:12:56.898306image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Frequencies of value counts

Unique

Unique

3192 ?

Unique (%)

100.0%

2020-10-27T15:12:57.019948image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Histogram of lengths of the category

Length

Max length

10

Median length

10

Mean length

10

Min length

10

-   [Overview](#-6892863291275787649unicode--6892863291275787649character_overview)
-   [Characters](#-6892863291275787649unicode--6892863291275787649characters)
-   [Categories](#-6892863291275787649unicode--6892863291275787649categories)
-   [Scripts](#-6892863291275787649unicode--6892863291275787649scripts)
-   [Blocks](#-6892863291275787649unicode--6892863291275787649blocks)

Overview of Unicode Properties

Unique unicode characters

11

Unique unicode categories

2
[?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)")

Unique unicode scripts

1
[?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)")

Unique unicode blocks

1
[?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)")

The Unicode Standard assigns character properties to each code point,
which can be used to analyse textual variables.

#### Most occurring characters

Value

Count

Frequency (%)

 

1

8158

25.6%

 

0

6728

21.1%

 

-

6384

20.0%

 

8

2138

6.7%

 

9

2138

6.7%

 

7

1538

4.8%

 

2

1288

4.0%

 

5

950

3.0%

 

6

938

2.9%

 

3

830

2.6%

 

4

830

2.6%

 

#### Most occurring categories

Value

Count

Frequency (%)

 

Decimal Number

25536

80.0%

 

Dash Punctuation

6384

20.0%

 

#### Most frequent Decimal Number characters

Value

Count

Frequency (%)

 

1

8158

31.9%

 

0

6728

26.3%

 

8

2138

8.4%

 

9

2138

8.4%

 

7

1538

6.0%

 

2

1288

5.0%

 

5

950

3.7%

 

6

938

3.7%

 

3

830

3.3%

 

4

830

3.3%

 

#### Most frequent Dash Punctuation characters

Value

Count

Frequency (%)

 

-

6384

100.0%

 

#### Most occurring scripts

Value

Count

Frequency (%)

 

Common

31920

100.0%

 

#### Most frequent Common characters

Value

Count

Frequency (%)

 

1

8158

25.6%

 

0

6728

21.1%

 

-

6384

20.0%

 

8

2138

6.7%

 

9

2138

6.7%

 

7

1538

4.8%

 

2

1288

4.0%

 

5

950

3.0%

 

6

938

2.9%

 

3

830

2.6%

 

4

830

2.6%

 

#### Most occurring blocks

Value

Count

Frequency (%)

 

ASCII

31920

100.0%

 

#### Most frequent ASCII characters

Value

Count

Frequency (%)

 

1

8158

25.6%

 

0

6728

21.1%

 

-

6384

20.0%

 

8

2138

6.7%

 

9

2138

6.7%

 

7

1538

4.8%

 

2

1288

4.0%

 

5

950

3.0%

 

6

938

2.9%

 

3

830

2.6%

 

4

830

2.6%

 

[LandAverageTemperature](#pp_var_4767428739462326834)\
Real number (ℝ)

`HIGH CORRELATION`\

Distinct

2850

Distinct (%)

89.6%

Missing

12

Missing (%)

0.4%

Infinite

0

Infinite (%)

0.0%

Mean

8.374731132

Minimum

-2.08

Maximum

19.021

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:57.148609image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#4767428739462326834bottom-4767428739462326834statistics)
-   [Histogram](#4767428739462326834bottom-4767428739462326834histogram)
-   [Common
    values](#4767428739462326834bottom-4767428739462326834common_values)
-   [Extreme
    values](#4767428739462326834bottom-4767428739462326834extreme_values)

Quantile statistics

Minimum

-2.08

5-th percentile

1.97075

Q1

4.312

median

8.6105

Q3

12.54825

95-th percentile

14.395

Maximum

19.021

Range

21.101

Interquartile range (IQR)

8.23625

Descriptive statistics

Standard deviation

4.381309771

Coefficient of variation (CV)

0.5231582604

Kurtosis

-1.342072459

Mean

8.374731132

Median Absolute Deviation (MAD)

4.1565

Skewness

-0.08142566548

Sum

26631.645

Variance

19.19587531

Monotocity

Not monotonic

2020-10-27T15:12:57.304188image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

13.293

4

0.1%

 

13.765

4

0.1%

 

2.737

3

0.1%

 

3.092

3

0.1%

 

14.197

3

0.1%

 

13.827

3

0.1%

 

13.459

3

0.1%

 

12.247

3

0.1%

 

13.744

3

0.1%

 

13.484

3

0.1%

 

13.821

3

0.1%

 

14.319

3

0.1%

 

2.039

3

0.1%

 

3.213

3

0.1%

 

14.742

3

0.1%

 

13.953

3

0.1%

 

13.412

3

0.1%

 

3.785

3

0.1%

 

3.099

3

0.1%

 

13.58

3

0.1%

 

5.272

3

0.1%

 

14.242

3

0.1%

 

8.722

3

0.1%

 

3.92

3

0.1%

 

11.097

3

0.1%

 

Other values (2825)

3103

97.2%

 

(Missing)

12

0.4%

 

-   [Minimum 5
    values](#4767428739462326834extreme_values-4767428739462326834firstn)
-   [Maximum 5
    values](#4767428739462326834extreme_values-4767428739462326834lastn)

Value

Count

Frequency (%)

 

-2.08

1

\< 0.1%

 

-1.503

1

\< 0.1%

 

-1.431

1

\< 0.1%

 

-1.385

1

\< 0.1%

 

-1.249

1

\< 0.1%

 

-0.978

1

\< 0.1%

 

-0.837

1

\< 0.1%

 

-0.811

1

\< 0.1%

 

-0.806

1

\< 0.1%

 

-0.793

1

\< 0.1%

 

Value

Count

Frequency (%)

 

19.021

1

\< 0.1%

 

17.91

1

\< 0.1%

 

17.61

1

\< 0.1%

 

17.115

1

\< 0.1%

 

16.821

1

\< 0.1%

 

16.521

1

\< 0.1%

 

16.468

1

\< 0.1%

 

16.391

1

\< 0.1%

 

16.183

1

\< 0.1%

 

16.025

1

\< 0.1%

 

[LandAverageTemperatureUncertainty](#pp_var_7578052883231535465)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\

Distinct

1594

Distinct (%)

50.1%

Missing

12

Missing (%)

0.4%

Infinite

0

Infinite (%)

0.0%

Mean

0.9384679245

Minimum

0.034

Maximum

7.88

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:57.446810image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#7578052883231535465bottom-7578052883231535465statistics)
-   [Histogram](#7578052883231535465bottom-7578052883231535465histogram)
-   [Common
    values](#7578052883231535465bottom-7578052883231535465common_values)
-   [Extreme
    values](#7578052883231535465bottom-7578052883231535465extreme_values)

Quantile statistics

Minimum

0.034

5-th percentile

0.066

Q1

0.18675

median

0.392

Q3

1.41925

95-th percentile

3.2351

Maximum

7.88

Range

7.846

Interquartile range (IQR)

1.2325

Descriptive statistics

Standard deviation

1.096439795

Coefficient of variation (CV)

1.168329536

Kurtosis

3.536050467

Mean

0.9384679245

Median Absolute Deviation (MAD)

0.31

Skewness

1.780596521

Sum

2984.328

Variance

1.202180224

Monotocity

Not monotonic

2020-10-27T15:12:57.596412image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

0.087

20

0.6%

 

0.064

19

0.6%

 

0.077

16

0.5%

 

0.078

16

0.5%

 

0.086

14

0.4%

 

0.068

14

0.4%

 

0.082

14

0.4%

 

0.085

13

0.4%

 

0.084

13

0.4%

 

0.07

12

0.4%

 

0.083

12

0.4%

 

0.106

12

0.4%

 

0.09

11

0.3%

 

0.104

11

0.3%

 

0.276

11

0.3%

 

0.062

11

0.3%

 

0.091

11

0.3%

 

0.079

11

0.3%

 

0.099

11

0.3%

 

0.08

11

0.3%

 

0.059

11

0.3%

 

0.089

11

0.3%

 

0.072

10

0.3%

 

0.066

10

0.3%

 

0.096

10

0.3%

 

Other values (1569)

2865

89.8%

 

(Missing)

12

0.4%

 

-   [Minimum 5
    values](#7578052883231535465extreme_values-7578052883231535465firstn)
-   [Maximum 5
    values](#7578052883231535465extreme_values-7578052883231535465lastn)

Value

Count

Frequency (%)

 

0.034

1

\< 0.1%

 

0.035

2

0.1%

 

0.036

1

\< 0.1%

 

0.039

1

\< 0.1%

 

0.04

1

\< 0.1%

 

0.041

3

0.1%

 

0.042

2

0.1%

 

0.044

2

0.1%

 

0.045

3

0.1%

 

0.046

3

0.1%

 

Value

Count

Frequency (%)

 

7.88

1

\< 0.1%

 

7.492

1

\< 0.1%

 

7.349

1

\< 0.1%

 

6.415

1

\< 0.1%

 

6.341

1

\< 0.1%

 

5.966

1

\< 0.1%

 

5.963

1

\< 0.1%

 

5.857

1

\< 0.1%

 

5.827

1

\< 0.1%

 

5.656

1

\< 0.1%

 

[LandMaxTemperature](#pp_var_7050631149182443474)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`MISSING`\

Distinct

1821

Distinct (%)

91.4%

Missing

1200

Missing (%)

37.6%

Infinite

0

Infinite (%)

0.0%

Mean

14.3506009

Minimum

5.9

Maximum

21.32

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:57.745043image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#7050631149182443474bottom-7050631149182443474statistics)
-   [Histogram](#7050631149182443474bottom-7050631149182443474histogram)
-   [Common
    values](#7050631149182443474bottom-7050631149182443474common_values)
-   [Extreme
    values](#7050631149182443474bottom-7050631149182443474extreme_values)

Quantile statistics

Minimum

5.9

5-th percentile

8.118

Q1

10.212

median

14.76

Q3

18.4515

95-th percentile

20.1625

Maximum

21.32

Range

15.42

Interquartile range (IQR)

8.2395

Descriptive statistics

Standard deviation

4.309578966

Coefficient of variation (CV)

0.3003065164

Kurtosis

-1.456171165

Mean

14.3506009

Median Absolute Deviation (MAD)

4.137

Skewness

-0.09693800875

Sum

28586.397

Variance

18.57247086

Monotocity

Not monotonic

2020-10-27T15:12:57.876689image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

17.196

3

0.1%

 

19.85

3

0.1%

 

8.555

3

0.1%

 

19.36

3

0.1%

 

17.289

3

0.1%

 

20.037

3

0.1%

 

19.628

3

0.1%

 

10.781

3

0.1%

 

19.753

3

0.1%

 

17.713

3

0.1%

 

11.411

3

0.1%

 

11.24

2

0.1%

 

11.384

2

0.1%

 

19.163

2

0.1%

 

18.078

2

0.1%

 

19.022

2

0.1%

 

10.469

2

0.1%

 

11.628

2

0.1%

 

19.82

2

0.1%

 

19.987

2

0.1%

 

17.394

2

0.1%

 

8.544

2

0.1%

 

19.275

2

0.1%

 

19.396

2

0.1%

 

17.769

2

0.1%

 

Other values (1796)

1931

60.5%

 

(Missing)

1200

37.6%

 

-   [Minimum 5
    values](#7050631149182443474extreme_values-7050631149182443474firstn)
-   [Maximum 5
    values](#7050631149182443474extreme_values-7050631149182443474lastn)

Value

Count

Frequency (%)

 

5.9

1

\< 0.1%

 

6.421

1

\< 0.1%

 

6.436

1

\< 0.1%

 

6.642

1

\< 0.1%

 

6.679

1

\< 0.1%

 

6.686

1

\< 0.1%

 

6.864

1

\< 0.1%

 

6.961

1

\< 0.1%

 

7.023

1

\< 0.1%

 

7.064

1

\< 0.1%

 

Value

Count

Frequency (%)

 

21.32

1

\< 0.1%

 

21.199

1

\< 0.1%

 

21.108

1

\< 0.1%

 

21.085

1

\< 0.1%

 

21.006

2

0.1%

 

20.972

1

\< 0.1%

 

20.97

1

\< 0.1%

 

20.923

1

\< 0.1%

 

20.922

1

\< 0.1%

 

20.905

1

\< 0.1%

 

[LandMaxTemperatureUncertainty](#pp_var_-6201146505617089049)\
Real number (ℝ~≥0~)

`MISSING`\

Distinct

841

Distinct (%)

42.2%

Missing

1200

Missing (%)

37.6%

Infinite

0

Infinite (%)

0.0%

Mean

0.4797816265

Minimum

0.044

Maximum

4.373

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:58.033239image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#-6201146505617089049bottom--6201146505617089049statistics)
-   [Histogram](#-6201146505617089049bottom--6201146505617089049histogram)
-   [Common
    values](#-6201146505617089049bottom--6201146505617089049common_values)
-   [Extreme
    values](#-6201146505617089049bottom--6201146505617089049extreme_values)

Quantile statistics

Minimum

0.044

5-th percentile

0.083

Q1

0.142

median

0.252

Q3

0.539

95-th percentile

1.86245

Maximum

4.373

Range

4.329

Interquartile range (IQR)

0.397

Descriptive statistics

Standard deviation

0.5832029575

Coefficient of variation (CV)

1.215559174

Kurtosis

7.55348287

Mean

0.4797816265

Median Absolute Deviation (MAD)

0.136

Skewness

2.565863891

Sum

955.725

Variance

0.3401256896

Monotocity

Not monotonic

2020-10-27T15:12:58.164915image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

0.093

14

0.4%

 

0.105

12

0.4%

 

0.098

11

0.3%

 

0.13

11

0.3%

 

0.106

11

0.3%

 

0.094

11

0.3%

 

0.179

10

0.3%

 

0.099

10

0.3%

 

0.16

10

0.3%

 

0.09

9

0.3%

 

0.108

9

0.3%

 

0.117

9

0.3%

 

0.088

9

0.3%

 

0.122

9

0.3%

 

0.116

9

0.3%

 

0.085

9

0.3%

 

0.165

9

0.3%

 

0.219

9

0.3%

 

0.079

9

0.3%

 

0.212

9

0.3%

 

0.28

8

0.3%

 

0.111

8

0.3%

 

0.298

8

0.3%

 

0.092

8

0.3%

 

0.084

8

0.3%

 

Other values (816)

1753

54.9%

 

(Missing)

1200

37.6%

 

-   [Minimum 5
    values](#-6201146505617089049extreme_values--6201146505617089049firstn)
-   [Maximum 5
    values](#-6201146505617089049extreme_values--6201146505617089049lastn)

Value

Count

Frequency (%)

 

0.044

1

\< 0.1%

 

0.048

1

\< 0.1%

 

0.052

1

\< 0.1%

 

0.055

3

0.1%

 

0.056

1

\< 0.1%

 

0.057

2

0.1%

 

0.058

2

0.1%

 

0.059

2

0.1%

 

0.06

2

0.1%

 

0.061

1

\< 0.1%

 

Value

Count

Frequency (%)

 

4.373

1

\< 0.1%

 

4.24

1

\< 0.1%

 

4.164

1

\< 0.1%

 

3.751

1

\< 0.1%

 

3.491

1

\< 0.1%

 

3.36

1

\< 0.1%

 

3.339

1

\< 0.1%

 

3.188

1

\< 0.1%

 

3.187

1

\< 0.1%

 

3.184

1

\< 0.1%

 

[LandMinTemperature](#pp_var_-6696416535259061525)\
Real number (ℝ)

`HIGH CORRELATION`\
`MISSING`\

Distinct

1872

Distinct (%)

94.0%

Missing

1200

Missing (%)

37.6%

Infinite

0

Infinite (%)

0.0%

Mean

2.743595382

Minimum

-5.407

Maximum

9.715

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:58.295572image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#-6696416535259061525bottom--6696416535259061525statistics)
-   [Histogram](#-6696416535259061525bottom--6696416535259061525histogram)
-   [Common
    values](#-6696416535259061525bottom--6696416535259061525common_values)
-   [Extreme
    values](#-6696416535259061525bottom--6696416535259061525extreme_values)

Quantile statistics

Minimum

-5.407

5-th percentile

-3.32445

Q1

-1.3345

median

2.9495

Q3

6.77875

95-th percentile

8.51045

Maximum

9.715

Range

15.122

Interquartile range (IQR)

8.11325

Descriptive statistics

Standard deviation

4.15583532

Coefficient of variation (CV)

1.514740602

Kurtosis

-1.433529954

Mean

2.743595382

Median Absolute Deviation (MAD)

4.088

Skewness

-0.05025501431

Sum

5465.242

Variance

17.27096721

Monotocity

Not monotonic

2020-10-27T15:12:58.438187image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

7.892

3

0.1%

 

8.161

3

0.1%

 

7.818

3

0.1%

 

8.184

3

0.1%

 

-1.139

3

0.1%

 

7.057

2

0.1%

 

-3.23

2

0.1%

 

5.176

2

0.1%

 

-1.942

2

0.1%

 

-3.764

2

0.1%

 

1.91

2

0.1%

 

7.965

2

0.1%

 

3.162

2

0.1%

 

0.555

2

0.1%

 

5.263

2

0.1%

 

-2.452

2

0.1%

 

8.205

2

0.1%

 

3.8

2

0.1%

 

-0.654

2

0.1%

 

7.796

2

0.1%

 

5.202

2

0.1%

 

6.597

2

0.1%

 

5.967

2

0.1%

 

8.012

2

0.1%

 

8.189

2

0.1%

 

Other values (1847)

1937

60.7%

 

(Missing)

1200

37.6%

 

-   [Minimum 5
    values](#-6696416535259061525extreme_values--6696416535259061525firstn)
-   [Maximum 5
    values](#-6696416535259061525extreme_values--6696416535259061525lastn)

Value

Count

Frequency (%)

 

-5.407

1

\< 0.1%

 

-5.345

1

\< 0.1%

 

-4.947

1

\< 0.1%

 

-4.717

1

\< 0.1%

 

-4.678

1

\< 0.1%

 

-4.621

1

\< 0.1%

 

-4.558

1

\< 0.1%

 

-4.519

1

\< 0.1%

 

-4.465

1

\< 0.1%

 

-4.365

1

\< 0.1%

 

Value

Count

Frequency (%)

 

9.715

1

\< 0.1%

 

9.684

1

\< 0.1%

 

9.569

1

\< 0.1%

 

9.551

1

\< 0.1%

 

9.482

1

\< 0.1%

 

9.456

1

\< 0.1%

 

9.428

1

\< 0.1%

 

9.409

1

\< 0.1%

 

9.407

1

\< 0.1%

 

9.344

1

\< 0.1%

 

[LandMinTemperatureUncertainty](#pp_var_-7957790986284982199)\
Real number (ℝ~≥0~)

`MISSING`\

Distinct

781

Distinct (%)

39.2%

Missing

1200

Missing (%)

37.6%

Infinite

0

Infinite (%)

0.0%

Mean

0.4318488956

Minimum

0.045

Maximum

3.498

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:58.582801image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#-7957790986284982199bottom--7957790986284982199statistics)
-   [Histogram](#-7957790986284982199bottom--7957790986284982199histogram)
-   [Common
    values](#-7957790986284982199bottom--7957790986284982199common_values)
-   [Extreme
    values](#-7957790986284982199bottom--7957790986284982199extreme_values)

Quantile statistics

Minimum

0.045

5-th percentile

0.08455

Q1

0.155

median

0.279

Q3

0.45825

95-th percentile

1.3948

Maximum

3.498

Range

3.453

Interquartile range (IQR)

0.30325

Descriptive statistics

Standard deviation

0.4458378371

Coefficient of variation (CV)

1.032393139

Kurtosis

7.0548683

Mean

0.4318488956

Median Absolute Deviation (MAD)

0.135

Skewness

2.384389692

Sum

860.243

Variance

0.198771377

Monotocity

Not monotonic

2020-10-27T15:12:58.717439image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

0.237

12

0.4%

 

0.13

11

0.3%

 

0.082

11

0.3%

 

0.145

11

0.3%

 

0.126

11

0.3%

 

0.213

10

0.3%

 

0.224

10

0.3%

 

0.338

10

0.3%

 

0.127

9

0.3%

 

0.125

9

0.3%

 

0.086

8

0.3%

 

0.313

8

0.3%

 

0.134

8

0.3%

 

0.092

8

0.3%

 

0.085

8

0.3%

 

0.113

8

0.3%

 

0.235

8

0.3%

 

0.345

8

0.3%

 

0.17

8

0.3%

 

0.115

8

0.3%

 

0.216

8

0.3%

 

0.252

8

0.3%

 

0.155

8

0.3%

 

0.247

8

0.3%

 

0.193

7

0.2%

 

Other values (756)

1769

55.4%

 

(Missing)

1200

37.6%

 

-   [Minimum 5
    values](#-7957790986284982199extreme_values--7957790986284982199firstn)
-   [Maximum 5
    values](#-7957790986284982199extreme_values--7957790986284982199lastn)

Value

Count

Frequency (%)

 

0.045

1

\< 0.1%

 

0.047

1

\< 0.1%

 

0.051

3

0.1%

 

0.053

1

\< 0.1%

 

0.054

2

0.1%

 

0.055

1

\< 0.1%

 

0.058

1

\< 0.1%

 

0.06

3

0.1%

 

0.061

2

0.1%

 

0.062

2

0.1%

 

Value

Count

Frequency (%)

 

3.498

1

\< 0.1%

 

3.428

1

\< 0.1%

 

2.963

1

\< 0.1%

 

2.929

1

\< 0.1%

 

2.843

1

\< 0.1%

 

2.822

1

\< 0.1%

 

2.795

1

\< 0.1%

 

2.714

1

\< 0.1%

 

2.594

1

\< 0.1%

 

2.56

1

\< 0.1%

 

[LandAndOceanAverageTemperature](#pp_var_-8221517211577610154)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`MISSING`\

Distinct

1616

Distinct (%)

81.1%

Missing

1200

Missing (%)

37.6%

Infinite

0

Infinite (%)

0.0%

Mean

15.21256576

Minimum

12.475

Maximum

17.611

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:58.853076image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#-8221517211577610154bottom--8221517211577610154statistics)
-   [Histogram](#-8221517211577610154bottom--8221517211577610154histogram)
-   [Common
    values](#-8221517211577610154bottom--8221517211577610154common_values)
-   [Extreme
    values](#-8221517211577610154bottom--8221517211577610154extreme_values)

Quantile statistics

Minimum

12.475

5-th percentile

13.3

Q1

14.047

median

15.251

Q3

16.39625

95-th percentile

17.0166

Maximum

17.611

Range

5.136

Interquartile range (IQR)

2.34925

Descriptive statistics

Standard deviation

1.274092954

Coefficient of variation (CV)

0.08375266699

Kurtosis

-1.322464368

Mean

15.21256576

Median Absolute Deviation (MAD)

1.179

Skewness

-0.05604937795

Sum

30303.431

Variance

1.623312857

Monotocity

Not monotonic

2020-10-27T15:12:59.006634image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

15.005

5

0.2%

 

13.311

4

0.1%

 

16.783

4

0.1%

 

13.26

4

0.1%

 

16.496

4

0.1%

 

16.846

4

0.1%

 

16.596

4

0.1%

 

15.927

4

0.1%

 

16.912

3

0.1%

 

16.634

3

0.1%

 

14.607

3

0.1%

 

13.724

3

0.1%

 

14.161

3

0.1%

 

16.216

3

0.1%

 

14.047

3

0.1%

 

16.605

3

0.1%

 

14.359

3

0.1%

 

15.823

3

0.1%

 

15.126

3

0.1%

 

13.904

3

0.1%

 

16.83

3

0.1%

 

14.418

3

0.1%

 

16.437

3

0.1%

 

16.745

3

0.1%

 

13.54

3

0.1%

 

Other values (1591)

1908

59.8%

 

(Missing)

1200

37.6%

 

-   [Minimum 5
    values](#-8221517211577610154extreme_values--8221517211577610154firstn)
-   [Maximum 5
    values](#-8221517211577610154extreme_values--8221517211577610154lastn)

Value

Count

Frequency (%)

 

12.475

1

\< 0.1%

 

12.62

1

\< 0.1%

 

12.658

1

\< 0.1%

 

12.702

1

\< 0.1%

 

12.732

1

\< 0.1%

 

12.828

1

\< 0.1%

 

12.833

1

\< 0.1%

 

12.839

1

\< 0.1%

 

12.84

1

\< 0.1%

 

12.879

1

\< 0.1%

 

Value

Count

Frequency (%)

 

17.611

1

\< 0.1%

 

17.609

1

\< 0.1%

 

17.607

1

\< 0.1%

 

17.589

1

\< 0.1%

 

17.578

1

\< 0.1%

 

17.568

1

\< 0.1%

 

17.532

1

\< 0.1%

 

17.508

1

\< 0.1%

 

17.503

2

0.1%

 

17.491

1

\< 0.1%

 

[LandAndOceanAverageTemperatureUncertainty](#pp_var_8989519429109620280)\
Real number (ℝ~≥0~)

`HIGH CORRELATION`\
`MISSING`\

Distinct

294

Distinct (%)

14.8%

Missing

1200

Missing (%)

37.6%

Infinite

0

Infinite (%)

0.0%

Mean

0.1285321285

Minimum

0.042

Maximum

0.457

Zeros

0

Zeros (%)

0.0%

Memory size

25.1 KiB

2020-10-27T15:12:59.308824image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Toggle details

-   [Statistics](#8989519429109620280bottom-8989519429109620280statistics)
-   [Histogram](#8989519429109620280bottom-8989519429109620280histogram)
-   [Common
    values](#8989519429109620280bottom-8989519429109620280common_values)
-   [Extreme
    values](#8989519429109620280bottom-8989519429109620280extreme_values)

Quantile statistics

Minimum

0.042

5-th percentile

0.052

Q1

0.063

median

0.122

Q3

0.151

95-th percentile

0.28345

Maximum

0.457

Range

0.415

Interquartile range (IQR)

0.088

Descriptive statistics

Standard deviation

0.07358679601

Coefficient of variation (CV)

0.5725167462

Kurtosis

1.525069706

Mean

0.1285321285

Median Absolute Deviation (MAD)

0.0535

Skewness

1.275594309

Sum

256.036

Variance

0.005415016546

Monotocity

Not monotonic

2020-10-27T15:12:59.438512image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value

Count

Frequency (%)

 

0.061

49

1.5%

 

0.059

47

1.5%

 

0.06

45

1.4%

 

0.062

44

1.4%

 

0.057

41

1.3%

 

0.058

39

1.2%

 

0.056

37

1.2%

 

0.063

35

1.1%

 

0.054

35

1.1%

 

0.064

31

1.0%

 

0.122

30

0.9%

 

0.129

28

0.9%

 

0.127

28

0.9%

 

0.125

27

0.8%

 

0.052

27

0.8%

 

0.053

26

0.8%

 

0.05

25

0.8%

 

0.126

25

0.8%

 

0.128

25

0.8%

 

0.137

23

0.7%

 

0.134

23

0.7%

 

0.051

22

0.7%

 

0.13

22

0.7%

 

0.055

22

0.7%

 

0.065

22

0.7%

 

Other values (269)

1214

38.0%

 

(Missing)

1200

37.6%

 

-   [Minimum 5
    values](#8989519429109620280extreme_values-8989519429109620280firstn)
-   [Maximum 5
    values](#8989519429109620280extreme_values-8989519429109620280lastn)

Value

Count

Frequency (%)

 

0.042

1

\< 0.1%

 

0.043

1

\< 0.1%

 

0.045

3

0.1%

 

0.046

3

0.1%

 

0.047

4

0.1%

 

0.048

12

0.4%

 

0.049

13

0.4%

 

0.05

25

0.8%

 

0.051

22

0.7%

 

0.052

27

0.8%

 

Value

Count

Frequency (%)

 

0.457

1

\< 0.1%

 

0.442

1

\< 0.1%

 

0.438

1

\< 0.1%

 

0.427

1

\< 0.1%

 

0.417

1

\< 0.1%

 

0.414

1

\< 0.1%

 

0.402

1

\< 0.1%

 

0.389

1

\< 0.1%

 

0.387

1

\< 0.1%

 

0.378

2

0.1%

 

Interactions {.page-header}
============

-   [LandAverageTemperature](#interactions-interactions_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions-interactions_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions-interactions_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions-interactions_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions-interactions_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions-interactions_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions-interactions_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions-interactions_LandAndOceanAverageTemperatureUncertainty)

-   [LandAverageTemperature](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandAverageTemperature-interactions_LandAverageTemperature_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:47.386606image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:47.653973image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:47.790606image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:47.923257image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.045922image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.178568image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.314205image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.438872image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandAverageTemperatureUncertainty-interactions_LandAverageTemperatureUncertainty_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:48.565530image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.706159image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.839801image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:48.974438image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:49.107083image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:49.240728image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:49.407249image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:49.540922image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandMaxTemperature-interactions_LandMaxTemperature_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:49.668581image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:49.800229image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:49.939855image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:50.083440image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:50.232073image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:50.369705image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:50.503316image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:50.631005image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandMaxTemperatureUncertainty-interactions_LandMaxTemperatureUncertainty_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:50.760659image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:50.876351image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.017110image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.137811image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.336289image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.454940image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.572654image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.683359image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandMinTemperature-interactions_LandMinTemperature_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:51.793066image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:51.924713image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.059352image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.191002image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.312674image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.446317image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.576967image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.704626image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandMinTemperatureUncertainty-interactions_LandMinTemperatureUncertainty_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:52.827297image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:52.956952image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.094582image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.228230image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.349869image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.480551image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.611201image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.734868image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandAndOceanAverageTemperature-interactions_LandAndOceanAverageTemperature_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:53.874465image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:53.998164image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.120804image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.239518image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.352190image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.470899image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.592541image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.704281image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

-   [LandAverageTemperature](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandAverageTemperature)
-   [LandAverageTemperatureUncertainty](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandAverageTemperatureUncertainty)
-   [LandMaxTemperature](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandMaxTemperature)
-   [LandMaxTemperatureUncertainty](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandMaxTemperatureUncertainty)
-   [LandMinTemperature](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandMinTemperature)
-   [LandMinTemperatureUncertainty](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandMinTemperatureUncertainty)
-   [LandAndOceanAverageTemperature](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandAndOceanAverageTemperature)
-   [LandAndOceanAverageTemperatureUncertainty](#interactions_LandAndOceanAverageTemperatureUncertainty-interactions_LandAndOceanAverageTemperatureUncertainty_LandAndOceanAverageTemperatureUncertainty)

2020-10-27T15:12:54.816944image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:54.934658image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:55.056332image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:55.176012image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:55.289709image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:55.406397image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:55.526076image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:55.740503image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Correlations {.page-header}
============

Toggle correlation descriptions

-   [Pearson's r](#correlations_tab-pearson)
-   [Spearman's ρ](#correlations_tab-spearman)
-   [Kendall's τ](#correlations_tab-kendall)
-   [Phik (φk)](#correlations_tab-phi_k)

2020-10-27T15:12:59.565140image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

### Pearson's r

The Pearson's correlation coefficient (*r*) is a measure of linear
correlation between two variables. It's value lies between -1 and +1, -1
indicating total negative linear correlation, 0 indicating no linear
correlation and 1 indicating total positive linear correlation.
Furthermore, *r* is invariant under separate changes in location and
scale of the two variables, implying that for a linear function the
angle to the x-axis does not affect *r*.\
\
To calculate *r* for two variables *X* and *Y*, one divides the
covariance of *X* and *Y* by the product of their standard deviations.

2020-10-27T15:12:59.794527image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

### Spearman's ρ

The Spearman's rank correlation coefficient (*ρ*) is a measure of
monotonic correlation between two variables, and is therefore better in
catching nonlinear monotonic correlations than Pearson's *r*. It's value
lies between -1 and +1, -1 indicating total negative monotonic
correlation, 0 indicating no monotonic correlation and 1 indicating
total positive monotonic correlation.\
\
To calculate *ρ* for two variables *X* and *Y*, one divides the
covariance of the rank variables of *X* and *Y* by the product of their
standard deviations.

2020-10-27T15:13:00.021921image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

### Kendall's τ

Similarly to Spearman's rank correlation coefficient, the Kendall rank
correlation coefficient (*τ*) measures ordinal association between two
variables. It's value lies between -1 and +1, -1 indicating total
negative correlation, 0 indicating no correlation and 1 indicating total
positive correlation. \
\
To calculate *τ* for two variables *X* and *Y*, one determines the
number of concordant and discordant pairs of observations. *τ* is given
by the number of concordant pairs minus the discordant pairs divided by
the total number of pairs.

2020-10-27T15:13:00.242361image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

### Phik (φk)

Phik (φk) is a new and practical correlation coefficient that works
consistently between categorical, ordinal and interval variables,
captures non-linear dependency and reverts to the Pearson correlation
coefficient in case of a bivariate normal input distribution. There is
extensive documentation available
[here](https://phik.readthedocs.io/en/latest/index.html).

Missing values {.page-header}
==============

-   [Count](#missing-bar)
-   [Matrix](#missing-matrix)
-   [Heatmap](#missing-heatmap)
-   [Dendrogram](#missing-dendrogram)

2020-10-27T15:12:55.949945image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:56.194358image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:56.456456image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

2020-10-27T15:12:56.685878image/svg+xmlMatplotlib v3.3.2,
https://matplotlib.org/

Sample {.page-header}
======

First rows {.indent}
----------

dt

LandAverageTemperature

LandAverageTemperatureUncertainty

LandMaxTemperature

LandMaxTemperatureUncertainty

LandMinTemperature

LandMinTemperatureUncertainty

LandAndOceanAverageTemperature

LandAndOceanAverageTemperatureUncertainty

0

1750-01-01

3.034

3.574

NaN

NaN

NaN

NaN

NaN

NaN

1

1750-02-01

3.083

3.702

NaN

NaN

NaN

NaN

NaN

NaN

2

1750-03-01

5.626

3.076

NaN

NaN

NaN

NaN

NaN

NaN

3

1750-04-01

8.490

2.451

NaN

NaN

NaN

NaN

NaN

NaN

4

1750-05-01

11.573

2.072

NaN

NaN

NaN

NaN

NaN

NaN

5

1750-06-01

12.937

1.724

NaN

NaN

NaN

NaN

NaN

NaN

6

1750-07-01

15.868

1.911

NaN

NaN

NaN

NaN

NaN

NaN

7

1750-08-01

14.750

2.231

NaN

NaN

NaN

NaN

NaN

NaN

8

1750-09-01

11.413

2.637

NaN

NaN

NaN

NaN

NaN

NaN

9

1750-10-01

6.367

2.668

NaN

NaN

NaN

NaN

NaN

NaN

Last rows {.indent}
---------

dt

LandAverageTemperature

LandAverageTemperatureUncertainty

LandMaxTemperature

LandMaxTemperatureUncertainty

LandMinTemperature

LandMinTemperatureUncertainty

LandAndOceanAverageTemperature

LandAndOceanAverageTemperatureUncertainty

3182

2015-03-01

6.740

0.060

12.659

0.096

0.894

0.079

15.193

0.061

3183

2015-04-01

9.313

0.088

15.224

0.137

3.402

0.147

15.962

0.061

3184

2015-05-01

12.312

0.081

18.181

0.117

6.313

0.153

16.774

0.058

3185

2015-06-01

14.505

0.068

20.364

0.133

8.627

0.168

17.390

0.057

3186

2015-07-01

15.051

0.086

20.904

0.109

9.326

0.225

17.611

0.058

3187

2015-08-01

14.755

0.072

20.699

0.110

9.005

0.170

17.589

0.057

3188

2015-09-01

12.999

0.079

18.845

0.088

7.199

0.229

17.049

0.058

3189

2015-10-01

10.801

0.102

16.450

0.059

5.232

0.115

16.290

0.062

3190

2015-11-01

7.433

0.119

12.892

0.093

2.157

0.106

15.252

0.063

3191

2015-12-01

5.518

0.100

10.725

0.154

0.287

0.099

14.774

0.062

Report generated with
[pandas-profiling](https://github.com/pandas-profiling/pandas-profiling).
