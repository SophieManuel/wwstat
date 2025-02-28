"""
ISO 2-digit and 3-digit country codes for data file validations.
"""

CC_2D = [
    'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM',
    'AW', 'AU', 'AT', 'AZ', 'BH', 'BS', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ',
    'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF',
    'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC',
    'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ',
    'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK',
    'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH',
    'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT',
    'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM',
    'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW',
    'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK',
    'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX',
    'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP',
    'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK',
    'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA',
    'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS',
    'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB',
    'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH',
    'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR',
    'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU',
    'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW',
]

CC_3D = [
    'AFG', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG', 'ARG',
    'ARM', 'ABW', 'AUS', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BRB', 'BLR',
    'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BOL', 'BIH', 'BWA', 'BVT',
    'BRA', 'IOT', 'BRN', 'BRN', 'BGR', 'BFA', 'BDI', 'KHM', 'CMR', 'CAN',
    'CPV', 'CYM', 'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK', 'COL', 'COM',
    'COG', 'COD', 'COK', 'CRI', 'CIV', 'CIV', 'HRV', 'CUB', 'CYP', 'CZE',
    'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST',
    'ETH', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF', 'ATF', 'GAB',
    'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL', 'GRD', 'GLP', 'GUM',
    'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'HMD', 'VAT', 'HND', 'HKG',
    'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ', 'IRL', 'IMN', 'ISR', 'ITA',
    'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 'KEN', 'KIR', 'PRK', 'KOR', 'KOR',
    'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LBY', 'LIE',
    'LTU', 'LUX', 'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI', 'MLT',
    'MHL', 'MTQ', 'MRT', 'MUS', 'MYT', 'MEX', 'FSM', 'MDA', 'MCO', 'MNG',
    'MNE', 'MSR', 'MAR', 'MOZ', 'MMR', 'MMR', 'NAM', 'NRU', 'NPL', 'NLD',
    'ANT', 'NCL', 'NZL', 'NIC', 'NER', 'NGA', 'NIU', 'NFK', 'MNP', 'NOR',
    'OMN', 'PAK', 'PLW', 'PSE', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'PCN',
    'POL', 'PRT', 'PRI', 'QAT', 'REU', 'ROU', 'RUS', 'RUS', 'RWA', 'SHN',
    'KNA', 'LCA', 'SPM', 'VCT', 'VCT', 'VCT', 'WSM', 'SMR', 'STP', 'SAU',
    'SEN', 'SRB', 'SYC', 'SLE', 'SGP', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF',
    'SGS', 'ESP', 'LKA', 'SDN', 'SUR', 'SJM', 'SWZ', 'SWE', 'CHE', 'SYR',
    'TWN', 'TWN', 'TJK', 'TZA', 'THA', 'TLS', 'TGO', 'TKL', 'TON', 'TTO',
    'TTO', 'TUN', 'TUR', 'TKM', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR',
    'USA', 'UMI', 'URY', 'UZB', 'VUT', 'VEN', 'VEN', 'VNM', 'VNM', 'VGB',
    'VIR', 'WLF', 'ESH', 'YEM', 'ZMB', 'ZWE', 'CHI', 'CUW', 'XKX', 'SXM',
    'SSD', 'MAF'
]

CC_NAMES = {
    "ABW": "Aruba",
    "AFG": "Afghanistan",
    "AGO": "Angola",
    "AIA": "Anguilla",
    "ALA": "Åland Islands",
    "ALB": "Albania",
    "AND": "Andorra",
    "ARE": "United Arab Emirates",
    "ARG": "Argentina",
    "ARM": "Armenia",
    "ASM": "American Samoa",
    "ATA": "Antarctica",
    "ATF": "French Southern Territories",
    "ATG": "Antigua and Barbuda",
    "AUS": "Australia",
    "AUT": "Austria",
    "AZE": "Azerbaijan",
    "BDI": "Burundi",
    "BEL": "Belgium",
    "BEN": "Benin",
    "BES": "Bonaire, Sint Eustatius and Saba",
    "BFA": "Burkina Faso",
    "BGD": "Bangladesh",
    "BGR": "Bulgaria",
    "BHR": "Bahrain",
    "BHS": "Bahamas",
    "BIH": "Bosnia and Herzegovina",
    "BLM": "Saint Barthélemy",
    "BLR": "Belarus",
    "BLZ": "Belize",
    "BMU": "Bermuda",
    "BOL": "Bolivia (Plurinational State of)",
    "BRA": "Brazil",
    "BRB": "Barbados",
    "BRN": "Brunei Darussalam",
    "BTN": "Bhutan",
    "BVT": "Bouvet Island",
    "BWA": "Botswana",
    "CAF": "Central African Republic",
    "CAN": "Canada",
    "CCK": "Cocos (Keeling) Islands",
    "CHE": "Switzerland",
    "CHL": "Chile",
    "CHN": "China",
    "CIV": "Côte d'Ivoire",
    "CMR": "Cameroon",
    "COD": "Congo, Democratic Republic of the",
    "COG": "Congo",
    "COK": "Cook Islands",
    "COL": "Colombia",
    "COM": "Comoros",
    "CPV": "Cabo Verde",
    "CRI": "Costa Rica",
    "CUB": "Cuba",
    "CUW": "Curaçao",
    "CXR": "Christmas Island",
    "CYM": "Cayman Islands",
    "CYP": "Cyprus",
    "CZE": "Czechia",
    "DEU": "Germany",
    "DJI": "Djibouti",
    "DMA": "Dominica",
    "DNK": "Denmark",
    "DOM": "Dominican Republic",
    "DZA": "Algeria",
    "ECU": "Ecuador",
    "EGY": "Egypt",
    "ERI": "Eritrea",
    "ESH": "Western Sahara",
    "ESP": "Spain",
    "EST": "Estonia",
    "ETH": "Ethiopia",
    "FIN": "Finland",
    "FJI": "Fiji",
    "FLK": "Falkland Islands (Malvinas)",
    "FRA": "France",
    "FRO": "Faroe Islands",
    "FSM": "Micronesia (Federated States of)",
    "GAB": "Gabon",
    "GBR": "United Kingdom of Great Britain and Northern Ireland",
    "GEO": "Georgia",
    "GGY": "Guernsey",
    "GHA": "Ghana",
    "GIB": "Gibraltar",
    "GIN": "Guinea",
    "GLP": "Guadeloupe",
    "GMB": "Gambia",
    "GNB": "Guinea-Bissau",
    "GNQ": "Equatorial Guinea",
    "GRC": "Greece",
    "GRD": "Grenada",
    "GRL": "Greenland",
    "GTM": "Guatemala",
    "GUF": "French Guiana",
    "GUM": "Guam",
    "GUY": "Guyana",
    "HKG": "Hong Kong",
    "HMD": "Heard Island and McDonald Islands",
    "HND": "Honduras",
    "HRV": "Croatia",
    "HTI": "Haiti",
    "HUN": "Hungary",
    "IDN": "Indonesia",
    "IMN": "Isle of Man",
    "IND": "India",
    "IOT": "British Indian Ocean Territory",
    "IRL": "Ireland",
    "IRN": "Iran (Islamic Republic of)",
    "IRQ": "Iraq",
    "ISL": "Iceland",
    "ISR": "Israel",
    "ITA": "Italy",
    "JAM": "Jamaica",
    "JEY": "Jersey",
    "JOR": "Jordan",
    "JPN": "Japan",
    "KAZ": "Kazakhstan",
    "KEN": "Kenya",
    "KGZ": "Kyrgyzstan",
    "KHM": "Cambodia",
    "KIR": "Kiribati",
    "KNA": "Saint Kitts and Nevis",
    "KOR": "Korea, Republic of",
    "KWT": "Kuwait",
    "LAO": "Lao People's Democratic Republic",
    "LBN": "Lebanon",
    "LBR": "Liberia",
    "LBY": "Libya",
    "LCA": "Saint Lucia",
    "LIE": "Liechtenstein",
    "LKA": "Sri Lanka",
    "LSO": "Lesotho",
    "LTU": "Lithuania",
    "LUX": "Luxembourg",
    "LVA": "Latvia",
    "MAC": "Macao",
    "MAF": "Saint Martin (French part)",
    "MAR": "Morocco",
    "MCO": "Monaco",
    "MDA": "Moldova, Republic of",
    "MDG": "Madagascar",
    "MDV": "Maldives",
    "MEX": "Mexico",
    "MHL": "Marshall Islands",
    "MKD": "North Macedonia",
    "MLI": "Mali",
    "MLT": "Malta",
    "MMR": "Myanmar",
    "MNE": "Montenegro",
    "MNG": "Mongolia",
    "MNP": "Northern Mariana Islands",
    "MOZ": "Mozambique",
    "MRT": "Mauritania",
    "MSR": "Montserrat",
    "MTQ": "Martinique",
    "MUS": "Mauritius",
    "MWI": "Malawi",
    "MYS": "Malaysia",
    "MYT": "Mayotte",
    "NAM": "Namibia",
    "NCL": "New Caledonia",
    "NER": "Niger",
    "NFK": "Norfolk Island",
    "NGA": "Nigeria",
    "NIC": "Nicaragua",
    "NIU": "Niue",
    "NLD": "Netherlands",
    "NOR": "Norway",
    "NPL": "Nepal",
    "NRU": "Nauru",
    "NZL": "New Zealand",
    "OMN": "Oman",
    "PAK": "Pakistan",
    "PAN": "Panama",
    "PCN": "Pitcairn",
    "PER": "Peru",
    "PHL": "Philippines",
    "PLW": "Palau",
    "PNG": "Papua New Guinea",
    "POL": "Poland",
    "PRI": "Puerto Rico",
    "PRK": "Korea (Democratic People's Republic of)",
    "PRT": "Portugal",
    "PRY": "Paraguay",
    "PSE": "Palestine, State of",
    "PYF": "French Polynesia",
    "QAT": "Qatar",
    "REU": "Réunion",
    "ROU": "Romania",
    "RUS": "Russian Federation",
    "RWA": "Rwanda",
    "SAU": "Saudi Arabia",
    "SDN": "Sudan",
    "SEN": "Senegal",
    "SGP": "Singapore",
    "SGS": "South Georgia and the South Sandwich Islands",
    "SHN": "Saint Helena, Ascension and Tristan da Cunha",
    "SJM": "Svalbard and Jan Mayen",
    "SLB": "Solomon Islands",
    "SLE": "Sierra Leone",
    "SLV": "El Salvador",
    "SMR": "San Marino",
    "SOM": "Somalia",
    "SPM": "Saint Pierre and Miquelon",
    "SRB": "Serbia",
    "SSD": "South Sudan",
    "STP": "Sao Tome and Principe",
    "SUR": "Suriname",
    "SVK": "Slovakia",
    "SVN": "Slovenia",
    "SWE": "Sweden",
    "SWZ": "Eswatini",
    "SXM": "Sint Maarten (Dutch part)",
    "SYC": "Seychelles",
    "SYR": "Syrian Arab Republic",
    "TCA": "Turks and Caicos Islands",
    "TCD": "Chad",
    "TGO": "Togo",
    "THA": "Thailand",
    "TJK": "Tajikistan",
    "TKL": "Tokelau",
    "TKM": "Turkmenistan",
    "TLS": "Timor-Leste",
    "TON": "Tonga",
    "TTO": "Trinidad and Tobago",
    "TUN": "Tunisia",
    "TUR": "Turkey",
    "TUV": "Tuvalu",
    "TWN": "Taiwan, Province of China",
    "TZA": "Tanzania, United Republic of",
    "UGA": "Uganda",
    "UKR": "Ukraine",
    "UMI": "United States Minor Outlying Islands",
    "URY": "Uruguay",
    "USA": "United States of America",
    "UZB": "Uzbekistan",
    "VAT": "Holy See",
    "VCT": "Saint Vincent and the Grenadines",
    "VEN": "Venezuela (Bolivarian Republic of)",
    "VGB": "Virgin Islands (British)",
    "VIR": "Virgin Islands (U.S.)",
    "VNM": "Viet Nam",
    "VUT": "Vanuatu",
    "WLF": "Wallis and Futuna",
    "WSM": "Samoa",
    "YEM": "Yemen",
    "ZAF": "South Africa",
    "ZMB": "Zambia",
    "ZWE": "Zimbabwe",
}
