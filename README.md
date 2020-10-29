
# Deep-Learning Dummy Data File Generator from csv File

---


## Overview

- Load csv File
- Meta Information Parsing From csv File
- Generate to Python Source File
- Run Generated Python Source File When Create Dummy Data File for Deep-Learning



---


## Usage

- Install the prerequisites DLDummyGen

```
> pip install DLDummyGen
```


- Sample Code

```python

from DLDummyGen.DLDummyGen import DLLogger, DLDummyFieldHandler, DLDummyGenerator

if __name__ == '__main__':

    # Original csv File (Real Data)
    CSV_FILE_NAME = "pima-indians-diabetes.csv"
    
    # Maximum length of data to be generated
    GEN_ROW_MAX = 10
    
    # Length of Unique String Field (eg, Code Value) Judgment criteria
    UNIQUE_FIELD_COUNT = 1000
    
    
    # Create Logging Object
    logger = DLLogger()
    
    dg = DLDummyGenerator(CSV_FILE_NAME, GEN_ROW_MAX, UNIQUE_FIELD_COUNT, logger=logger)
    
    # Run to Generate python source code
    dg.gen_src_from_csv()

```


- With Custom Field Callback Handler Code

```python

from DLDummyGen.DLDummyGen import DLLogger, DLDummyFieldHandler, DLDummyGenerator

class DLDummyFieldAutoIncrement(DLDummyFieldHandler):
    """
    Auto Increment ID - Custom Field Callback Handler
    """

    def on_custom_field(self, dg, fgen, column, dataset):
        fgen.write('gen_df[\"' + column + '\"] = ')
        fgen.write('[\'ID{:05d}\'.format(idx+1) for idx in range(GEN_ROW_MAX)]\n\n')


class DLDummyFieldChoiceString(DLDummyFieldHandler):
    """
    Choice String - Custom Field Callback Handler
    """

    def on_custom_field(self, dg, fgen, column, dataset):
        fgen.write('gen_df[\"' + column + '\"] = ')
        fgen.write('choice([\"' + '\", \"'.join(['Y', 'N']) + '\"], GEN_ROW_MAX)\n\n')

...

if __name__ == '__main__':

    # Original csv File (Real Data)
    CSV_FILE_NAME = "pima-indians-diabetes.csv"
    
    # Maximum length of data to be generated
    GEN_ROW_MAX = 10
    
    # Length of Unique String Field (eg, Code Value) Judgment criteria
    UNIQUE_FIELD_COUNT = 1000
    
    
    # Create Logging Object
    logger = DLLogger()
    
    dg = DLDummyGenerator(CSV_FILE_NAME, GEN_ROW_MAX, UNIQUE_FIELD_COUNT, logger=logger)
    
    
    # Definition to generate random date/time
    # [[Field Name, Start Date, End Date, Input Date Format, Output Date Format]]
    DATE_FIELDS = [
        [' Glucose', '2019-01', '2019-12', '%Y-%m', '%Y%m']
    ]
    dg.set_date_fields(DATE_FIELDS)
    
    # Definition to custom field handler
    # [[Field Name, DLDummyFieldHandler class implement instance]]
    CUSTOM_FIELDS = [
        ['Pregnancies', DLDummyFieldAutoIncrement()]
        , [' Outcome', DLDummyFieldChoiceString()]
    ]
    dg.set_custom_fields(CUSTOM_FIELDS)
    
    # Run to Generate python source code
    dg.gen_src_from_csv()

```


---


## Generated Python Source Code

- Install the prerequisites numpy, pandas and faker (Python 3.7)

```
> pip install numpy
> pip install pandas
> pip install faker
```

- Generated Python Source Code

```python
import pandas as pd

import numpy as np
from numpy import random
from datetime import datetime

...

gen_df = pd.DataFrame()

# Pregnancies
gen_df["Pregnancies"] = ['ID{:05d}'.format(idx+1) for idx in range(GEN_ROW_MAX)]

#  Glucose
gen_df[" Glucose"] = [fake.date_between(
    start_date=datetime.strptime('2019-01', '%Y-%m')
    , end_date=datetime.strptime('2019-12', '%Y-%m')).strftime('%Y%m')
    for _ in range(GEN_ROW_MAX)]

...

#  Age
gen_df[" Age"] = random.randint(21, 81 + 1, GEN_ROW_MAX, dtype="int64")

#  Outcome
gen_df[" Outcome"] = choice(["Y", "N"], GEN_ROW_MAX)


gen_df.to_csv('gen_pima-indians-diabetes.csv', index=False)

print('\ngen_pima-indians-diabetes.csv File Created...\n')

```

---


## Appendix

- [Numpy](https://numpy.org/doc/stable/) : NumPy is the fundamental package for scientific computing in Python
- [Pandas](https://pandas.pydata.org/docs) : pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
- [Faker](https://github.com/joke2k/faker) : Python package that generates fake data for you



