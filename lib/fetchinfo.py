import sqlite3

def victim_details():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    details = cursor.execute("SELECT * FROM VICTIM")       
    data_list = details.fetchall()
    return data_list

def fetch_data():
    details = victim_details()
    lat_list = []
    lon_list = []
    city_list = []
    country_list = []
    isp_list = []
    unique_key = []
    ipaddress = []
    for detail in details:
        unique_key.append(detail[0])
        ipaddress.append(detail[1])
        lat_list.append(detail[2])
        lon_list.append(detail[3])
        city_list.append(detail[4])
        country_list.append(detail[5])
        isp_list.append(detail[6])
    return ( unique_key, ipaddress, lat_list, lon_list, city_list, country_list, isp_list)

def query(unique_key):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    details = cursor.execute(f"SELECT * FROM VICTIM WHERE UniqueId='{unique_key}'")
    details = details.fetchall()
    lat_list = []
    lon_list = []
    city_list = []
    country_list = []
    isp_list = []
    unique_key = []
    ipaddress = []
    for detail in details:
        unique_key.append(detail[0])
        ipaddress.append(detail[1])
        lat_list.append(detail[2])
        lon_list.append(detail[3])
        city_list.append(detail[4])
        country_list.append(detail[5])
        isp_list.append(detail[6])
    return ( unique_key, ipaddress, lat_list, lon_list, city_list, country_list, isp_list)

def delete(unique_key):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM VICTIM WHERE UniqueId='{unique_key}'")
    connection.commit()
    cursor.close()