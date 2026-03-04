'''Select the name and age of a student given the student id in a dataframe using pandas'''
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]
