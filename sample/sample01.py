from pylocalytics import pylocalytics
from datetime import datetime
from datetime import timedelta


loctx = pylocalytics(api_key = 'YOU_API_KEY', api_secret= 'YOUR_API_SECRET_KEY')

loctx.download_data(
            app_ids = ['AAAAA', 'BBBBB'],
            start_date = datetime.today() - timedelta(2),
            end_date = datetime.today()
        )
