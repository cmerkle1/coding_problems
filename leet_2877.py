'''Create dataframe from 2d list
variables student_id and age'''
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns =["student_id", "age"])
    return df
