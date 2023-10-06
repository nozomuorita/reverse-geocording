"""
・Get address data for each prefecture from "https://nlftp.mlit.go.jp/isj/"
"""

# import modules and setting
import os
import urllib.request
import urllib.error
import shutil
import pandas as pd
import time

# main
def main():
    
    df = pd.DataFrame()
    setting()
    # Processing for all prefectures
    for i in range(1, 48):
        time.sleep(3)
        prefecture_code = str(i).zfill(2)
        new_data = download_data(prefecture_code)
        df = processing(df, new_data, prefecture_code)
        print(f'完了：prefecture-code{prefecture_code}')
    save_data_to_csv(df)

    
def setting():
    """
    initialization

    ・Create directory for storing address data
    """
    data_dir_path = "../data/address/"
    
    # make directory for storing
    if os.path.exists(data_dir_path):
        # if exist, delete all and new directory
        shutil.rmtree(data_dir_path)
    
    os.mkdir(data_dir_path)

def download_data(prefecture_code: str):
    """
    Download address data for a prefecture

    Args:
        prefecture_code (str): prefecture code
    """
    
    #prefecture_code = str(prefecture_code).zfill(2)
    url = f"https://nlftp.mlit.go.jp/isj/dls/data/16.0b/{prefecture_code}000-16.0b.zip"
    save_path = f"../data/address/{prefecture_code}.zip"
    
    try:
        with urllib.request.urlopen(url) as download_file:
            data = download_file.read()
            with open(save_path, mode='wb') as save_file:
                save_file.write(data)
    except urllib.error.URLError as e:
        print(e)

    # Unpack the zip file
    shutil.unpack_archive(f'../data/address/{prefecture_code}.zip', '../data/address/')
    # delete zip file
    os.remove(f'../data/address/{prefecture_code}.zip')
    data = pd.read_csv(f'../data/address/{prefecture_code}000-16.0b/{prefecture_code}_2022.csv', encoding="cp932")
    return data   
 
def processing(df_base: pd.DataFrame, df_new: pd.DataFrame, prefecture_code: str):
    """
    main process

    Args:
        df_base (pd.DataFrame): Original data to be combined
        df_new (pd.DataFrame): New data to be combined
        prefecture_code (str): prefecture code

    Returns:
        pd.DataFrame: Combined data
    """
    
    df = pd.concat([df_base, df_new])
    # delete directory after concat
    shutil.rmtree(f'../data/address/{prefecture_code}000-16.0b')
    return df

def save_data_to_csv(df: pd.DataFrame):
    """
    Save address data

    Args:
        df (pd.DataFrame): address data
    """
    df.to_csv('../data/address/addres-data.csv')
    
if __name__=="__main__":
    main()