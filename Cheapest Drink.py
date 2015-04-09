__author__ = 'Jeff Capaldo'

print 'Welcome to Cheapest Drink!\n\nThis program will calculate ' \
      'which beverage of\nyour choice will give you the most alcohol ' \
      'for your money.\n'

size_drink_ltr = 0
size_drink_ml = 0
size_drink_oz = 0
measurement = 'q'
total_price = 0
alcohol_content = 0

brand_drink = raw_input('Enter the brand of drink you wish to analyze: ')
beverage_drink = raw_input('What type of drink is this (beer, whiskey, wine, etc.? ')

while measurement[0] != 'l' and measurement[0] != 'L' and measurement[0] != 'm'\
        and measurement[0] != 'M' and measurement[0] != 'o'\
        and measurement[0] != 'O' and measurement[0] != '0':
    measurement = raw_input('Are we measuring in liters, milliliters or ounces? ')

if measurement[0] == 'l' or measurement[0] == 'L':
    size_drink_ltr = float(input('How many liters per container? Enter numbers only: '))
elif measurement[0] == 'm' or measurement[0] == 'M':
    size_drink_ml = float(input('How many milliliters per container? Enter numbers only: '))
elif measurement[0] == 'o' or measurement[0] == 'O' or measurement == '0':
    size_drink_oz = float(input('How many ounces per container? Enter numbers only: '))

units = int(input('How many containers are you analyzing? '))

print '\nTo calculate \'proof\' for beer or wine, multiply the alcohol percentage listed on container by 2.\n' \
      'For liquor, proof should be listed on bottle label.\n' \
      '\nFor unknown proof light beer, enter \'6.4\'.\nFor unknown regular beer, enter \'9\'.' \
      '\nFor unknown wine, enter \'25\', and for unknown liquor, enter \'80\'.'
proof = input('\nWhat \'proof\' alcohol is this?\n')
total_price = float(input('What is the total price (in dollars and cents) for ' + str(units) + ' units?\n' \
                        '$'))

if size_drink_ltr == 0 and size_drink_ml == 0 and size_drink_oz == 0:
    print('Your drink is empty!')

if size_drink_ltr != 0:
    alcohol_content = size_drink_ltr * units * (proof * 0.005)
    convert_ml = alcohol_content * 1000
    convert_oz = alcohol_content * 33.81402
    price_per_ltr = total_price / alcohol_content
    price_per_ml = (total_price / alcohol_content) / 1000
    price_per_oz = total_price / convert_oz
    print 'Your ' + str(brand_drink) + ' ' + str(beverage_drink) + \
          ' will contain ' + str(format(alcohol_content, '.2f'))\
          + ' liters, ' + str(format(convert_ml, '.0f')) + ' milliliters or ' + \
          str(format(convert_oz, '.2f')) + ' ounces of pure alcohol. \n\n' \
          'At $' + str(format(total_price, '.2f')) + ', you are paying $' + str(format(price_per_ltr, '.2f')) +\
          ' per liter of alcohol.\n\nThat is $' + str(format(price_per_ml, '.2f')) + \
          ' per milliliter of alcohol or $' + str(format(price_per_oz, '.2f')) + ' per ounce.'
elif size_drink_ml != 0:
    alcohol_content = size_drink_ml * units * (proof * 0.005)
    convert_ltr = alcohol_content / 1000
    convert_oz = convert_ltr * 33.81402
    price_per_ml = total_price / alcohol_content
    price_per_ltr = (total_price / alcohol_content) * 1000
    price_per_oz = total_price / convert_oz
    print 'Your ' + str(brand_drink) + ' ' + str(beverage_drink) + \
          ' will contain ' + str(format(alcohol_content, '.0f'))\
          + ' milliliters, ' + str(format(convert_ltr, '.2f')) + ' liters or ' + \
          str(format(convert_oz, '.2f')) + ' ounces of pure alcohol. \n\n' \
          'At $' + str(format(total_price, '.2f')) + ', you are paying $' + str(format(price_per_ml, '.2f')) +\
          ' per milliliter of alcohol.\n\nThat is $' + str(format(price_per_ltr, '.2f')) + \
          ' per liter of alcohol or $' + str(format(price_per_oz, '.2f')) + ' per ounce.'
elif size_drink_oz != 0:
    alcohol_content = size_drink_oz * units * (proof * 0.005)
    convert_ltr = alcohol_content * 0.0295735
    convert_ml = alcohol_content * 29.5735
    price_per_oz = total_price / alcohol_content
    price_per_ltr = total_price / convert_ltr
    price_per_ml = total_price / convert_ml
    print 'Your ' + str(brand_drink) + ' ' + str(beverage_drink) + \
          ' will contain ' + str(format(alcohol_content, '.2f'))\
          + ' ounces, ' + str(format(convert_ltr, '.2f')) + ' liters or ' + \
          str(format(convert_ml, '.0f')) + ' milliliters of pure alcohol. \n\n' \
          'At $' + str(format(total_price, '.2f')) + ', you are paying $' + str(format(price_per_oz, '.2f')) +\
          ' per ounce of alcohol.\n\nThat is $' + str(format(price_per_ltr, '.2f')) + \
          ' per liter of alcohol or $' + str(format(price_per_ml, '.2f')) + ' per milliliter.'