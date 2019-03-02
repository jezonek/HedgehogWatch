def prepare_time_for_display(hour, minute, second):
    return 't {hour}.{minute}.{second}'.format(hour=str(hour).zfill(2), minute=str(minute).zfill(2),
                                               second=str(second).zfill(2))


def prepare_date_for_display(day, month, year):
    return '{day}.{month}.{year}'.format(day=str(day).zfill(2), month=str(month).zfill(2), year=str(year))
