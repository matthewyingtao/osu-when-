import datetime
game = input("what game do you want to play \n")
hour = int(input("what time do you get home? \n"))


def calc_datetime(day, hour):
	current_date = datetime.datetime.now()
	next_date = datetime.date.today()
	osu_time = datetime.time(hour, 00, 0)

	while next_date.weekday() != day:
		next_date += datetime.timedelta(1)

	next_osu = datetime.datetime.combine(next_date, osu_time)

	hours_difference = (next_osu - current_date).total_seconds() / 3600.0
	return(str(round(hours_difference)))

print("Assuming " + game + " gaming starts at Friday " + str(hour) + "pm, " + game + " will begin in: " + calc_datetime(4, hour) + " hours.")

