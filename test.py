import csv

data_is_loaded = False

def load_data():
	with open('US_Presidential_Results_12-16.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader, None)  # skip header
		data_total = {}
		for row in reader:
			if row[9] in data_total:
				data_total[row[9]][0] += int(row[2])
				data_total[row[9]][1] += int(row[3])
				data_total[row[9]][2] += int(row[4])
				data_total[row[9]][3] += int(row[12])
				data_total[row[9]][4] += int(row[13])
				data_total[row[9]][5] += int(row[14])
			if row[9] not in data_total:
				data_total[row[9]] = []
				data_total[row[9]].append(int(row[2]))
				data_total[row[9]].append(int(row[3]))
				data_total[row[9]].append(int(row[4]))
				data_total[row[9]].append(int(row[12]))
				data_total[row[9]].append(int(row[13]))
				data_total[row[9]].append(int(row[14]))
		return data_total
		data_is_loaded = True

def get_data(party='gop', raw=False, sort_ascending=True, year=2016):
	if not data_is_loaded:
		data_total = load_data()
	#start to edit
	if party is 'dem':
		####################### dem 2016 ########################
		if year == 2016:
			if raw is True:
				if sort_ascending is True:
					# return dem 2016 raw ascend
					dem_16_raw_asc = []
					i = 0
					for state in data_total.keys():
						dem_16_raw_asc.append([])
						dem_16_raw_asc[i].append(state)
						dem_16_raw_asc[i].append(data_total[state][0])
						dem_16_raw_asc[i] = tuple(dem_16_raw_asc[i])
						i += 1
					dem_16_raw_asc.sort(key=lambda x: x[1])
					# print (dem_16_raw_asc)
					return dem_16_raw_asc

				if sort_ascending is False:
					# return dem 2016 raw descend
					dem_16_raw_des = []
					i = 0
					for state in data_total.keys():
						dem_16_raw_des.append([])
						dem_16_raw_des[i].append(state)
						dem_16_raw_des[i].append(data_total[state][0])
						dem_16_raw_des[i] = tuple(dem_16_raw_des[i])
						i += 1
					dem_16_raw_des.sort(key=lambda x: x[1], reverse=True)
					print (dem_16_raw_des)
					return dem_16_raw_des

			if raw is False:
				if sort_ascending is True:
					# return dem 2016 ratio ascend
					dem_16_ratio_asc = []
					i = 0
					for state in data_total.keys():
						dem_16_ratio_asc.append([])
						dem_16_ratio_asc[i].append(state)
						dem_16_ratio_asc[i].append(data_total[state][0] / data_total[state][2])
						dem_16_ratio_asc[i] = tuple(dem_16_ratio_asc[i])
						i += 1
					dem_16_ratio_asc.sort(key=lambda x: x[1])
					# print (dem_16_ratio_asc)
					return dem_16_ratio_asc
				if sort_ascending is False:
					# return dem 2016 ratio descend
					dem_16_ratio_des = []
					i = 0
					for state in data_total.keys():
						dem_16_ratio_des.append([])
						dem_16_ratio_des[i].append(state)
						dem_16_ratio_des[i].append(data_total[state][0] / data_total[state][2])
						dem_16_ratio_des[i] = tuple(dem_16_ratio_des[i])
						i += 1
					dem_16_ratio_des.sort(key=lambda x: x[1], reverse = True)
					# print (dem_16_ratio_des)
					return dem_16_ratio_des

		####################### dem 2012 ########################
		if year == 2012:
			if raw is True:
				if sort_ascending is True:
					# return dem 2012 raw ascend
					dem_12_raw_asc = []
					i = 0
					for state in data_total.keys():
						dem_12_raw_asc.append([])
						dem_12_raw_asc[i].append(state)
						dem_12_raw_asc[i].append(data_total[state][4])
						dem_12_raw_asc[i] = tuple(dem_12_raw_asc[i])
						i += 1
					dem_12_raw_asc.sort(key=lambda x: x[1])
					# print (dem_12_raw_asc)
					return dem_12_raw_asc

				if sort_ascending is False:
					# return dem 2012 raw descend
					dem_12_raw_des = []
					i = 0
					for state in data_total.keys():
						dem_12_raw_des.append([])
						dem_12_raw_des[i].append(state)
						dem_12_raw_des[i].append(data_total[state][4])
						dem_12_raw_des[i] = tuple(dem_12_raw_des[i])
						i += 1
					dem_12_raw_des.sort(key=lambda x: x[1], reverse=True)
					# print (dem_12_raw_des)
					return dem_12_raw_des

			if raw is False:
				if sort_ascending is True:
					# return dem 2012 ratio ascend
					dem_12_ratio_asc = []
					i = 0
					for state in data_total.keys():
						dem_12_ratio_asc.append([])
						dem_12_ratio_asc[i].append(state)
						dem_12_ratio_asc[i].append(data_total[state][4] / data_total[state][3])
						dem_12_ratio_asc[i] = tuple(dem_12_ratio_asc[i])
						i += 1
					dem_12_ratio_asc.sort(key=lambda x: x[1])
					# print (dem_12_ratio_asc)
					return dem_12_ratio_asc

				if sort_ascending is False:
					# return dem 2012 ratio descend
					dem_12_ratio_des = []
					i = 0
					for state in data_total.keys():
						dem_12_ratio_des.append([])
						dem_12_ratio_des[i].append(state)
						dem_12_ratio_des[i].append(data_total[state][4] / data_total[state][3])
						dem_12_ratio_des[i] = tuple(dem_12_ratio_des[i])
						i += 1
					dem_12_ratio_des.sort(key=lambda x: x[1], reverse = True)
					# print (dem_12_ratio_des)
					return dem_12_ratio_des


	if party is 'gop':
		####################### gop 2016 ########################
		if year == 2016:
			if raw is True:
				if sort_ascending is True:
					# return gop 2016 raw ascend
					gop_16_raw_asc = []
					i = 0
					for state in data_total.keys():
						gop_16_raw_asc.append([])
						gop_16_raw_asc[i].append(state)
						gop_16_raw_asc[i].append(data_total[state][1])
						gop_16_raw_asc[i] = tuple(gop_16_raw_asc[i])
						i += 1
					gop_16_raw_asc.sort(key=lambda x: x[1])
					# print (gop_16_raw_asc)
					return gop_16_raw_asc

				if sort_ascending is False:
					# return gop 2016 raw descend
					gop_16_raw_des = []
					i = 0
					for state in data_total.keys():
						gop_16_raw_des.append([])
						gop_16_raw_des[i].append(state)
						gop_16_raw_des[i].append(data_total[state][1])
						gop_16_raw_des[i] = tuple(gop_16_raw_des[i])
						i += 1
					gop_16_raw_des.sort(key=lambda x: x[1], reverse=True)
					# print (gop_16_raw_des)
					return gop_16_raw_des
			if raw is False:
				if sort_ascending is True:
					# return gop 2016 ratio ascend
					gop_16_ratio_asc = []
					i = 0
					for state in data_total.keys():
						gop_16_ratio_asc.append([])
						gop_16_ratio_asc[i].append(state)
						gop_16_ratio_asc[i].append(data_total[state][1] / data_total[state][2])
						gop_16_ratio_asc[i] = tuple(gop_16_ratio_asc[i])
						i += 1
					gop_16_ratio_asc.sort(key=lambda x: x[1])
					# print (gop_16_ratio_asc)
					return gop_16_ratio_asc

				if sort_ascending is False:
					# return gop 2016 ratio descend
					gop_16_ratio_des = []
					i = 0
					for state in data_total.keys():
						gop_16_ratio_des.append([])
						gop_16_ratio_des[i].append(state)
						gop_16_ratio_des[i].append(data_total[state][1] / data_total[state][2])
						gop_16_ratio_des[i] = tuple(gop_16_ratio_des[i])
						i += 1
					gop_16_ratio_des.sort(key=lambda x: x[1], reverse = True)
					# print (gop_16_ratio_des)
					return gop_16_ratio_des

		####################### gop 2012 ########################
		if year == 2012:
			if raw is True:
				if sort_ascending is True:
					# return gop 2012 raw ascend
					gop_12_raw_asc = []
					i = 0
					for state in data_total.keys():
						gop_12_raw_asc.append([])
						gop_12_raw_asc[i].append(state)
						gop_12_raw_asc[i].append(data_total[state][5])
						gop_12_raw_asc[i] = tuple(gop_12_raw_asc[i])
						i += 1
					gop_12_raw_asc.sort(key=lambda x: x[1])
					# print (gop_12_raw_asc)
					return gop_12_raw_asc

				if sort_ascending is False:
					# return gop 2012 raw descend
					gop_12_raw_des = []
					i = 0
					for state in data_total.keys():
						gop_12_raw_des.append([])
						gop_12_raw_des[i].append(state)
						gop_12_raw_des[i].append(data_total[state][5])
						gop_12_raw_des[i] = tuple(gop_12_raw_des[i])
						i += 1
					gop_12_raw_des.sort(key=lambda x: x[1], reverse=True)
					# print (gop_12_raw_des)
					return gop_12_raw_des

			if raw is False:
				if sort_ascending is True:
					# return gop 2012 ratio ascend
					gop_12_ratio_asc = []
					i = 0
					for state in data_total.keys():
						gop_12_ratio_asc.append([])
						gop_12_ratio_asc[i].append(state)
						gop_12_ratio_asc[i].append(data_total[state][5] / data_total[state][3])
						gop_12_ratio_asc[i] = tuple(gop_12_ratio_asc[i])
						i += 1
					gop_12_ratio_asc.sort(key=lambda x: x[1])
					# print (gop_12_ratio_asc)
					return gop_12_ratio_asc

				if sort_ascending is False:
					# return gop 2012 ratio descend
					gop_12_ratio_des = []
					i = 0
					for state in data_total.keys():
						gop_12_ratio_des.append([])
						gop_12_ratio_des[i].append(state)
						gop_12_ratio_des[i].append(data_total[state][5] / data_total[state][3])
						gop_12_ratio_des[i] = tuple(gop_12_ratio_des[i])
						i += 1
					gop_12_ratio_des.sort(key=lambda x: x[1], reverse = True)
					# print (gop_12_ratio_des)
					return gop_12_ratio_des

	# build the appropriate list of tuples to return

	# return [('A', 1), ('B', 2)]

get_data('dem', True, False)
