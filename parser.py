import csv

popread = open('gm-pop.csv', 'rb')
popreader = csv.reader(popread, delimiter = ',')

Y = open('gapminder_load.sql', 'w')

for i in range(1):
    yearvalues = popreader.next()

year_arr = []

#insert years into YEAR table and year_arr
for z in yearvalues:
    if (z != 'Population'):
        year_arr.append(z)
        Y.write("INSERT INTO YEAR VALUES(%s);\n" %z)
Y.write("\n")

#fill GM_POP table
try:
    count = 1
    while count < 254:
        for i in range(count):
            country_values = popreader.next()
            countryname = country_values[0]

            i = -1
            for z in country_values:
                if(z != countryname):
                    if(z == ''):
                        Y.write("INSERT INTO GM_POP VALUES('%s',%s,NULL);\n" %(countryname,year_arr[i]))
                    else:
                        Y.write("INSERT INTO GM_POP VALUES('%s',%s,%s);\n" %(countryname,year_arr[i],z))
                i += 1
        count += 1  
except:
    popread.close()

#GM_LE--------------------------------------------------------------------------

leread = open('gm-le.csv', 'rb')
lereader = csv.reader(leread, delimiter = ',')

for i in range(1):
    leyear = lereader.next()

leyear_arr = []

for z in leyear:
    if (z != 'Life expectancy at birth'):
        leyear_arr.append(z)

#fill GM_LE table
try:
    count = 1
    while count < 254:
        for i in range(count):
            le_values = lereader.next()
            if(le_values[0] == 'Cote d\'Ivoire'):
                le_values[0] = 'Cote d\'\'Ivoire'
            countryname = le_values[0]

            i = -1
            for z in le_values:
                if(z != countryname):
                    if(z == ''):
                        Y.write("INSERT INTO GM_LE VALUES('%s',%s,NULL);\n" %(countryname,leyear_arr[i]))
                    else:
                        Y.write("INSERT INTO GM_LE VALUES('%s',%s,%s);\n" %(countryname,leyear_arr[i],z))
                i += 1
        count += 1  
except:
    leread.close()

#GM_INCOME----------------------------------------------------------------------

incomeread = open('gm-income.csv', 'rb')
incomereader = csv.reader(incomeread, delimiter = ',')

for i in range(1):
    incomeyear = incomereader.next()

incomeyear_arr = []

for z in incomeyear:
    if (z != ''):
        incomeyear_arr.append(z)

#fill GM_INCOME table
try:
    count = 1
    while count < 254:
        for i in range(count):
            income_values = incomereader.next()
            if(income_values[0] == 'Cote d\'Ivoire'):
                income_values[0] = 'Cote d\'\'Ivoire'
            countryname = income_values[0]

            i = -1
            for z in income_values:
                if(z != countryname):
                    if(z == ''):
                        Y.write("INSERT INTO GM_INCOME VALUES('%s',%s,NULL);\n" %(countryname,incomeyear_arr[i]))
                    else:
                        Y.write("INSERT INTO GM_INCOME VALUES('%s',%s,%s);\n" %(countryname,incomeyear_arr[i],z))
                i += 1
        count += 1  
except:
    incomeread.close()

#GM_HS--------------------------------------------------------------------------

hsread = open('gm-health-spending.csv', 'rb')
hsreader = csv.reader(hsread, delimiter = ',')

for i in range(1):
    hsyear = hsreader.next()

hsyear_arr = []

for z in hsyear:
    if (z != 'Per capita total expenditure on health (PPP int. $)'):
        hsyear_arr.append(z)

#fill GM_HS table
try:
    count = 1
    while count < 254:
        for i in range(count):
            hs_values = hsreader.next()
            if(hs_values[0] == 'Cote d\'Ivoire'):
                hs_values[0] = 'Cote d\'\'Ivoire'
            countryname = hs_values[0]

            i = -1
            for z in hs_values:
                if(z != countryname):
                    if(z == ''):
                        Y.write("INSERT INTO GM_HS VALUES('%s',%s,NULL);\n" %(countryname,hsyear_arr[i]))
                    else:
                        Y.write("INSERT INTO GM_HS VALUES('%s',%s,%s);\n" %(countryname,hsyear_arr[i],z))
                i += 1
        count += 1  
except:
    hsread.close()

#GM_ELECTRICITY-----------------------------------------------------------------

elecread = open('gm-electricity.csv', 'rb')
elecreader = csv.reader(elecread, delimiter = ',')

for i in range(1):
    elecyear = elecreader.next()

elecyear_arr = []

for z in elecyear:
    if (z != 'Electricity consumption, per capita (kWh)'):
        elecyear_arr.append(z)

#fill GM_ELECTRICITY table
try:
    count = 1
    while count < 254:
        for i in range(count):
            elec_values = elecreader.next()
            if(elec_values[0] == 'Cote d\'Ivoire'):
                elec_values[0] = 'Cote d\'\'Ivoire'
            countryname = elec_values[0]

            i = -1
            for z in elec_values:
                if(z != countryname):
                    if(z == '-'):
                        Y.write("INSERT INTO GM_ELECTRICITY VALUES('%s',%s,NULL);\n" %(countryname,elecyear_arr[i]))
                    else:
                        Y.write("INSERT INTO GM_ELECTRICITY VALUES('%s',%s,%s);\n" %(countryname,elecyear_arr[i],z))
                i += 1
        count += 1  
except:
    elecread.close()


Y.close()
