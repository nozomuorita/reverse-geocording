import pandas as pd
import time

start_time = time.perf_counter() # measure run time
data = pd.read_csv("../data/address/address-data.csv", index_col=0)
data2 = pd.read_csv("../data/address/address-data2.csv", index_col=0)
prefecture_code = pd.read_csv("../data/prefecture/prefecture-code.csv", index_col=0)
origin = pd.read_csv("../data/origin/data_origin.csv", index_col=0)

def main():
    address_lst = []
    interval = 20  # data interval
    # specified address at 20 data interval(about 1 hour)
    for i in range(0, len(origin), interval):
        if i%1000==0 and i!=0: 
            print(f'完了: {i}')
            # break
        latitude = origin.iloc[i, 2]
        longitude = origin.iloc[i, 3]
        
        if len(c:=candidate(latitude, longitude))==1: p=c[0]
        else: p=specific(c, latitude, longitude)
        
        if len(address_lst)+interval<=len(origin): address_lst+=[p]*interval
        else: address_lst+=[p]*(len(origin)-len(address_lst))
        
    if len(address_lst)!=len(origin):
        print('length error')
        exit()
    origin['ADDRESS'] = address_lst
    origin.to_csv("../data/origin/data_origin_add_address.csv")
    run_time = time.perf_counter()-start_time
    print(f'run time: {run_time}')
    

def candidate(lat: float, lon: float):
    """
    Get Prefecture expected the address located
    """
    
    candidate = []
    for i in range(len(data2)):
        p = data2.iloc[i, 0]
        max_lat = data2.iloc[i, 1]
        min_lat = data2.iloc[i, 2]
        max_lon = data2.iloc[i, 3]
        min_lon = data2.iloc[i, 4]
        
        if (min_lat<lat<max_lat) and (min_lon<lon<max_lon):
            candidate.append(p)
    
    return candidate
        
def specific(candidate: list, lat:float, lon:float):
    """
    Specify prefecture

    Args:
        candidate (list): candidate list of prefectures
        lat (float): latitude
        lon (float): longitude

    Returns:
        str: a specified prefecture 
    """
    dist = float('inf')
    for i in candidate:
        tmp = data[data['都道府県名']==i]
        for j in range(len(tmp)):
            lat_j = tmp.iloc[j, 6]
            lon_j = tmp.iloc[j, 7]
            if (d:=((lat-lat_j)**2 + (lon-lon_j)**2)**0.5)<dist:
                dist = d
                # ans = tmp.iloc[j, 1] + tmp.iloc[j, 3] + tmp.iloc[j, 5]
                ans = tmp.iloc[j, 1]
                
    return ans
        
if __name__=="__main__":
    main()