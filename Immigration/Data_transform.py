import os
import datetime

class Data_dictionary:

    '''A class that contains all dictionaries and functions needed to transform the data

    '''
    data_dict = {
    'cit_res' : {
    '582.0': 'MEXICO Air Sea, and Not Reported (I-94, no land arrivals)',
    '236.0': 'AFGHANISTAN',
    '101.0': 'ALBANIA',
    '316.0': 'ALGERIA',
    '102.0': 'ANDORRA',
    '324.0': 'ANGOLA',
    '529.0': 'ANGUILLA',
    '518.0': 'ANTIGUA-BARBUDA',
    '687.0': 'ARGENTINA ',
    '151.0': 'ARMENIA',
    '532.0': 'ARUBA',
    '438.0': 'AUSTRALIA',
    '103.0': 'AUSTRIA',
    '152.0': 'AZERBAIJAN',
    '512.0': 'BAHAMAS',
    '298.0': 'BAHRAIN',
    '274.0': 'BANGLADESH',
    '513.0': 'BARBADOS',
    '104.0': 'BELGIUM',
    '581.0': 'BELIZE',
    '386.0': 'BENIN',
    '509.0': 'BERMUDA',
    '153.0': 'BELARUS',
    '242.0': 'BHUTAN',
    '688.0': 'BOLIVIA',
    '717.0': 'BONAIRE, ST EUSTATIUS, SABA',
    '164.0': 'BOSNIA-HERZEGOVINA',
    '336.0': 'BOTSWANA',
    '689.0': 'BRAZIL',
    '525.0': 'BRITISH VIRGIN ISLANDS',
    '217.0': 'BRUNEI',
    '105.0': 'BULGARIA',
    '393.0': 'BURKINA FASO',
    '243.0': 'BURMA',
    '375.0': 'BURUNDI',
    '310.0': 'CAMEROON',
    '326.0': 'CAPE VERDE',
    '526.0': 'CAYMAN ISLANDS',
    '383.0': 'CENTRAL AFRICAN REPUBLIC',
    '384.0': 'CHAD',
    '690.0': 'CHILE',
    '245.0': 'CHINA, PRC',
    '721.0': 'CURACAO',
    '270.0': 'CHRISTMAS ISLAND',
    '271.0': 'COCOS ISLANDS',
    '691.0': 'COLOMBIA',
    '317.0': 'COMOROS',
    '385.0': 'CONGO',
    '467.0': 'COOK ISLANDS',
    '575.0': 'COSTA RICA',
    '165.0': 'CROATIA',
    '584.0': 'CUBA',
    '218.0': 'CYPRUS',
    '140.0': 'CZECH REPUBLIC',
    '723.0': 'FAROE ISLANDS (PART OF DENMARK)',
    '108.0': 'DENMARK',
    '322.0': 'DJIBOUTI',
    '519.0': 'DOMINICA',
    '585.0': 'DOMINICAN REPUBLIC',
    '240.0': 'EAST TIMOR',
    '692.0': 'ECUADOR',
    '368.0': 'EGYPT',
    '576.0': 'EL SALVADOR',
    '399.0': 'EQUATORIAL GUINEA',
    '372.0': 'ERITREA',
    '109.0': 'ESTONIA',
    '369.0': 'ETHIOPIA',
    '604.0': 'FALKLAND ISLANDS',
    '413.0': 'FIJI',
    '110.0': 'FINLAND',
    '111.0': 'FRANCE',
    '601.0': 'FRENCH GUIANA',
    '411.0': 'FRENCH POLYNESIA',
    '387.0': 'GABON',
    '338.0': 'GAMBIA',
    '758.0': 'GAZA STRIP',
    '154.0': 'GEORGIA',
    '112.0': 'GERMANY',
    '339.0': 'GHANA',
    '143.0': 'GIBRALTAR',
    '113.0': 'GREECE',
    '520.0': 'GRENADA',
    '507.0': 'GUADELOUPE',
    '577.0': 'GUATEMALA',
    '382.0': 'GUINEA',
    '327.0': 'GUINEA-BISSAU',
    '603.0': 'GUYANA',
    '586.0': 'HAITI',
    '726.0': 'HEARD AND MCDONALD IS.',
    '149.0': 'HOLY SEE/VATICAN',
    '528.0': 'HONDURAS',
    '206.0': 'HONG KONG',
    '114.0': 'HUNGARY',
    '115.0': 'ICELAND',
    '213.0': 'INDIA',
    '759.0': 'INDIAN OCEAN AREAS (FRENCH)',
    '729.0': 'INDIAN OCEAN TERRITORY',
    '204.0': 'INDONESIA',
    '249.0': 'IRAN',
    '250.0': 'IRAQ',
    '116.0': 'IRELAND',
    '251.0': 'ISRAEL',
    '117.0': 'ITALY',
    '388.0': 'IVORY COAST',
    '514.0': 'JAMAICA',
    '209.0': 'JAPAN',
    '253.0': 'JORDAN',
    '201.0': 'KAMPUCHEA',
    '155.0': 'KAZAKHSTAN',
    '340.0': 'KENYA',
    '414.0': 'KIRIBATI',
    '732.0': 'KOSOVO',
    '272.0': 'KUWAIT',
    '156.0': 'KYRGYZSTAN',
    '203.0': 'LAOS',
    '118.0': 'LATVIA',
    '255.0': 'LEBANON',
    '335.0': 'LESOTHO',
    '370.0': 'LIBERIA',
    '381.0': 'LIBYA',
    '119.0': 'LIECHTENSTEIN',
    '120.0': 'LITHUANIA',
    '121.0': 'LUXEMBOURG',
    '214.0': 'MACAU',
    '167.0': 'MACEDONIA',
    '320.0': 'MADAGASCAR',
    '345.0': 'MALAWI',
    '273.0': 'MALAYSIA',
    '220.0': 'MALDIVES',
    '392.0': 'MALI',
    '145.0': 'MALTA',
    '472.0': 'MARSHALL ISLANDS',
    '511.0': 'MARTINIQUE',
    '389.0': 'MAURITANIA',
    '342.0': 'MAURITIUS',
    '760.0': 'MAYOTTE (AFRICA - FRENCH)',
    '473.0': 'MICRONESIA, FED. STATES OF',
    '157.0': 'MOLDOVA',
    '122.0': 'MONACO',
    '299.0': 'MONGOLIA',
    '735.0': 'MONTENEGRO',
    '521.0': 'MONTSERRAT',
    '332.0': 'MOROCCO',
    '329.0': 'MOZAMBIQUE',
    '371.0': 'NAMIBIA',
    '440.0': 'NAURU',
    '257.0': 'NEPAL',
    '123.0': 'NETHERLANDS',
    '508.0': 'NETHERLANDS ANTILLES',
    '409.0': 'NEW CALEDONIA',
    '464.0': 'NEW ZEALAND',
    '579.0': 'NICARAGUA',
    '390.0': 'NIGER',
    '343.0': 'NIGERIA',
    '470.0': 'NIUE',
    '275.0': 'NORTH KOREA',
    '124.0': 'NORWAY',
    '256.0': 'OMAN',
    '258.0': 'PAKISTAN',
    '474.0': 'PALAU',
    '743.0': 'PALESTINE',
    '504.0': 'PANAMA',
    '441.0': 'PAPUA NEW GUINEA',
    '693.0': 'PARAGUAY',
    '694.0': 'PERU',
    '260.0': 'PHILIPPINES',
    '416.0': 'PITCAIRN ISLANDS',
    '107.0': 'POLAND',
    '126.0': 'PORTUGAL',
    '297.0': 'QATAR',
    '748.0': 'REPUBLIC OF SOUTH SUDAN',
    '321.0': 'REUNION',
    '127.0': 'ROMANIA',
    '158.0': 'RUSSIA',
    '376.0': 'RWANDA',
    '128.0': 'SAN MARINO',
    '330.0': 'SAO TOME AND PRINCIPE',
    '261.0': 'SAUDI ARABIA',
    '391.0': 'SENEGAL',
    '142.0': 'SERBIA AND MONTENEGRO',
    '745.0': 'SERBIA',
    '347.0': 'SEYCHELLES',
    '348.0': 'SIERRA LEONE',
    '207.0': 'SINGAPORE',
    '141.0': 'SLOVAKIA',
    '166.0': 'SLOVENIA',
    '412.0': 'SOLOMON ISLANDS',
    '397.0': 'SOMALIA',
    '373.0': 'SOUTH AFRICA',
    '276.0': 'SOUTH KOREA',
    '129.0': 'SPAIN',
    '244.0': 'SRI LANKA',
    '346.0': 'ST. HELENA',
    '522.0': 'ST. KITTS-NEVIS',
    '523.0': 'ST. LUCIA',
    '502.0': 'ST. PIERRE AND MIQUELON',
    '524.0': 'ST. VINCENT-GRENADINES',
    '716.0': 'SAINT BARTHELEMY',
    '736.0': 'SAINT MARTIN',
    '749.0': 'SAINT MAARTEN',
    '350.0': 'SUDAN',
    '602.0': 'SURINAME',
    '351.0': 'SWAZILAND',
    '130.0': 'SWEDEN',
    '131.0': 'SWITZERLAND',
    '262.0': 'SYRIA',
    '268.0': 'TAIWAN',
    '159.0': 'TAJIKISTAN',
    '353.0': 'TANZANIA',
    '263.0': 'THAILAND',
    '304.0': 'TOGO',
    '417.0': 'TONGA',
    '516.0': 'TRINIDAD AND TOBAGO',
    '323.0': 'TUNISIA',
    '264.0': 'TURKEY',
    '161.0': 'TURKMENISTAN',
    '527.0': 'TURKS AND CAICOS ISLANDS',
    '420.0': 'TUVALU',
    '352.0': 'UGANDA',
    '162.0': 'UKRAINE',
    '296.0': 'UNITED ARAB EMIRATES',
    '135.0': 'UNITED KINGDOM',
    '695.0': 'URUGUAY',
    '163.0': 'UZBEKISTAN',
    '410.0': 'VANUATU',
    '696.0': 'VENEZUELA',
    '266.0': 'VIETNAM',
    '469.0': 'WALLIS AND FUTUNA ISLANDS',
    '757.0': 'WEST INDIES (FRENCH)',
    '333.0': 'WESTERN SAHARA',
    '465.0': 'WESTERN SAMOA',
    '216.0': 'YEMEN',
    '139.0': 'YUGOSLAVIA',
    '301.0': 'ZAIRE',
    '344.0': 'ZAMBIA',
    '315.0': 'ZIMBABWE',
    '403.0': 'INVALID: AMERICAN SAMOA',
    '712.0': 'INVALID: ANTARCTICA',
    '700.0': 'INVALID: BORN ON BOARD SHIP',
    '719.0': 'INVALID: BOUVET ISLAND (ANTARCTICA/NORWAY TERR.)',
    '574.0': 'INVALID: CANADA',
    '720.0': 'INVALID: CANTON AND ENDERBURY ISLS',
    '106.0': 'INVALID: CZECHOSLOVAKIA',
    '739.0': 'INVALID: DRONNING MAUD LAND (ANTARCTICA-NORWAY)',
    '394.0': 'INVALID: FRENCH SOUTHERN AND ANTARCTIC',
    '501.0': 'INVALID: GREENLAND',
    '404.0': 'INVALID: GUAM',
    '730.0': 'INVALID: INTERNATIONAL WATERS',
    '731.0': 'INVALID: JOHNSON ISLAND',
    '471.0': 'INVALID: MARIANA ISLANDS, NORTHERN',
    '737.0': 'INVALID: MIDWAY ISLANDS',
    '753.0': 'INVALID: MINOR OUTLYING ISLANDS - USA',
    '740.0': 'INVALID: NEUTRAL ZONE (S. ARABIA/IRAQ)',
    '710.0': 'INVALID: NON-QUOTA IMMIGRANT',
    '505.0': 'INVALID: PUERTO RICO',
    '0.0': 'INVALID: STATELESS',
    '705.0': 'INVALID: STATELESS',
    '583.0': 'INVALID: UNITED STATES',
    '407.0': 'INVALID: UNITED STATES',
    '999.0': 'INVALID: UNKNOWN',
    '239.0': 'INVALID: UNKNOWN COUNTRY',
    '134.0': 'INVALID: USSR',
    '506.0': 'INVALID: U.S. VIRGIN ISLANDS',
    '755.0': 'INVALID: WAKE ISLAND',
    '311.0': 'Collapsed Tanzania (should not show)',
    '741.0': 'Collapsed Curacao (should not show)',
    '54.0': 'No Country Code (54)',
    '100.0': 'No Country Code (100)',
    '187.0': 'No Country Code (187)',
    '190.0': 'No Country Code (190)',
    '200.0': 'No Country Code (200)',
    '219.0': 'No Country Code (219)',
    '238.0': 'No Country Code (238)',
    '277.0': 'No Country Code (277)',
    '293.0': 'No Country Code (293)',
    '300.0': 'No Country Code (300)',
    '319.0': 'No Country Code (319)',
    '365.0': 'No Country Code (365)',
    '395.0': 'No Country Code (395)',
    '400.0': 'No Country Code (400)',
    '485.0': 'No Country Code (485)',
    '503.0': 'No Country Code (503)',
    '589.0': 'No Country Code (589)',
    '592.0': 'No Country Code (592)',
    '791.0': 'No Country Code (791)',
    '849.0': 'No Country Code (849)',
    '914.0': 'No Country Code (914)',
    '944.0': 'No Country Code (944)',
    '996.0': 'No Country Code (996)'},

    'port' : {
    'ALC': 'ALCAN, AK',
    'ANC': 'ANCHORAGE, AK',
    'BAR': 'BAKER AAF - BAKER ISLAND, AK',
    'DAC': 'DALTONS CACHE, AK',
    'PIZ': 'DEW STATION PT LAY DEW, AK',
    'DTH': 'DUTCH HARBOR, AK',
    'EGL': 'EAGLE, AK',
    'FRB': 'FAIRBANKS, AK',
    'HOM': 'HOMER, AK',
    'HYD': 'HYDER, AK',
    'JUN': 'JUNEAU, AK',
    '5KE': 'KETCHIKAN, AK',
    'KET': 'KETCHIKAN, AK',
    'MOS': 'MOSES POINT INTERMEDIATE, AK',
    'NIK': 'NIKISKI, AK',
    'NOM': 'NOM, AK',
    'PKC': 'POKER CREEK, AK',
    'ORI': 'PORT LIONS SPB, AK',
    'SKA': 'SKAGWAY, AK',
    'SNP': 'ST. PAUL ISLAND, AK',
    'TKI': 'TOKEEN, AK',
    'WRA': 'WRANGELL, AK',
    'HSV': 'MADISON COUNTY - HUNTSVILLE, AL',
    'MOB': 'MOBILE, AL',
    'LIA': 'LITTLE ROCK, AR (BPS)',
    'ROG': 'ROGERS ARPT, AR',
    'DOU': 'DOUGLAS, AZ',
    'LUK': 'LUKEVILLE, AZ',
    'MAP': 'MARIPOSA AZ',
    'NAC': 'NACO, AZ',
    'NOG': 'NOGALES, AZ',
    'PHO': 'PHOENIX, AZ',
    'POR': 'PORTAL, AZ',
    'SLU': 'SAN LUIS, AZ',
    'SAS': 'SASABE, AZ',
    'TUC': 'TUCSON, AZ',
    'YUI': 'YUMA, AZ',
    'AND': 'ANDRADE, CA',
    'BUR': 'BURBANK, CA',
    'CAL': 'CALEXICO, CA',
    'CAO': 'CAMPO, CA',
    'FRE': 'FRESNO, CA',
    'ICP': 'IMPERIAL COUNTY, CA',
    'LNB': 'LONG BEACH, CA',
    'LOS': 'LOS ANGELES, CA',
    'BFL': 'MEADOWS FIELD - BAKERSFIELD, CA',
    'OAK': 'OAKLAND, CA',
    'ONT': 'ONTARIO, CA',
    'OTM': 'OTAY MESA, CA',
    'BLT': 'PACIFIC, HWY. STATION, CA',
    'PSP': 'PALM SPRINGS, CA',
    'SAC': 'SACRAMENTO, CA',
    'SLS': 'SALINAS, CA (BPS)',
    'SDP': 'SAN DIEGO, CA',
    'SFR': 'SAN FRANCISCO, CA',
    'SNJ': 'SAN JOSE, CA',
    'SLO': 'SAN LUIS OBISPO, CA',
    'SLI': 'SAN LUIS OBISPO, CA (BPS)',
    'SPC': 'SAN PEDRO, CA',
    'SYS': 'SAN YSIDRO, CA',
    'SAA': 'SANTA ANA, CA',
    'STO': 'STOCKTON, CA (BPS)',
    'TEC': 'TECATE, CA',
    'TRV': 'TRAVIS-AFB, CA',
    'APA': 'ARAPAHOE COUNTY, CO',
    'ASE': 'ASPEN, CO #ARPT',
    'COS': 'COLORADO SPRINGS, CO',
    'DEN': 'DENVER, CO',
    'DRO': 'LA PLATA - DURANGO, CO',
    'BDL': 'BRADLEY INTERNATIONAL, CT',
    'BGC': 'BRIDGEPORT, CT',
    'GRT': 'GROTON, CT',
    'HAR': 'HARTFORD, CT',
    'NWH': 'NEW HAVEN, CT',
    'NWL': 'NEW LONDON, CT',
    'TST': 'NEWINGTON DATA CENTER TEST, CT',
    'WAS': 'WASHINGTON DC',
    'DOV': 'DOVER AFB, DE',
    'DVD': 'DOVER-AFB, DE',
    'WLL': 'WILMINGTON, DE',
    'BOC': 'BOCAGRANDE, FL',
    'SRQ': 'BRADENTON - SARASOTA, FL',
    'CAN': 'CAPE CANAVERAL, FL',
    'DAB': 'DAYTONA BEACH INTERNATIONAL, FL',
    'FRN': 'FERNANDINA, FL',
    'FTL': 'FORT LAUDERDALE, FL',
    'FMY': 'FORT MYERS, FL',
    'FPF': 'FORT PIERCE, FL',
    'HUR': 'HURLBURT FIELD, FL',
    'GNV': 'J R ALISON MUNI - GAINESVILLE, FL',
    'JAC': 'JACKSONVILLE, FL',
    'KEY': 'KEY WEST, FL',
    'LEE': 'LEESBURG MUNICIPAL AIRPORT, FL',
    'MLB': 'MELBOURNE, FL',
    'MIA': 'MIAMI, FL',
    'APF': 'NAPLES, FL #ARPT',
    'OPF': 'OPA LOCKA, FL',
    'ORL': 'ORLANDO, FL',
    'PAN': 'PANAMA CITY, FL',
    'PEN': 'PENSACOLA, FL',
    'PCF': 'PORT CANAVERAL, FL',
    'PEV': 'PORT EVERGLADES, FL',
    'PSJ': 'PORT ST JOE, FL',
    'SFB': 'SANFORD, FL',
    'SGJ': 'ST AUGUSTINE ARPT, FL',
    'SAU': 'ST AUGUSTINE, FL',
    'FPR': 'ST LUCIE COUNTY, FL',
    'SPE': 'ST PETERSBURG, FL',
    'TAM': 'TAMPA, FL',
    'WPB': 'WEST PALM BEACH, FL',
    'ATL': 'ATLANTA, GA',
    'BRU': 'BRUNSWICK, GA',
    'AGS': 'BUSH FIELD - AUGUSTA, GA',
    'SAV': 'SAVANNAH, GA',
    'AGA': 'AGANA, GU',
    'HHW': 'HONOLULU, HI',
    'OGG': 'KAHULUI - MAUI, HI',
    'KOA': 'KEAHOLE-KONA, HI',
    'LIH': 'LIHUE, HI',
    'CID': 'CEDAR RAPIDS/IOWA CITY, IA',
    'DSM': 'DES MOINES, IA',
    'BOI': 'AIR TERM. (GOWEN FLD) BOISE, ID',
    'EPI': 'EASTPORT, ID',
    'IDA': 'FANNING FIELD - IDAHO FALLS, ID',
    'PTL': 'PORTHILL, ID',
    'SPI': 'CAPITAL - SPRINGFIELD, IL',
    'CHI': 'CHICAGO, IL',
    'DPA': 'DUPAGE COUNTY, IL',
    'PIA': 'GREATER PEORIA, IL',
    'RFD': 'GREATER ROCKFORD, IL',
    'UGN': 'MEMORIAL - WAUKEGAN, IL',
    'GAR': 'GARY, IN',
    'HMM': 'HAMMOND, IN',
    'INP': 'INDIANAPOLIS, IN',
    'MRL': 'MERRILLVILLE, IN',
    'SBN': 'SOUTH BEND, IN',
    'ICT': 'MID-CONTINENT - WITCHITA, KS',
    'LEX': 'BLUE GRASS - LEXINGTON, KY',
    'LOU': 'LOUISVILLE, KY',
    'BTN': 'BATON ROUGE, LA',
    'LKC': 'LAKE CHARLES, LA',
    'LAK': 'LAKE CHARLES, LA (BPS)',
    'MLU': 'MONROE, LA',
    'MGC': 'MORGAN CITY, LA',
    'NOL': 'NEW ORLEANS, LA',
    'BOS': 'BOSTON, MA',
    'GLO': 'GLOUCESTER, MA',
    'BED': 'HANSCOM FIELD - BEDFORD, MA',
    'LYN': 'LYNDEN, WA',
    'ADW': 'ANDREWS AFB, MD',
    'BAL': 'BALTIMORE, MD',
    'MKG': 'MUSKEGON, MD',
    'PAX': 'PATUXENT RIVER, MD',
    'BGM': 'BANGOR, ME',
    'BOO': 'BOOTHBAY HARBOR, ME',
    'BWM': 'BRIDGEWATER, ME',
    'BCK': 'BUCKPORT, ME',
    'CLS': 'CALAIS, ME',
    'CRB': 'CARIBOU, ME',
    'COB': 'COBURN GORE, ME',
    'EST': 'EASTCOURT, ME',
    'EPT': 'EASTPORT MUNICIPAL, ME',
    'EPM': 'EASTPORT, ME',
    'FOR': 'FOREST CITY, ME',
    'FTF': 'FORT FAIRFIELD, ME',
    'FTK': 'FORT KENT, ME',
    'HML': 'HAMIIN, ME',
    'HTM': 'HOULTON, ME',
    'JKM': 'JACKMAN, ME',
    'KAL': 'KALISPEL, MT',
    'LIM': 'LIMESTONE, ME',
    'LUB': 'LUBEC, ME',
    'MAD': 'MADAWASKA, ME',
    'POM': 'PORTLAND, ME',
    'RGM': 'RANGELEY, ME (BPS)',
    'SBR': 'SOUTH BREWER, ME',
    'SRL': 'ST AURELIE, ME',
    'SPA': 'ST PAMPILE, ME',
    'VNB': 'VAN BUREN, ME',
    'VCB': 'VANCEBORO, ME',
    'AGN': 'ALGONAC, MI',
    'ALP': 'ALPENA, MI',
    'BCY': 'BAY CITY, MI',
    'DET': 'DETROIT, MI',
    'GRP': 'GRAND RAPIDS, MI',
    'GRO': 'GROSSE ISLE, MI',
    'ISL': 'ISLE ROYALE, MI',
    'MRC': 'MARINE CITY, MI',
    'MRY': 'MARYSVILLE, MI',
    'PTK': 'OAKLAND COUNTY - PONTIAC, MI',
    'PHU': 'PORT HURON, MI',
    'RBT': 'ROBERTS LANDING, MI',
    'SAG': 'SAGINAW, MI',
    'SSM': 'SAULT STE. MARIE, MI',
    'SCL': 'ST CLAIR, MI',
    'YIP': 'WILLOW RUN - YPSILANTI, MI',
    'BAU': 'BAUDETTE, MN',
    'CAR': 'CARIBOU MUNICIPAL AIRPORT, MN',
    'GTF': 'Collapsed into INT, MN',
    'INL': 'Collapsed into INT, MN',
    'CRA': 'CRANE LAKE, MN',
    'MIC': 'CRYSTAL MUNICIPAL AIRPORT, MN',
    'DUL': 'DULUTH, MN',
    'ELY': 'ELY, MN',
    'GPM': 'GRAND PORTAGE, MN',
    'SVC': 'GRANT COUNTY - SILVER CITY, MN',
    'INT': "INT''L FALLS, MN",
    'LAN': 'LANCASTER, MN',
    'MSP': 'MINN./ST PAUL, MN',
    'LIN': 'NORTHERN SVC CENTER, MN',
    'NOY': 'NOYES, MN',
    'PIN': 'PINE CREEK, MN',
    '48Y': 'PINECREEK BORDER ARPT, MN',
    'RAN': 'RAINER, MN',
    'RST': 'ROCHESTER, MN',
    'ROS': 'ROSEAU, MN',
    'SPM': 'ST PAUL, MN',
    'WSB': 'WARROAD INTL, SPB, MN',
    'WAR': 'WARROAD, MN',
    'KAN': 'KANSAS CITY, MO',
    'SGF': 'SPRINGFIELD-BRANSON, MO',
    'STL': 'ST LOUIS, MO',
    'WHI': 'WHITETAIL, MT',
    'WHM': 'WILD HORSE, MT',
    'GPT': 'BILOXI REGIONAL, MS',
    'GTR': 'GOLDEN TRIANGLE LOWNDES CNTY, MS',
    'GUL': 'GULFPORT, MS',
    'PAS': 'PASCAGOULA, MS',
    'JAN': 'THOMPSON FIELD - JACKSON, MS',
    'BIL': 'BILLINGS, MT',
    'BTM': 'BUTTE, MT',
    'CHF': 'CHIEF MT, MT',
    'CTB': 'CUT BANK MUNICIPAL, MT',
    'CUT': 'CUT BANK, MT',
    'DLB': 'DEL BONITA, MT',
    'EUR': 'EUREKA, MT (BPS)',
    'BZN': 'GALLATIN FIELD - BOZEMAN, MT',
    'FCA': 'GLACIER NATIONAL PARK, MT',
    'GGW': 'GLASGOW, MT',
    'GRE': 'GREAT FALLS, MT',
    'HVR': 'HAVRE, MT',
    'HEL': 'HELENA, MT',
    'LWT': 'LEWISTON, MT',
    'MGM': 'MORGAN, MT',
    'OPH': 'OPHEIM, MT',
    'PIE': 'PIEGAN, MT',
    'RAY': 'RAYMOND, MT',
    'ROO': 'ROOSVILLE, MT',
    'SCO': 'SCOBEY, MT',
    'SWE': 'SWEETGTASS, MT',
    'TRL': 'TRIAL CREEK, MT',
    'TUR': 'TURNER, MT',
    'WCM': 'WILLOW CREEK, MT',
    'CLT': 'CHARLOTTE, NC',
    'FAY': 'FAYETTEVILLE, NC',
    'MRH': 'MOREHEAD CITY, NC',
    'FOP': 'MORRIS FIELDS AAF, NC',
    'GSO': 'PIEDMONT TRIAD INTL AIRPORT, NC',
    'RDU': 'RALEIGH/DURHAM, NC',
    'SSC': 'SHAW AFB - SUMTER, NC',
    'WIL': 'WILMINGTON, NC',
    'AMB': 'AMBROSE, ND',
    'ANT': 'ANTLER, ND',
    'CRY': 'CARBURY, ND',
    'DNS': 'DUNSEITH, ND',
    'FAR': 'FARGO, ND',
    'FRT': 'FORTUNA, ND',
    'GRF': 'GRAND FORKS, ND',
    'HNN': 'HANNAH, ND',
    'HNS': 'HANSBORO, ND',
    'MAI': 'MAIDA, ND',
    'MND': 'MINOT, ND',
    'NEC': 'NECHE, ND',
    'NOO': 'NOONAN, ND',
    'NRG': 'NORTHGATE, ND',
    'PEM': 'PEMBINA, ND',
    'SAR': 'SARLES, ND',
    'SHR': 'SHERWOOD, ND',
    'SJO': 'ST JOHN, ND',
    'WAL': 'WALHALLA, ND',
    'WHO': 'WESTHOPE, ND',
    'WND': 'WILLISTON, ND',
    'OMA': 'OMAHA, NE',
    'LEB': 'LEBANON, NH',
    'MHT': 'MANCHESTER, NH',
    'PNH': 'PITTSBURG, NH',
    'PSM': 'PORTSMOUTH, NH',
    'BYO': 'BAYONNE, NJ',
    'CNJ': 'CAMDEN, NJ',
    'HOB': 'HOBOKEN, NJ',
    'JER': 'JERSEY CITY, NJ',
    'WRI': 'MC GUIRE AFB - WRIGHTSOWN, NJ',
    'MMU': 'MORRISTOWN, NJ',
    'NEW': 'NEWARK/TETERBORO, NJ',
    'PER': 'PERTH AMBOY, NJ',
    'ACY': 'POMONA FIELD - ATLANTIC CITY, NJ',
    'ALA': 'ALAMAGORDO, NM (BPS)',
    'ABQ': 'ALBUQUERQUE, NM',
    'ANP': 'ANTELOPE WELLS, NM',
    'CRL': 'CARLSBAD, NM',
    'COL': 'COLUMBUS, NM',
    'CDD': 'CRANE LAKE - ST. LOUIS CNTY, NM',
    'DNM': 'DEMING, NM (BPS)',
    'LAS': 'LAS CRUCES, NM',
    'LOB': 'LORDSBURG, NM (BPS)',
    'RUI': 'RUIDOSO, NM',
    'STR': 'SANTA TERESA, NM',
    'RNO': 'CANNON INTL - RENO/TAHOE, NV',
    'FLX': 'FALLON MUNICIPAL AIRPORT, NV',
    'LVG': 'LAS VEGAS, NV',
    'REN': 'RENO, NV',
    'ALB': 'ALBANY, NY',
    'AXB': 'ALEXANDRIA BAY, NY',
    'BUF': 'BUFFALO, NY',
    'CNH': 'CANNON CORNERS, NY',
    'CAP': 'CAPE VINCENT, NY',
    'CHM': 'CHAMPLAIN, NY',
    'CHT': 'CHATEAUGAY, NY',
    'CLA': 'CLAYTON, NY',
    'FTC': 'FORT COVINGTON, NY',
    'LAG': 'LA GUARDIA, NY',
    'LEW': 'LEWISTON, NY',
    'MAS': 'MASSENA, NY',
    'MAG': 'MCGUIRE AFB, NY',
    'MOO': 'MOORES, NY',
    'MRR': 'MORRISTOWN, NY',
    'NYC': 'NEW YORK, NY',
    'NIA': 'NIAGARA FALLS, NY',
    'OGD': 'OGDENSBURG, NY',
    'OSW': 'OSWEGO, NY',
    'ELM': 'REGIONAL ARPT - HORSEHEAD, NY',
    'ROC': 'ROCHESTER, NY',
    'ROU': 'ROUSES POINT, NY',
    'SWF': 'STEWART - ORANGE CNTY, NY',
    'SYR': 'SYRACUSE, NY',
    'THO': 'THOUSAND ISLAND BRIDGE, NY',
    'TRO': 'TROUT RIVER, NY',
    'WAT': 'WATERTOWN, NY',
    'HPN': 'WESTCHESTER - WHITE PLAINS, NY',
    'WRB': 'WHIRLPOOL BRIDGE, NY',
    'YOU': 'YOUNGSTOWN, NY',
    'AKR': 'AKRON, OH',
    'ATB': 'ASHTABULA, OH',
    'CIN': 'CINCINNATI, OH',
    'CLE': 'CLEVELAND, OH',
    'CLM': 'COLUMBUS, OH',
    'LOR': 'LORAIN, OH',
    'MBO': 'MARBLE HEADS, OH',
    'SDY': 'SANDUSKY, OH',
    'TOL': 'TOLEDO, OH',
    'OKC': 'OKLAHOMA CITY, OK',
    'TUL': 'TULSA, OK',
    'AST': 'ASTORIA, OR',
    'COO': 'COOS BAY, OR',
    'HIO': 'HILLSBORO, OR',
    'MED': 'MEDFORD, OR',
    'NPT': 'NEWPORT, OR',
    'POO': 'PORTLAND, OR',
    'PUT': 'PUT-IN-BAY, OH',
    'RDM': 'ROBERTS FIELDS - REDMOND, OR',
    'ERI': 'ERIE, PA',
    'MDT': 'HARRISBURG, PA',
    'HSB': 'HARRISONBURG, PA',
    'PHI': 'PHILADELPHIA, PA',
    'PIT': 'PITTSBURG, PA',
    'AGU': 'AGUADILLA, PR',
    'BQN': 'BORINQUEN - AGUADILLO, PR',
    'JCP': 'CULEBRA - BENJAMIN RIVERA, PR',
    'ENS': 'ENSENADA, PR',
    'FAJ': 'FAJARDO, PR',
    'HUM': 'HUMACAO, PR',
    'JOB': 'JOBOS, PR',
    'MAY': 'MAYAGUEZ, PR',
    'PON': 'PONCE, PR',
    'PSE': 'PONCE-MERCEDITA, PR',
    'SAJ': 'SAN JUAN, PR',
    'VQS': 'VIEQUES-ARPT, PR',
    'PRO': 'PROVIDENCE, RI',
    'PVD': 'THEODORE FRANCIS - WARWICK, RI',
    'CHL': 'CHARLESTON, SC',
    'CAE': 'COLUMBIA, SC #ARPT',
    'GEO': 'GEORGETOWN, SC',
    'GSP': 'GREENVILLE, SC',
    'GRR': 'GREER, SC',
    'MYR': 'MYRTLE BEACH, SC',
    'SPF': 'BLACK HILLS, SPEARFISH, SD',
    'HON': 'HOWES REGIONAL ARPT - HURON, SD',
    'SAI': 'SAIPAN, SPN',
    'TYS': 'MC GHEE TYSON - ALCOA, TN',
    'MEM': 'MEMPHIS, TN',
    'NSV': 'NASHVILLE, TN',
    'TRI': 'TRI CITY ARPT, TN',
    'ADS': 'ADDISON AIRPORT- ADDISON, TX',
    'ADT': 'AMISTAD DAM, TX',
    'ANZ': 'ANZALDUAS, TX',
    'AUS': 'AUSTIN, TX',
    'BEA': 'BEAUMONT, TX',
    'BBP': 'BIG BEND PARK, TX (BPS)',
    'SCC': 'BP SPEC COORD. CTR, TX',
    'BTC': 'BP TACTICAL UNIT, TX',
    'BOA': 'BRIDGE OF AMERICAS, TX',
    'BRO': 'BROWNSVILLE, TX',
    'CRP': 'CORPUS CHRISTI, TX',
    'DAL': 'DALLAS, TX',
    'DLR': 'DEL RIO, TX',
    'DNA': 'DONNA, TX',
    'EGP': 'EAGLE PASS, TX',
    'ELP': 'EL PASO, TX',
    'FAB': 'FABENS, TX',
    'FAL': 'FALCON HEIGHTS, TX',
    'FTH': 'FORT HANCOCK, TX',
    'AFW': 'FORT WORTH ALLIANCE, TX',
    'FPT': 'FREEPORT, TX',
    'GAL': 'GALVESTON, TX',
    'HLG': 'HARLINGEN, TX',
    'HID': 'HIDALGO, TX',
    'HOU': 'HOUSTON, TX',
    'SGR': 'HULL FIELD, SUGAR LAND ARPT, TX',
    'LLB': 'JUAREZ-LINCOLN BRIDGE, TX',
    'LCB': 'LAREDO COLUMBIA BRIDGE, TX',
    'LRN': 'LAREDO NORTH, TX',
    'LAR': 'LAREDO, TX',
    'LSE': 'LOS EBANOS, TX',
    'IND': 'LOS INDIOS, TX',
    'LOI': 'LOS INDIOS, TX',
    'MRS': 'MARFA, TX (BPS)',
    'MCA': 'MCALLEN, TX',
    'MAF': 'ODESSA REGIONAL, TX',
    'PDN': 'PASO DEL NORTE,TX',
    'PBB': 'PEACE BRIDGE, NY',
    'PHR': 'PHARR, TX',
    'PAR': 'PORT ARTHUR, TX',
    'ISB': 'PORT ISABEL, TX',
    'POE': 'PORT OF EL PASO, TX',
    'PRE': 'PRESIDIO, TX',
    'PGR': 'PROGRESO, TX',
    'RIO': 'RIO GRANDE CITY, TX',
    'ROM': 'ROMA, TX',
    'SNA': 'SAN ANTONIO, TX',
    'SNN': 'SANDERSON, TX',
    'VIB': 'VETERAN INTL BRIDGE, TX',
    'YSL': 'YSLETA, TX',
    'CHA': 'CHARLOTTE AMALIE, VI',
    'CHR': 'CHRISTIANSTED, VI',
    'CRU': 'CRUZ BAY, ST JOHN, VI',
    'FRK': 'FREDERIKSTED, VI',
    'STT': 'ST THOMAS, VI',
    'LGU': 'CACHE AIRPORT - LOGAN, UT',
    'SLC': 'SALT LAKE CITY, UT',
    'CHO': 'ALBEMARLE CHARLOTTESVILLE, VA',
    'DAA': 'DAVISON AAF - FAIRFAX CNTY, VA',
    'HOP': 'HOPEWELL, VA',
    'HEF': 'MANASSAS, VA #ARPT',
    'NWN': 'NEWPORT, VA',
    'NOR': 'NORFOLK, VA',
    'RCM': 'RICHMOND, VA',
    'ABS': 'ALBURG SPRINGS, VT',
    'ABG': 'ALBURG, VT',
    'BEB': 'BEEBE PLAIN, VT',
    'BEE': 'BEECHER FALLS, VT',
    'BRG': 'BURLINGTON, VT',
    'CNA': 'CANAAN, VT',
    'DER': 'DERBY LINE, VT (I-91)',
    'DLV': 'DERBY LINE, VT (RT. 5)',
    'ERC': 'EAST RICHFORD, VT',
    'HIG': 'HIGHGATE SPRINGS, VT',
    'MOR': 'MORSES LINE, VT',
    'NPV': 'NEWPORT, VT',
    'NRT': 'NORTH TROY, VT',
    'NRN': 'NORTON, VT',
    'PIV': 'PINNACLE ROAD, VT',
    'RIF': 'RICHFORT, VT',
    'STA': 'ST ALBANS, VT',
    'SWB': 'SWANTON, VT (BP - SECTOR HQ)',
    'WBE': 'WEST BERKSHIRE, VT',
    'ABE': 'ABERDEEN, WA',
    'ANA': 'ANACORTES, WA',
    'BEL': 'BELLINGHAM, WA',
    'BLI': 'BELLINGHAM, WASHINGTON #INTL',
    'BLA': 'BLAINE, WA',
    'BWA': 'BOUNDARY, WA',
    'CUR': 'CURLEW, WA (BPS)',
    'DVL': 'DANVILLE, WA',
    'EVE': 'EVERETT, WA',
    'FER': 'FERRY, WA',
    'FRI': 'FRIDAY HARBOR, WA',
    'FWA': 'FRONTIER, WA',
    'KLM': 'KALAMA, WA',
    'LAU': 'LAURIER, WA',
    'LON': 'LONGVIEW, WA',
    'MET': 'METALINE FALLS, WA',
    'MWH': 'MOSES LAKE GRANT COUNTY ARPT, WA',
    'NEA': 'NEAH BAY, WA',
    'NIG': 'NIGHTHAWK, WA',
    'OLY': 'OLYMPIA, WA',
    'ORO': 'OROVILLE, WA',
    'PWB': 'PASCO, WA',
    'PIR': 'POINT ROBERTS, WA',
    'PNG': 'PORT ANGELES, WA',
    'PTO': 'PORT TOWNSEND, WA',
    'SEA': 'SEATTLE, WA',
    'SPO': 'SPOKANE, WA',
    'SUM': 'SUMAS, WA',
    'TAC': 'TACOMA, WA',
    'PSC': 'TRI-CITIES - PASCO, WA',
    'VAN': 'VANCOUVER, WA',
    'AGM': 'ALGOMA, WI',
    'BAY': 'BAYFIELD, WI',
    'GRB': 'GREEN BAY, WI',
    'MNW': 'MANITOWOC, WI',
    'MIL': 'MILWAUKEE, WI',
    'MSN': 'TRUAX FIELD - DANE COUNTY, WI',
    'CHS': 'CHARLESTON, WV',
    'CLK': 'CLARKSBURG, WV',
    'BLF': 'MERCER COUNTY, WV',
    'CSP': 'CASPER, WY',
    'XXX': 'NOT REPORTED/UNKNOWN',
    '888': 'UNIDENTIFED AIR / SEAPORT',
    'UNK': 'UNKNOWN POE',
    'CLG': 'CALGARY, CANADA',
    'EDA': 'EDMONTON, CANADA',
    'YHC': 'HAKAI PASS, CANADA',
    'HAL': 'Halifax, NS, Canada',
    'MON': 'MONTREAL, CANADA',
    'OTT': 'OTTAWA, CANADA',
    'YXE': 'SASKATOON, CANADA',
    'TOR': 'TORONTO, CANADA',
    'VCV': 'VANCOUVER, CANADA',
    'VIC': 'VICTORIA, CANADA',
    'WIN': 'WINNIPEG, CANADA',
    'AMS': 'AMSTERDAM-SCHIPHOL, NETHERLANDS',
    'ARB': 'ARUBA, NETH ANTILLES',
    'BAN': 'BANKOK, THAILAND',
    'BEI': 'BEICA #ARPT, ETHIOPIA',
    'PEK': 'BEIJING CAPITAL INTL, PRC',
    'BDA': 'KINDLEY FIELD, BERMUDA',
    'BOG': 'BOGOTA, EL DORADO #ARPT, COLOMBIA',
    'EZE': 'BUENOS AIRES, MINISTRO PIST, ARGENTINA',
    'CUN': 'CANCUN, MEXICO',
    'CRQ': 'CARAVELAS, BA #ARPT, BRAZIL',
    'MVD': 'CARRASCO, URUGUAY',
    'DUB': 'DUBLIN, IRELAND',
    'FOU': 'FOUGAMOU #ARPT, GABON',
    'FBA': 'FREEPORT, BAHAMAS',
    'MTY': 'GEN M. ESCOBEDO, Monterrey, MX',
    'HMO': 'GEN PESQUEIRA GARCIA, MX',
    'GCM': 'GRAND CAYMAN, CAYMAN ISLAND',
    'GDL': 'GUADALAJARA, MIGUEL HIDAL, MX',
    'HAM': 'HAMILTON, BERMUDA',
    'ICN': 'INCHON, SEOUL KOREA',
    'IWA': 'INVALID - IWAKUNI, JAPAN',
    'CND': 'KOGALNICEANU, ROMANIA',
    'LAH': 'LABUHA ARPT, INDONESIA',
    'DUR': 'LOUIS BOTHA, SOUTH AFRICA',
    'MAL': 'MANGOLE ARPT, INDONESIA',
    'MDE': 'MEDELLIN, COLOMBIA',
    'MEX': 'JUAREZ INTL, MEXICO CITY, MX',
    'LHR': 'MIDDLESEX, ENGLAND',
    'NBO': 'NAIROBI, KENYA',
    'NAS': 'NASSAU, BAHAMAS',
    'NCA': 'NORTH CAICOS, TURK & CAIMAN',
    'PTY': 'OMAR TORRIJOS, PANAMA',
    'SPV': 'PAPUA, NEW GUINEA',
    'UIO': 'QUITO (MARISCAL SUCR), ECUADOR',
    'RIT': 'ROME, ITALY',
    'SNO': 'SAKON NAKHON #ARPT, THAILAND',
    'SLP': 'SAN LUIS POTOSI #ARPT, MEXICO',
    'SAN': 'SAN SALVADOR, EL SALVADOR',
    'SRO': 'SANTANA RAMOS #ARPT, COLOMBIA',
    'GRU': 'GUARULHOS INTL, SAO PAULO, BRAZIL',
    'SHA': 'SHANNON, IRELAND',
    'HIL': 'SHILLAVO, ETHIOPIA',
    'TOK': 'TOROKINA #ARPT, PAPUA, NEW GUINEA',
    'VER': 'VERACRUZ, MEXICO',
    'LGW': 'WEST SUSSEX, ENGLAND',
    'ZZZ': 'MEXICO Land (Banco de Mexico)',
    'CHN': 'No PORT Code (CHN)',
    'CNC': 'CANNON CORNERS, NY',
    'MAA': 'Abu Dhabi',
    'AG0': 'MAGNOLIA, AR',
    'BHM': 'BAR HARBOR, ME',
    'BHX': 'BIRMINGHAM, AL',
    'CAK': 'AKRON, OH',
    'FOK': 'SUFFOLK COUNTY, NY',
    'LND': 'LANDER, WY',
    'MAR': 'MARFA, TX',
    'MLI': 'MOLINE, IL',
    'RIV': 'RIVERSIDE, CA',
    'RME': 'ROME, NY',
    'VNY': 'VAN NUYS, CA',
    'YUM': 'YUMA, AZ',
    'FRG': 'Collapsed (FOK) 06/15',
    'HRL': 'Collapsed (HLG) 06/15',
    'ISP': 'Collapsed (FOK) 06/15',
    'JSJ': 'Collapsed (SAJ) 06/15',
    'BUS': 'Collapsed (BUF) 06/15',
    'IAG': 'Collapsed (NIA) 06/15',
    'PHN': 'Collapsed (PHU) 06/15',
    'STN': 'Collapsed (STR) 06/15',
    'VMB': 'Collapsed (VNB) 06/15',
    'T01': 'Collapsed (SEA) 06/15',
    'PHF': 'No PORT Code (PHF)',
    'DRV': 'No PORT Code (DRV)',
    'FTB': 'No PORT Code (FTB)',
    'GAC': 'No PORT Code (GAC)',
    'GMT': 'No PORT Code (GMT)',
    'JFA': 'No PORT Code (JFA)',
    'JMZ': 'No PORT Code (JMZ)',
    'NC8': 'No PORT Code (NC8)',
    'NYL': 'No PORT Code (NYL)',
    'OAI': 'No PORT Code (OAI)',
    'PCW': 'No PORT Code (PCW)',
    'WA5': 'No PORT Code (WAS)',
    'WTR': 'No PORT Code (WTR)',
    'X96': 'No PORT Code (X96)',
    'XNA': 'No PORT Code (XNA)',
    'YGF': 'No PORT Code (YGF)',
    '5T6': 'No PORT Code (5T6)',
    '060': 'No PORT Code (60)',
    'SP0': 'No PORT Code (SP0)',
    'W55': 'No PORT Code (W55)',
    'X44': 'No PORT Code (X44)',
    'AUH': 'No PORT Code (AUH)',
    'RYY': 'No PORT Code (RYY)',
    'SUS': 'No PORT Code (SUS)',
    '74S': 'No PORT Code (74S)',
    'ATW': 'No PORT Code (ATW)',
    'CPX': 'No PORT Code (CPX)',
    'MTH': 'No PORT Code (MTH)',
    'PFN': 'No PORT Code (PFN)',
    'SCH': 'No PORT Code (SCH)',
    'ASI': 'No PORT Code (ASI)',
    'BKF': 'No PORT Code (BKF)',
    'DAY': 'No PORT Code (DAY)',
    'Y62': 'No PORT Code (Y62)',
    'AG': 'No PORT Code (AG)',
    'BCM': 'No PORT Code (BCM)',
    'DEC': 'No PORT Code (DEC)',
    'PLB': 'No PORT Code (PLB)',
    'CXO': 'No PORT Code (CXO)',
    'JBQ': 'No PORT Code (JBQ)',
    'JIG': 'No PORT Code (JIG)',
    'OGS': 'No PORT Code (OGS)',
    'TIW': 'No PORT Code (TIW)',
    'OTS': 'No PORT Code (OTS)',
    'AMT': 'No PORT Code (AMT)',
    'EGE': 'No PORT Code (EGE)',
    'GPI': 'No PORT Code (GPI)',
    'NGL': 'No PORT Code (NGL)',
    'OLM': 'No PORT Code (OLM)',
    '.GA': 'No PORT Code (.GA)',
    'CLX': 'No PORT Code (CLX)',
    'CP': 'No PORT Code (CP)',
    'FSC': 'No PORT Code (FSC)',
    'NK': 'No PORT Code (NK)',
    'ADU': 'No PORT Code (ADU)',
    'AKT': 'No PORT Code (AKT)',
    'LIT': 'No PORT Code (LIT)',
    'A2A': 'No PORT Code (A2A)',
    'OSN': 'No PORT Code (OSN)'},

    'state' : {
    'AL' : 'ALABAMA',
    'AK': 'ALASKA',
    'AZ': 'ARIZONA',
    'AR': 'ARKANSAS',
    'CA': 'CALIFORNIA',
    'CO': 'COLORADO',
    'CT': 'CONNECTICUT',
    'DE': 'DELAWARE',
    'DC': 'DIST. OF COLUMBIA',
    'FL': 'FLORIDA',
    'GA': 'GEORGIA',
    'GU': 'GUAM',
    'HI': 'HAWAII',
    'ID': 'IDAHO',
    'IL': 'ILLINOIS',
    'IN': 'INDIANA',
    'IA': 'IOWA',
    'KS': 'KANSAS',
    'KY': 'KENTUCKY',
    'LA': 'LOUISIANA',
    'ME': 'MAINE',
    'MD': 'MARYLAND',
    'MA': 'MASSACHUSETTS',
    'MI': 'MICHIGAN',
    'MN': 'MINNESOTA',
    'MS': 'MISSISSIPPI',
    'MO': 'MISSOURI',
    'MT': 'MONTANA',
    'NC': 'N. CAROLINA',
    'ND': 'N. DAKOTA',
    'NE': 'NEBRASKA',
    'NV': 'NEVADA',
    'NH': 'NEW HAMPSHIRE',
    'NJ': 'NEW JERSEY',
    'NM': 'NEW MEXICO',
    'NY': 'NEW YORK',
    'OH': 'OHIO',
    'OK': 'OKLAHOMA',
    'OR': 'OREGON',
    'PA': 'PENNSYLVANIA',
    'PR': 'PUERTO RICO',
    'RI': 'RHODE ISLAND',
    'SC': 'S. CAROLINA',
    'SD': 'S. DAKOTA',
    'TN': 'TENNESSEE',
    'TX': 'TEXAS',
    'UT': 'UTAH',
    'VT': 'VERMONT',
    'VI': 'VIRGIN ISLANDS',
    'VA': 'VIRGINIA',
    'WV': 'W. VIRGINIA',
    'WA': 'WASHINGTON',
    'WI': 'WISCONSON',
    'WY': "WYOMING' ",
    '99': 'All Other Codes'},

    'purpose_of_stay':{
    '1.0':'Business',
    '2.0':'Pleasure',
    '3.0':'Student'},

    'column_names': {
    'Unnamed: 0': 'id',
    'cicid': 'cicid',
    'i94yr': 'i94_year',
    'i94mon': 'i94_month',
    'i94cit': 'i94_city',
    'i94res': 'i94_residence',
    'i94port': 'i94_port',
    'arrdate': 'arrival_date',
    'i94mode': 'travel_method',
    'i94addr': 'i94_state',
    'depdate': 'departure_date',
    'i94bir': 'age',
    'i94visa': 'purpose_of_stay',
    'count': 'count',
    'dtadfile': 'file_date_add',
    'visapost': 'visa_post',
    'occup': 'occupation',
    'entdepa': 'arrival_flag',
    'entdepd': 'departure_flag',
    'entdepu': 'update_flag',
    'matflag': 'match_flag',
    'biryear': 'birth_year',
    'dtaddto': 'admission_date',
    'gender': 'gender',
    'insnum': 'ins_number',
    'airline': 'airline',
    'admnum': 'admission_number',
    'fltno': 'flight_num',
    'visatype': 'visa_type'},

    'travel_method' : {
    '1.0':'Air',
    '2.0':'Sea',
    '3.0':'Land',
    '9.0':'Not Reported'},

    }


    #Create transformation functions for arr/dep date and admission_date


    def sas_date_days(date):
        epoch= datetime.datetime(1960,1,1)
        return (epoch + datetime.timedelta(days=date))

    def date_format_F(date):
        if date == 'D/S':
            return None
        else:
            return datetime.datetime.strptime(str(date), '%Y%m%d')

    def date_format_A(date):
        if date == 'D/S':
            return None
        else:
            return datetime.datetime.strptime(date, '%m%d%Y')

    def pooled_average(mean_dict):
        '''takes in a dictionary with sample size
        as the key and averages as the value and finds
        the pooled average of the means'''
        keys = list(mean_dict.keys())
        values = list(mean_dict.values())

        return np.dot(keys,values)/sum(keys)
