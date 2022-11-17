import random
import dropbox
import pandas as pd

# function to calculate age from orginal date of consent
def age(birth_date, date_of_consent):
    return date_of_consent.year - birth_date.year - ((date_of_consent.month, date_of_consent.day) < (birth_date.month, birth_date.day))

# function to disguise the date of consent
def disguise_date_of_consent(date_of_consent):
    # generate random number of days greater than 35000 days to have  given dates earlier than year 1925
    offset_days = random.randint(35000, 40000) 
    date_of_consent2 = date_of_consent - pd.DateOffset(days=offset_days)
    return date_of_consent2, offset_days

def main():
    dbx = dropbox.Dropbox("sl.BTRxsw0GeCDjsMcaJSrmtxe4LUk7muE7wMuifx4fpBoljqwBNWeHtQM2JhOULr8RNnDU2riB6Z1y1BZ5FdQS040rk1w-YYCM0uWxxIi2cbCGySwYWTd6BVDz9qhwLtmEElTTbQw")

    with open('enroll_data.csv', 'wb') as f:
        metadata, res = dbx.files_download(path='/recruitment_project_2/enroll_data.csv')
        f.write(res.content)
    
    enroll_data = pd.read_csv('enroll_data.csv')
    # convert columns to datetime format
    enroll_data['birth date'] = pd.to_datetime(enroll_data['birth date'])
    enroll_data['date of consent'] = pd.to_datetime(enroll_data['date of consent'])
    
    # get age from birth date and date of consent
    enroll_data['age'] = enroll_data.apply(lambda x: age(x['birth date'], x['date of consent']), axis=1)

    # disguise the date of consent
    enroll_data[['date of consent','days_offset']] = enroll_data.apply(lambda x: disguise_date_of_consent(x['date of consent']), axis=1, result_type='expand')
    
    # save days offset to csv
    enroll_data[['days_offset']].to_csv('enroll_data_offset_DP.csv', index=False)

    # upload to dropbox
    with open('enroll_data_offset_DP.csv', 'rb') as f:
        dbx.files_upload(f.read(), '/recruitment_project_2/enroll_data_offset_DP.csv')

    enroll_data.drop(columns='days_offset', inplace=True)
    
    # save enroll data to csv
    enroll_data.to_csv('enroll_data_anon_DP.csv', index=False)
    
    # upload to dropbox
    with open('enroll_data_anon_DP.csv', 'rb') as f:
        dbx.files_upload(f.read(), '/recruitment_project_2/enroll_data_anon_DP.csv')

    return

if __name__ == '__main__':
    main()