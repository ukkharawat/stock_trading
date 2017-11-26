import csv , sys , os
import numpy as np
import math

project_dir = '/backend/'

sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django

django.setup()

from stockApp.models import Stock , StockValue

data = csv.reader(open('PTT.BK.csv'), delimiter=",")

for row in data:
	if row[0] != 'Date':
		stockvalue = StockValue()
		stockvalue.name = Stock.objects.get(name='PTT')
		stockvalue.date = row[0]
		if row[1] is "":
			stockvalue.openPrice = np.nan
			stockvalue.closePrice = np.nan
			stockvalue.high = np.nan
			stockvalue.low = np.nan
			stockvalue.adjClose = np.nan
			stockvalue.volume = np.nan
			stockvalue.save()

		else:
			stockvalue.openPrice = row[1]
			stockvalue.closePrice = row[2]
			stockvalue.high = row[3]
			stockvalue.low = row[4]
			stockvalue.adjClose = row[5]
			stockvalue.volume = row[6]
			stockvalue.save()

		print(row)
	