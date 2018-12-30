from . import(uuid4, datetime, relativedelta)


class BaseModel:
    """Defines the shared properties of various models"""

    def __init__(self, created_at="", updated_at=""):
        self.id = str(uuid4())
        self.created_at = created_at
        self.updated_at = updated_at

    def date_created(self):
        """Retuns the date when an item was created in DDMMYY format"""
        return self.created_at.strftime('%d-%m-%Y')

    def time_updated(self):
        """Returns the time when item was last updated"""
        time_difference = relativedelta(
            datetime.datetime.now(), self.updated_at)
        years = time_difference.years
        months = time_difference.months
        days = time_difference.days
        hours = time_difference.hours
        minutes = time_difference.minutes
        seconds = time_difference.seconds
        return_string = ""
        if years > 0:
            return_string = "updated {} year(s), {} month(s), {} day(s), {} hour(s), {} minute(s), {} second(s) ago".format(
                years, months, days, hours, minutes, seconds)
            return return_string
        elif months > 0:
            return_string = "updated {} month(s), {} day(s), {} hour(s), {} minute(s), {} second(s) ago".format(
                months, days, hours, minutes, seconds)
        elif days > 0:
            return_string = "updated {} day(s), {} hour(s), {} minute(s), {} second(s) ago".format(
                days, hours, minutes, seconds)
        elif hours > 0:
            return_string = "updated {} hour(s), {} minute(s), {} second(s) ago".format(
                hours, minutes, seconds)
        elif minutes > 0:
            return_string = "updated {} minute(s), {} second(s) ago".format(
                minutes, seconds)
        else:
            return_string = "updated {} second(s) ago".format(seconds)
        return return_string
