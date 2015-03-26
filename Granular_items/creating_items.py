import pandas as pd
import re

location = "C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Expanded_Description\jandesc.csv"
df = pd.read_csv(location)

df.columns = ['IndexNo', 'BillNo', 'Date', 'Time', 'Description', 'Quantity', 'Rate', 'Amount']
df = df.drop('IndexNo', axis=1)

df = df[np.isfinite(df['Rate'])]
lis = pd.Series()
for i in range(0 ,max(df.index)+1):
    lis = lis.set_value(i, 'UNNAMED')

#df = df.drop('Item', axis=1)
df.insert(4,'Item',lis,allow_duplicates=False)

for idx, record in df['Description'].iteritems():
    if (re.search("GLUCOND", record) or re.search("SATVA CHOCO", record) or re.search("GATORADE", record) or re.search("SATVA GETRIM", record) or re.search("GLUCOVITA", record) or re.search("PEDIASURE", record) or re.search("CHYAWANPRAKASH", record) or re.search("BOOST", record) or re.search("BOURNVITA", record) or re.search("COMPLAN", record) or re.search("HORLICKS", record) or re.search("MALTOVA", record) or re.search("PROTINEX", record) or re.search("SQUASH", record) or re.search("BOURN VITA", record) or re.search("PEDIASURE", record) or re.search("VIVA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'ENERGY DRINKS'

for idx, record in df['Description'].iteritems():
    if (re.search("5 STAR", record) or re.search("GALAXY", record) or re.search("JUICY FRUIT", record) or re.search("JUJUBE", record) or re.search("BOOMER", record) or re.search("HERSHEY`S", record) or re.search("CADBURY", record) or re.search("COFFY BITE", record) or re.search("DAIRY MILK", record) or re.search("KIT KAT", record) or re.search("KITKAT", record) or re.search("LOTTE", record) or re.search("ORBIT", record) or re.search("JUICY FRUIT", record) or re.search("DOUBLEMINT", record) or re.search("MILKYBAR", record) or re.search("MUNCH", record) or re.search("MINT", record) or re.search("NESTLE", record) or re.search("BAR ONE", record) or re.search("ALPENLIEBE", record) or re.search("TEMPTATIONS", record) or re.search("CELEBRATIONS", record) or re.search("ECLAIRS", record) or re.search("GEMS", record) or re.search("PERK", record) or re.search("GEMS", record) or re.search("FEAST", record) or re.search("SNICKERS", record) or re.search("POLO", record) or re.search("LOLLIPOP", record) or re.search("SPEARMINT", record) or re.search("KINDER JOY", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'CHOCOLATE'

for idx, record in df['Description'].iteritems():
    if (re.search("APSARA", record) or re.search("SCOTCH MAGIC", record) or re.search("CDDVD MARKE", record) or re.search("C D / DVD", record) or re.search("RIPPER BALL", record) or re.search("RANGEELA MOU", record) or re.search("BROWN COVERS ROLL", record) or re.search("GLITTER", record) or re.search("CAMLIN", record) or re.search("CHALKPIEC", record) or re.search("CAMEL", record) or re.search("CRAYONS", record) or re.search("DRAWING", record) or re.search("FEVI", record) or re.search("FABERCASTEL", record) or re.search("NATARAJ", record) or re.search("CELLO", record) or re.search("CHART", record) or re.search("PEN ", record) or re.search("A4", record) or re.search("REYNOLDS", record) or re.search("TAPE", record) or re.search("NOTE  BOOK", record) or re.search("STAPLES", record) or re.search("KANGARO", record) or re.search("MSEAL", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'STATIONARY'

for idx, record in df['Description'].iteritems():
    if (re.search("ARIEL", record) or re.search("ACTIVE", record) or re.search("ROBIN", record) or re.search("WASHING", record) or re.search("COMFORT", record) or re.search("FABRIC", record) or re.search("HENKO", record) or re.search("MR.WHITE", record) or re.search("REVIVE", record) or re.search("RIN", record) or re.search("STARCH", record) or re.search("SURF EXCEL", record) or re.search("TIDE", record) or re.search("UJALA", record) or re.search("VANISH", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'DETERGENT'

for idx, record in df['Description'].iteritems():
    if (re.search("AJAY", record) or re.search("CLOSE UP", record) or re.search("COLGATE", record) or re.search("MOUTHWASH", record) or re.search("DENTAL", record) or re.search("TOOTH PICK", record) or re.search("DABUR RED", record) or re.search("MESWAK", record) or re.search("ORAL B", record) or re.search("ORALB", record) or re.search("PEPSODENT", record) or re.search("SENSODYNE", record) or re.search("TPASTE", record) or re.search("TONGUE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'DENTAL CARE'

for idx, record in df['Description'].iteritems():
    if (re.search("MILK 500ML", record) or re.search("GOOD MILK", record) or re.search("TONED MILK", record) or re.search("FLAVOURED MILK", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'MILK'

for idx, record in df['Description'].iteritems():
    if (re.search("EGG", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'EGG'

for idx, record in df['Description'].iteritems():
    if (re.search("AMUL", record) or re.search("GHEE", record) or re.search("VISAKHA", record) or re.search("BUTTER MILK", record) or re.search("BUTTER", record) or re.search("YOGHU", record) or re.search("JUNNU", record) or re.search("DALDA", record) or re.search("DAHI", record) or re.search("HERITAGE", record) or re.search("CURD", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'MILK PRODUCTS'
        
for idx, record in df['Description'].iteritems():
    if (re.search("CHEETOS", record) or re.search("MURMUR", record) or re.search("BOONDI", record) or re.search("KAMALA TIL SWEET", record) or re.search("MURUKU", record) or re.search("LADDU", record) or re.search("TTK FRYUMS", record) or re.search("HAILDIRAM", record) or re.search("HALDIRAM", record) or re.search("KURKURE", record) or re.search("LAYS", record) or re.search("LEHAR", record) or re.search("LITTLE HEARTS", record) or re.search("MOONG", record) or re.search("CHIPS", record) or re.search("FATAFAT", record) or re.search("MISIRI", record) or re.search("CHUDUVA", record) or re.search("NAMKEEN", record) or re.search("CHIKK", record) or re.search("KHAT MIT", record) or re.search("PARLA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'SNACKS'

for idx, record in df['Description'].iteritems():
    if (re.search("BISCUITS", record) or re.search("BISCUTS", record)  or re.search("MCVITIES", record) or re.search("McVITIES", record) or re.search("BISCUIT", record) or re.search("BOURNVILLE", record) or re.search("BRITANNIA", record) or re.search("DARK FANTASY", record) or re.search("DARKFANTASY", record) or re.search("GOOD DAY", record) or re.search("KARACHI", record) or re.search("KRACK", record) or re.search("OREO", record) or re.search("PARLE", record) or re.search("SUNFEAST", record) or re.search("5050", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'BISCUITS'

for idx, record in df['Description'].iteritems():
    if (re.search("COCACOLA", record) or re.search("APPY", record) or re.search("DIET COKE", record) or re.search("FANTA", record) or re.search("LIMCA", record) or re.search("MAAZA", record) or re.search("MINUTE MAID", record) or re.search("PEPSI", record) or re.search("RASNA", record) or re.search("TANG", record) or re.search("REAL JUICE", record) or re.search("RED BULL", record) or re.search("SPRITE", record) or re.search("THUMSUP", record) or re.search("THUMS UP", record) or re.search("TROPICANA", record) or re.search("KINLEY", record) or re.search("B`LUE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'BEVERAGES'

for idx, record in df['Description'].iteritems():
    if ( re.search("BAND-AID", record) or re.search("PANCHA TULAS", record) or re.search("PREMS BORIC ACID", record) or re.search("CHOCOLATE EX", record) or re.search("SPLENDA TAB", record) or re.search("DETTOL", record) or re.search("MOOV", record) or re.search("ZANDU", record) or re.search("VICKS", record) or re.search("SUGAR FREE", record) or re.search("SPLENDA SACT", record) or re.search("AMRUTANJAN", record) or re.search("FAST RELIEF", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'HEALTH CARE'

for idx, record in df['Description'].iteritems():
    if (re.search("SALT", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'SALT'

for idx, record in df['Description'].iteritems():
    if (re.search("TEA", record) or re.search("SUNRISE", record) or re.search("3 ROSES", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'TEA'

for idx, record in df['Description'].iteritems():
    if (re.search("COFFE", record) or re.search("BRU", record) or re.search("NASCAFE", record) or re.search("NESCAFE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'COFFEE'

for idx, record in df['Description'].iteritems():
    if (re.search("ICE CREAM", record) or re.search("CORNETTO", record) or re.search("KWALITY WALL`S", record) or re.search("MAGNUM", record) or re.search("BUTTERSCOTCH", record) or re.search("VANILLA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'ICE CREAM'

for idx, record in df['Description'].iteritems():
    if (re.search("ALL OUT", record) or re.search("TRUBBLE GUM", record) or re.search("JET ", record) or re.search("INSECT KILLER", record) or re.search("GOOD KNIGH", record) or re.search("LAXMANREKHAA", record) or re.search("BAYGON", record) or re.search("HIT", record) or re.search("MORTEIN", record) or re.search("ODOMOS", record) or re.search("ODOMAS", record) or re.search("GAMAXINE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'INSECT REPELLENT'

for idx, record in df['Description'].iteritems():
    if (re.search("KELLOGG", record) or re.search("KELLOGG`S", record) or re.search("BAGRRY`S WHI", record) or re.search("OAT", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'CEREAL'

for idx, record in df['Description'].iteritems():
    if (re.search("SUGAR", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'SUGAR'

for idx, record in df['Description'].iteritems():
    if (re.search("SOUNF", record) or re.search("CRANE", record) or re.search("NUT POWDER", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'SOUNF'

for idx, record in df['Description'].iteritems():
    if (re.search("COCONUT", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'COCONUT'

for idx, record in df['Description'].iteritems():
    if (re.search("HUGGIES", record) or re.search("MAMY POKO PANTS", record) or re.search("PAMPERS", record) or re.search("DIAPERS", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'DIAPERS'

for idx, record in df['Description'].iteritems():
    if (re.search("NOODLES", record) or re.search("MAGGI", record) or re.search("KNORR", record)):# and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'NOODLES'

for idx, record in df['Description'].iteritems():
    if (re.search("RAVA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'RAVA'

for idx, record in df['Description'].iteritems():
    if (re.search("POPCORN", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'POPCORN'

for idx, record in df['Description'].iteritems():
    if (re.search("AMBICA", record) or re.search("CYCLE", record) or re.search("SAI  FLORA", record) or re.search("N R YAGNA", record) or re.search("CHANDAN", record) or re.search("GOPURAM", record) or re.search("GOKURAPURAM", record) or re.search("KUMKUM", record) or re.search("PAKEEZAH", record) or re.search("VATHULU", record) or re.search("ANURAG", record) or re.search("AGARBATHI", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'POOJA ITEMS'

for idx, record in df['Description'].iteritems():
    if (re.search("STAYFREE", record) or re.search("WHISPER", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'SANITARY PADS'

for idx, record in df['Description'].iteritems():
    if (re.search("ONIONS", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'ONIONS'

for idx, record in df['Description'].iteritems():
    if (re.search("AIRCEL", record) or re.search("AIRTEL", record) or re.search("EXCELL", record) or re.search("RELIANCE", record) or re.search("IDEA", record) or re.search("TATA INDICOM", record) or re.search("VODAFONE", record) or re.search("TATA DOCOMO", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'RECHARGE'

for idx, record in df['Description'].iteritems():
    if (re.search("SAUCE", record) or re.search("SOUCE", record) or re.search("KETCHUP", record) or re.search("PUREE", record) or re.search("TOM ", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'SAUCE'

for idx, record in df['Description'].iteritems():
    if (re.search("FRUIT JAM", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'JAM'

for idx, record in df['Description'].iteritems():
    if (re.search("MAIDA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'MAIDA'

for idx, record in df['Description'].iteritems():
    if (re.search("SABENA", record) or re.search("AXION", record) or re.search("MR MUSCLE", record) or re.search("VIM", record) or re.search("PITAMBARI", record) or re.search("PRILL", record) or re.search("PRIL", record) or re.search("EXO", record) or re.search("SCRUB", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'DISH CLEANER'

for idx, record in df['Description'].iteritems():
    if (re.search("PAPAD", record) or re.search("APPALAM", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'PAPAD'

for idx, record in df['Description'].iteritems():
    if (re.search("MASAL", record) or re.search("NOODELS", record) or re.search("EVEREST PANE", record) or re.search("EVEREST RAJM", record) or re.search("CHAAT", record) or re.search("NONVE", record) or re.search("EVEREST KITCHEN KING", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'MASALA'

for idx, record in df['Description'].iteritems():
    if (re.search("VIJAYA", record) or re.search("GINGELLY OIL", record) or re.search("SUNFLOWER OIL", record) or re.search("RICE RICHY OIL", record) or re.search("SAFFOLA", record) or re.search("FORTUNE", record) or re.search("FREEDOM", record) or re.search("FIGARO", record) or re.search("SUNDROP", record) or re.search("SAFFOLA", record) or re.search("GOLD DROP", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'COOKING OIL'

for idx, record in df['Description'].iteritems():
    if (re.search("BABY ", record) or re.search("JOHNSON", record) or re.search("WOODWARDS", record) or re.search("JOHBSON", record) or re.search("JOHNSON`S", record) or re.search("DOY CARE", record) or re.search("FEEDING", record) or re.search("CERELAC", record) or re.search("WIPRO SILICON NIPPLE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'BABY CARE'


for idx, record in df['Description'].iteritems():
    if (re.search("NIPPO", record) or re.search("DURACELL", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'BATTERIES'
        
for idx, record in df['Description'].iteritems():
    if (re.search("CARRY BAG", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'CARRY BAG'
        
for idx, record in df['Description'].iteritems():
    if (re.search("COMB", record) or re.search("COMBS", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'COMB'

for idx, record in df['Description'].iteritems():
    if (re.search("SOAP BOX", record) or re.search("RUBBER", record)or re.search("FRIDGE", record) or re.search("STRAWS", record) or re.search("MAT ", record) or re.search("DOOR MAT", record) or re.search("CLOTH BRUSH", record) or re.search("CLIPS", record) or re.search("ALUMINIUM", record) or re.search("DECOR CONTAI", record) or re.search("DUST PAN", record) or re.search("LONG BOTTLE CLEANER", record) or re.search("ALL TIME GLASS", record) or re.search("PLASTIC", record) or re.search("GASKET", record) or re.search("LOCKS", record) or re.search("UMBRELLA", record) or re.search("PLAYING CARDS", record) or re.search("NYLON", record) or re.search("999", record) or re.search("PVC", record) or re.search("PIPE", record) or re.search("PLATES", record) or re.search("GLASSES", record) or re.search("HANDLE", record) or re.search("YOGA", record) or re.search("GARBAGE", record) or re.search("THERMOCOL", record) or re.search("HEAVY DUTY ROPE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'PLASTIC'

for idx, record in df['Description'].iteritems():
    if (re.search("SOAP", record) or re.search("CINTHOL", record) or re.search("CHANDRIKA", record) or re.search("DOVE", record) or re.search("MEDIMIX", record) or re.search("SANTOOR", record) or re.search("HAMAM", record) or re.search("LIFEBUOY", record) or re.search("LUX", record) or re.search("PEARS", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'BODY SOAP'

for idx, record in df['Description'].iteritems():
    if (re.search("HARPIC", record) or re.search("GLO ", record) or re.search("DRAIN CLEAN", record) or re.search("CIF CREAM",record) or re.search("KITCHEN CLEANER", record) or re.search("CLOTH", record) or re.search("GEM ", record) or re.search("MOP", record) or re.search("BROOM", record) or re.search("KHARATA", record) or re.search("LIZOL", record) or re.search("DOMEX", record) or re.search("SPONGE", record) or re.search("DUSTER", record) or re.search("FLOOR", record) or re.search("EASY OFF BA", record) or re.search("KLINOL ACID", record) or re.search("COLIN", record) or re.search("KIWI ", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'FLOOR CLEANER'

for idx, record in df['Description'].iteritems():
    if (re.search("BADAM", record) or re.search("DATES", record) or re.search("ALMOND", record) or re.search("ANJEER", record) or re.search("KAJU", record) or re.search("KIS MIS", record) or re.search("KARJOOR", record) or re.search("PISTA", record) or re.search("GRAPE", record) or re.search("WALNUT", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'DRY FRUITS'

for idx, record in df['Description'].iteritems():
    if (re.search("JAGGERY", record) or re.search("JAGGRY", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'JAGGERY'

for idx, record in df['Description'].iteritems():
    if (re.search("SWARNA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'TAMARIND'

for idx, record in df['Description'].iteritems():
    if (re.search("ANASAFLOWER", record) or re.search("ATAL SENDHA NAMAK", record) or re.search("KALA MIRCH", record) or re.search("KASURI METHI", record) or re.search("AZANMOTO", record) or re.search("BARLIE", record) or re.search("JEERA", record) or re.search("BIRYANI LEAF", record) or re.search("SHAJEERA", record) or re.search("DALCHANI", record) or re.search("DHANIYA", record) or re.search("ELACHI", record) or re.search("ENO", record) or re.search("JAJI KAI", record) or re.search("JAPATRI", record) or re.search("JEERA", record) or re.search("KARAKAI", record) or re.search("LAVANGAM", record) or re.search("MARATI MOGGA", record) or re.search("MENTHI", record) or re.search("VAKAKALU", record) or re.search("VAMU", record) or re.search("RAI ", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'SPICES'

for idx, record in df['Description'].iteritems():
    if (re.search("HONEY", record) or re.search("GIRIJAN", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'HONEY'


for idx, record in df['Description'].iteritems():
    if (re.search(" MIX", record) or re.search("READY TO EAT", record) or re.search("GELATINE", record) or re.search("MTR UTTAPPAM", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'INSTANT MIXES'

for idx, record in df['Description'].iteritems():
    if (re.search("RICE", record) or re.search("DAAWAT", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'RICE'

for idx, record in df['Description'].iteritems():
    if (re.search("UDATH", record) or re.search("SABJA SEED", record) or re.search(" DAL", record) or re.search("SOYA BEAN", record) or re.search("TIL BLACK", record) or re.search("RAGULU", record) or re.search("CHANA", record) or re.search("BOBBARLU", record) or re.search("RAJAMA", record) or re.search("GROUND NUT", record) or re.search("SANAGALU", record) or re.search("PUTANALU", record) or re.search("BATANI", record) or re.search("BATANA", record) or re.search("SAGO", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'PULSES'

for idx, record in df['Description'].iteritems():
    if (re.search("CAKE", record) or re.search("CHERRY", record) or re.search("CHOCOLATE CU", record) or re.search("MILK BREAD", record) or re.search("NUTELLA", record) or re.search("ESSENCE", record) or re.search("ELITE", record) or re.search("PAV BUN", record) or re.search("PIE ", record) or re.search("TUTY FRUITY", record) or re.search("DRIED YEAST", record) or re.search("VINEGAR", record) or re.search("BAKING POWDER", record) or re.search("EATING SODA", record) or re.search("COCOA", record) or re.search("VIOLA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'BAKERY ITEMS'

for idx, record in df['Description'].iteritems():
    if (re.search("C C", record) or re.search("I D", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'BATTER'

for idx, record in df['Description'].iteritems():
    if (re.search("TURMERIC", record) or re.search("HALDI KADI", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'TURMERIC'

for idx, record in df['Description'].iteritems():
    if (re.search("SHAMPOO", record) or re.search("CLINIC ALLCLEAR", record) or re.search("DABUR LEMONE", record) or re.search("PANTENE", record) or re.search("SHAM", record) or re.search("HEAD & SHOULDER", record) or re.search("SUNSILK", record) or re.search("TRESEMME", record) or re.search("CLINIC PLUS", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'SHAMPOO'

for idx, record in df['Description'].iteritems():
    if (re.search("VEET", record) or re.search("GILLETTE", record) or re.search("WILMAN II EXECUTIVE", record) or re.search("SHAVING", record) or re.search("SHAVE FOAM", record) or re.search("BLADE", record) or re.search("SUPERMAX", record) or re.search("SUPER MAX", record) or re.search("SHAVIN", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'HAIR REMOVALS'

for idx, record in df['Description'].iteritems():
    if (re.search("AIR WICK", record) or re.search("GLADE", record) or re.search("FRESHENER", record) or re.search("NAPTHALANE", record) or re.search("NAPTHALENE", record) or re.search("ROOM FRESHENER", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'AIR FRESHENERS'

for idx, record in df['Description'].iteritems():
    if (re.search("CRYSTAL", record) or re.search("CUTTER", record) or re.search("SCISSORS", record) or re.search("CARTINI", record) or re.search("PEELER", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'CUTLERY'

for idx, record in df['Description'].iteritems():
    if (re.search("BODY", record) or re.search("SKIN", record) or re.search("FAIR CREAM", record) or re.search("AYUR CLEANSING MILK", record) or re.search("YARDLEY", record) or re.search("PREMIUM EAU DE COLOGNE", record) or re.search("SUN SCREEN", record) or re.search("SUNSCREEN", record) or re.search("SHOWER TO SHOWER", record) or re.search("AYUR MOISTURIZER", record) or re.search("SAKA BLEACH FOR MEN", record) or re.search("AYUR ASTRIGENT", record) or re.search("THE COLO SSA", record) or re.search("GLOVES", record) or re.search("ANOOS FAIR & FRESH", record) or re.search("FOOT FILE", record) or re.search("SONY PUMICE STONE", record) or re.search("EMAMI", record) or re.search("BABYLIPS", record) or re.search("VICCO", record) or re.search("BUDS", record) or re.search("GULABARI", record) or re.search("NAIL CUTTER", record) or re.search("NAILPAINT", record) or re.search("LACTO CALAMINE", record) or re.search("TALC", record) or re.search("VASELINE", record) or re.search("VASELION", record) or re.search("LOTION", record) or re.search("SET WET", record) or re.search("EVER YUTH", record) or re.search("BANJARA`S", record) or re.search("FAIR & LOVELY", record) or re.search("FAIREVER", record) or re.search("GARNIER", record) or re.search("GODREJ", record) or re.search("HIMALAYA", record) or re.search("HIMANI", record) or re.search("DEO", record) or re.search("AXE", record) or re.search("LAKME", record) or re.search("LOTUS", record) or re.search("LOREAL", record) or re.search("NIVEA", record) or re.search("NYCIL", record) or re.search("NOVA", record) or re.search("OLAY", record) or re.search("OLD SPICE", record) or re.search("OXY BLEACH", record) or re.search("PALMOLIVE", record) or re.search("PARK AVENUE", record) or re.search("PONDS", record) or re.search("DERMI COOL", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'BODY CARE'

for idx, record in df['Description'].iteritems():
    if (re.search("TISSUE", record) or re.search("WIPES", record) or re.search("TOWEL", record) or re.search("NAPKINS", record) or re.search("KERCHIEF", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'TISSUE'

for idx, record in df['Description'].iteritems():
    if (re.search("CANDLE", record) or re.search("BALLOON", record) or re.search("GIFT", record) or re.search("BOUTIQUE", record) or re.search("PARTY PACK", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'PARTY NEEDS'

for idx, record in df['Description'].iteritems():
    if (re.search("HAIR OIL", record) or re.search("COCONUT OIL", record) or re.search("PARACHUTE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'HAIR OIL'

for idx, record in df['Description'].iteritems():
    if (re.search("HAIR CARE", record) or re.search("AMLA", record) or re.search("GATSBY GEL", record) or re.search("CASTOR OIL", record)  or re.search("LIVON SILKY POTION", record) or re.search("PARAC", record) or re.search("FEM BLEACH", record) or re.search("CASTROL OIL", record) or re.search("SUPER VASMOL", record) or re.search("MEDIKER", record) or re.search("HAIR COLOR", record) or re.search("HAIR COLOUR", record) or re.search("REVLON", record) or re.search("CONDITIONER", record) or re.search("HENNA", record) or re.search("MEHANDI", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'HAIR CARE'

for idx, record in df['Description'].iteritems():
    if (re.search("CFL", record) or re.search("BULB", record) or re.search("GANGA GAS LIGHTER", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'LIGHTS'

for idx, record in df['Description'].iteritems():
    if (re.search("MATCHES", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'MATCHES'

for idx, record in df['Description'].iteritems():
    if (re.search("POWDER", record) or re.search("PINDI", record) or re.search("EVEREST JALJIRA", record) or re.search("NALLAKARAM", record) or re.search("SAMBAR", record) or re.search("RASAM", record) or re.search(" PODI", record) or re.search("EVEREST HING", record) or re.search("PDR", record) or re.search("CHILI POW", record) or re.search(" CHILLI", record) or re.search("COPRA ", record) or re.search("CORNFLOUR", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'KITCHEN POWDERS'

for idx, record in df['Description'].iteritems():
    if (re.search("MEAL MAKER", record) or re.search("MEALMAKER", record) or re.search("VARMICELLI", record) or re.search("MACRONI", record) or re.search("MACARONI", record) or re.search("VARMI", record) or re.search("PASTA", record) or re.search("GOLD FINGERS", record) or re.search("FRYAMS", record) or re.search("KUS KUS", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'COOKING ITEMS'

for idx, record in df['Description'].iteritems():
    if (re.search("GENERAL", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'GENERAL'

for idx, record in df['Description'].iteritems():
    if (re.search("GINGER GARLIC PASTE", record) or re.search("PULIHORA", record) or re.search("CURRY PASTE", record) or re.search("PRO NATURE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'KITCHEN PASTES'

for idx, record in df['Description'].iteritems():
    if (re.search("PICKLE", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'PICKLES'

for idx, record in df['Description'].iteritems():
    if (re.search("GULAB JAMUN", record) or re.search("CUSTARD POW", record) or re.search("RAGI ", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'INSTANT MIXES'

for idx, record in df['Description'].iteritems():
    if (re.search("TENNIS BALL", record) or re.search("SHUTTLE COCK", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'SPORTS'

for idx, record in df['Description'].iteritems():
    if (re.search("CHERRY HANDYSHINE", record) or re.search("CHERRY BLACK", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'SHOE POLISH'

for idx, record in df['Description'].iteritems():
    if (re.search("ATTA", record) or re.search("MULTI GRAINS", record) or re.search("AASHIRVAAD", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx, 'Item'] = 'ATTA'

for idx, record in df['Description'].iteritems():
    if (re.search("FELIX PERF", record) or re.search("BANJAR`S KAS", record) or re.search("CHETANS STEEL PAKKAD", record) or re.search("THREE MOON SAFFRON", record) or re.search("COTTON FLAME ROUND", record) or re.search("KAMAL TIL LA", record) or re.search("KAMAL PENI", record) or re.search("DAADI`S KHAK", record) or re.search("G.D SPECIAL", record) or re.search("ATAL BHAGGAR", record) or re.search("KAMAL ANDHRA", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'OTHER'

for idx, record in df['Description'].iteritems():
    if (re.search("AQUAGUARD PU", record) or re.search("PREMIER WET", record) or re.search("WHIRLPOOL LI", record)) and df.loc[idx, 'Item'] == "UNNAMED":
        df.loc[idx,'Item'] = 'MACHINES'

df.to_csv("C:\Users\saisree849\Documents\GitHub\Super-Market-Data\Granular_items\janitems.csv", sep = ",")