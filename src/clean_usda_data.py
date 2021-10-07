import os
import pandas as pd
import re

data_dir = '..'+os.path.sep+'data'
raw_data_dir = os.path.join(data_dir,'raw')
clean_data_dir = os.path.join(data_dir,'clean')
usda_filenames = [os.path.join(raw_data_dir,f) for f in os.listdir(raw_data_dir) if f.startswith('USDA')]
for f in usda_filenames:
    print(f)
    
for f in usda_filenames:
    df=pd.read_csv(f)
    # add col for county vs. city:
    if ('County' in df.columns) and ('State' in df.columns):
        df = df[df.State=='VA']
        if (len(df)==134):
            df['geo_type'] = pd.Series(['county']*95+['city']*39,index=df.index)
    # remove extra commas, convert to numeric:
    df=df.applymap(lambda x: x if not(isinstance(x,str)) else re.sub(',(?=\d)','',x))
    for c in df:
        try:
            df[c] = df[c].astype(float)
        except:
            pass
    # output:
    df.to_csv(f.replace(os.path.sep+'raw'+os.path.sep,os.path.sep+'clean'+os.path.sep))