import datetime
import pytz

date = datetime.datetime.now(
    pytz.timezone('Asia/Ho_Chi_Minh')
)
print(date)