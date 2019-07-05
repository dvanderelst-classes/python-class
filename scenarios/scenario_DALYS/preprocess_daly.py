import pandas
import copy

sheet_names = ['All ages', '0-4','5-14','15-29','30-49','50-59','60-69','70+']
#sheet_names = [sheet_names[5]]

# in raw
sex_column = 0
ghe_column = 1
first_data_column = 7 #afghanistan
first_data_row = 5 #country name
last_data_row = 659

# in data
first_row = 4

for sheet_name in sheet_names:
    sheet = 'DALYs ' + sheet_name
    print(sheet)

    read = pandas.read_excel('daly.xlsx', sheet_name= sheet, na_values='.')

    #%%
    raw = copy.copy(read)
    raw = raw.reset_index()

    data = pandas.concat((raw.iloc[first_data_row:last_data_row+1, sex_column],
                          raw.iloc[first_data_row:last_data_row+1, ghe_column],
                          raw.iloc[first_data_row:last_data_row+1, first_data_column:]), axis=1)

    header = data.iloc[0, :]
    iso = data.iloc[1, :]
    data.columns = header.values

    data = data.iloc[4:,:]

    not_na = -pandas.isna(data['GHE code'])
    data = data.loc[not_na.values, :]

    #%%

    countries = raw.iloc[5,8:]
    population_persons = raw.iloc[8,8:]
    population_males = raw.iloc[226, 8:]
    population_females = raw.iloc[444, 8:]

    norm_persons = pandas.DataFrame()
    norm_persons['country'] = countries
    norm_persons['population'] = population_persons
    norm_persons['sex'] = 'Persons'
    norm_persons['ISO'] = iso

    norm_males = pandas.DataFrame()
    norm_males['country'] = countries
    norm_males['population'] = population_males
    norm_males['sex'] = 'Males'
    norm_males['ISO'] = iso

    norm_females = pandas.DataFrame()
    norm_females['country'] = countries
    norm_females['population'] = population_females
    norm_females['sex'] = 'Females'
    norm_females['ISO'] = iso

    norm = pandas.concat((norm_persons, norm_males, norm_females))

    #%%
    molten = pandas.melt(data, id_vars=['GHE code', 'Sex'])
    molten.columns = ['GHE','sex', 'country', 'daly']

    molten = pandas.merge(molten, norm, on=['country', 'sex'])
    molten['daly_norm_pm'] = (molten['daly'] / molten['population']) * 1000
    molten['group'] = sheet

    file_name = sheet.replace(' ', '_')
    file_name = file_name + '.csv'

    molten = molten.dropna(axis=0, how='all')

    molten.to_csv(file_name, index=False)

#%% Concatenate

age1 = pandas.read_csv('DALYs_0-4.csv')
age2 = pandas.read_csv('DALYs_5-14.csv')
age3 = pandas.read_csv('DALYs_15-29.csv')
age4 = pandas.read_csv('DALYs_30-49.csv')
age5 = pandas.read_csv('DALYs_50-59.csv')
age6 = pandas.read_csv('DALYs_60-69.csv')
age7 = pandas.read_csv('DALYs_70+.csv')

all = pandas.concat((age1, age2, age3, age4, age5, age6, age7))

#%% Add gdp

gdp = pandas.read_excel('gdp.xlsx', sheet_name= 'Data')
gdp = gdp.loc[:, ['ISO', '2016']]
gdp.columns = ['ISO', 'gdp']

all = pandas.merge(all, gdp, on='ISO')



#%% write

all.to_csv('DALYS.csv', index=False)