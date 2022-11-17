## Task 1

- Start with creating connection to Dropbox using the token generated from the Dropbox App
- To download `enroll_data.csv`, use `files_download()` and write it to a file
- Read the csv and convert columns `birth date` and `date of consent` for easy calculation
- `age` function calculates age from orginal date of consent
- `disguise_date_of_consent` function generates random number of days greater than 35000 days to have  given dates earlier than year 1925 and offset_days
- Save  `days offset` to `enroll_data_offset_DP.csv` and 
`enroll data` to `enroll_data_anon_DP.csv`
- Upload `enroll_data_offset_DP.csv` and `enroll_data_anon_DP.csv` to Dropbox using `files_upload()`