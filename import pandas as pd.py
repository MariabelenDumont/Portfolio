import pandas as pd
regions = {"Armenia":["Armenia"],
                    "Belize":["San Ignacio"],
                    "Bolivia":["Caranavi", "La Paz"],
                    "Brazil":["Brazil","Ern Brazil'","Bahia","Amazonas","Ipanema", "Minas Gerais", "Sul De Minas", "Ern Minas Gerais", "Minas Gerais State", "Chapada Diamantina","Carmo De Minas", "Ern Brazil"],
                    "Burundi":["Kayanza", "Buhinyuza", "Burundi", "Ern Burundi"],
                    "China":["Lintong"],
                    "Colombia":["Colombia","Ern Colombia","Caldas", "Valle Del Colombia", "Urrao","Aratoca", "Risaralda", "Quindo", "Valle De Cauca", "Cauca", "Nario","Gaitania","Valle Del Cauca", "Cundinamarca", "Narino", "Huila", "Tolima", "Nariño", "Antioquia", "Caicedonia", "Planadas", "Pitalito", "Quindio"],
                    "Costa Rica":["Tarrazu","Sabanilla De Costa Rica","Turrubares", "Pos Volcano","Cartago", "Sabanilla De Costa Rica", "Mercedes Sur", "El Guarco", "Alajuela", "Brunca", "Costa Rica", "Sabanilla De Alajuela", "Santa Maria De Dota", "Naranjo", "Tarrazú"],
                    "Democratic Republic of the Congo":["Kivu", "Kalehe"],
                    "Dominican Republic":["Nueva Suiza", "Jarabacoa"],
                    "Ecuador":["Pichincha", "Santa Elena", "San Jose De Minas", "Ern Ecuador"],
                    "El Salvador":["El Salvador","Ern El Salvador","Ern El Salvador","El Salvadorilamatepec", "Ahuachapan", "La Libertad", "Chalatenango", "Apaneca-Ilamatepec", "Tecapa Chinameca", "Apaneca", "El Boquerón"],
                    "Ethiopia": ["Guji","Idamo  Ethiopia","Ethiopia Woreda", "Ern Ethiopia", "Oromia", "Ethiopia  Ethiopia", "Workasakaro", "Arbegona", "Idamo  Ethiopia", "Ethiopia Woreda", "Benchmaji", "Limu Woreda", "Gedeo", "Ethiopia Ethiopia", "Agaro Gera", "Bombe Mountains", "Jimma", "Yirgacheffe", "Ethiopia", "Sidamo (Also Sidama)", "Sidama", "Sidamo", "Gedeb", "Odo Shakiso", "Kochere", "Bench-Maji", "Hambela Wamena", "Djimma", "Hambela"],
                    "France":["Biollet"],
                    "Guatemala": ["Antigua","Lake Atitln", "Fraijanes Plateau", "San Martin Jilotepeque", "Guatemala", "Huehuetenango", "Acatenango", "Chimaltenango", "Cobán", "Suchitan", "El Progresso"],
                    "Hawai'i":["Big Island Of Hawai'I","Holualoa","Hawaii","Hawai'Iai","Big Island Of Hawai'I", "Big Island Of Hawaii","Kealakekua", "Kainaliu", "Kainaliu", "Kalaheo", "Kau", "Ka'U", "Hawai'i", "Kona", "Ka’U", "Captain Cook", "Puna"],
                    "Honduras":["Marcala","Comayagua", "Honduras", "Siguatepeque"],
                    "Indonesia":["Lintong","Ern Indonesia","Sulawesi", "Simalungun","Indonesia  Indonesia", "Indonesia", "Aceh", "Sumatra" ,"Gayo", "Java", "Toraja"],
                    "Italy":["Panchia"],
                    "Japan":["Uraga"],
                    "Kenya":["Nyeri", "Central Kenya", "Kericho", "Gichugu", "Kirinyaga", "Kenya", "South-Central Kenya", "Kiambu", "Murang'A", "Embu", "Thika", "Muranga", "Nakuru"],
                    "Mexico":["Mexico", "Chiapas", "Veracruz", "Oaxaca", "Pluma Hidalgo"],
                    "Myanmar":["Muhinga"],
                    "Nepal":["Bhirkune", "Nuwakot"],
                    "Nicaragua":["Matagalpa", "Nueva Segovia", "Jinotega"],
                    "Palestine":["Palestina"],
                    "Panama":["Boquete","Panamai","Far Ern Panama","Chiriqu", "Ern Panama", "Panama", "Chiriqui", "Piedra Candela", "Alto Quiel", "Jaramillo"],
                    "Papua New Guinea":["Papua New Guinea", "Ainantu", "Kabiufa"],
                    "Peru":["Peru","Satipo","Chirinos","Ern Peru", "Pasco","Cusco", "Cajamarca", "Utcubamba", "Trujillo", "Tabaconas"],
                    "Philippines":["Benguet", "Sierra Madre"],
                    "Rwanda":["Nyamasheke", "Huye", "Rulindo", "Rustiro", "Gikongoro", "Rwanda", "Gakenke", "Muhanga", "Nyamagabe"],
                    "Spain":["Loja", "Algeciras", "Palencia", "Santander"],
                    "Taiwan":["Alishan", "Chiayi"],
                    "Tanzania":["Tarime", "Ngorongoro"],
                    "Thailand":["Chiang Rai", "Thailand", "Tha Sae", "Chumphon"],
                    "Uganda":["Sipi Falls", "Bugisu"],
                    "United States": ["Santa Barbara","United S","United Se","United Statestates","United S", "United Statese", "El Diamante", "San Jos", "Los Altos", "San Jose", "Santa Brbara", "Santa Ana", "Villa Rica"],
                    "Yemen":["Al Hayma","Al Mashtal Ul Burhani","Yemen Governorate", "Yemen", "Bani Matar", "Haraaz", "Sana’A", "Sanaa"],
                    "Zambia":["Zambia"]
                    }
# helper function to fix text
def fix_text(df, col):
    df[col] = df[col].str.lower()
    df[col] = df[col].str.replace("[^A-Za-z' ]","", regex=True)
    df[col] = df[col].str.replace("\t","").str.replace("\n", "").str.replace("\r", "")
    df[col] = df[col].str.strip()
    df[col] = df[col].str.title()
    return df

# function to remove the regions that appear less than 2 times
def remove_regions(df, col):
    to_remove = ["Zone", "State", "Growing Region", "Growing", "Prefecture", "Region", "Division", "Village", "City", "Town", "Province", "Department", "District", "Also", "South", "West", "North", "East", "Central", "North-Western", "North-Eastern", "South-Western", "South-Eastern", "Western", "Eastern", "County", "Africe", "America", "Valley"]

    df = fix_text(df, col)
    
    #remove location specifiers like "zone", "village", "prefecture", etc.
    for i in to_remove:
        df[col] = df[col].replace(i, "", regex=True)

    return df

def replace_regions(df, col, dict):
    for key, values in dict.items():
        for items in values:
            df[col] = df[col].str.replace(items, key, regex=True)
    return df

def regions_to_countries(df, col,dict):
    to_remove = ["Africa","Blue Pine Forest", "Jan","Mara", "Kabuye","Snnp", "Lincong","Ern Highlands", "Ern", "Congonama", "Ern Highlands", "NaN", "Nan", "", "Yeri", "Volcan", "Wood", "Llayla", "Plateau", "Cobn", "Mathira", "Ka", "Tarraz"]
    
    df = remove_regions(df, col)
    df = replace_regions(df, col, dict)
    df = fix_text(df, col)
    
    df.drop(df[df[col].isin(to_remove)].index, inplace=True)
    return df

for _ in range(3):
    dataset = regions_to_countries(dataset, "origin_2", regions)
    dataset = regions_to_countries(dataset, "origin_1", regions)


dataset[dataset["origin_1"]=="United S"] = "United States"
dataset[dataset["origin_1"]=="United Statestatese"] = "United States"
dataset[dataset["origin_1"] == "United Statestates"] = "United States"
dataset[dataset["origin_2"] == "United Statestates"] = "United States"



different_origins = dataset[dataset["origin_1"]!=dataset["origin_2"]]
dataset.drop(different_origins.index, axis=0, inplace=True)
dataset.drop(["origin_2"], axis=1, inplace=True)
dataset.rename(columns={"origin_1":"origin"})



dataset.drop(["desc_3", "desc_2"], axis=1, inplace=True)
dataset.rename(columns={"desc_1":"review"})