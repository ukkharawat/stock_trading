import csv , sys , os
import numpy as np
import math

project_dir = '/backend/'

sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django

django.setup()

from stockApp.models import Stock

data = csv.reader(open('symkey.csv'), delimiter=",")
Stock.objects.all().delete()

for row in data:
	if row[0] != 'Name':
		stock = Stock()
		stock.name = row[0]
		stock.fullname = row[1]
		stock.industry = row[2]
		stock.sector = row[3]
		stock.save()
		print(row)
	

# for row in data:
# 	for item in row:
# 		if item is "" :
# 			print "Nan"


# # for row in data:
# 	if row[0] != 'Date':
# 		stock = Stock()
# 		stock.date = row[0]
# 		if row[1] is "":
# 			stock.openPrice = np.nan
# 			stock.closePrice = np.nan
# 			stock.high = np.nan
# 			stock.low = np.nan
# 			stock.adjClose = np.nan
# 			stock.volume = np.nan
# 			stock.save()

# 		else:
# 			stock.openPrice = row[1]
# 			stock.closePrice = row[2]
# 			stock.high = row[3]
# 			stock.low = row[4]
# 			stock.adjClose = row[5]
# 			stock.volume = row[6]
# 			stock.save()

# 		print(row)
