#!/usr/bin/env python
# coding: utf-8


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


if __name__ == '__main__':

    # Original csv File (Real Data)
    CSV_FILE_NAME = "pima-indians-diabetes.csv"

    # Maximum length of data to be generated
    GEN_ROW_MAX = 10

    # Length of Unique String Field (eg, Code Value) Judgment criteria
    UNIQUE_FIELD_COUNT = 1000

    # 로깅 객체 생성
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

