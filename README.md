# Python Client for Localytics Raw and Audience Data Export
This is a Python API Client to get data from  [Localytics Raw Data Export](https://docs.localytics.com/dev/export-apis.html#log-exports-api)
and [Localytics Audience Data Export](https://docs.localytics.com/dev/export-apis.html#audience-exports).

It allows to export all events and sessions and user defined audience captured by Localytics. Data is written in JSON (Compressed) and available on hourly basis as log files.


## Installation
istall it by `pip`

```bash
    $ pip install pylocalytics
```


## Usage
Start by loading the library and also you need to import `timedelta` and `datetime` on most cases.

```python
    >>> from pylocalytics import pyLocalytics
    >>> from datetime import datetime
    >>> from datetime import timedelta
```


### Setup and Authentication
In order for you to download Localytics events, you need to authenticate with using `api_key` and `api_secret`.
Once you supply it, it will be used throughout the entire session. You can find you API_KEY and API_SECRET_KEY in your  Localytics Admin Panel on [Admin Setting API Key](https://dashboard.localytics.com/settings/apikeys)

```python
    >>> loctx = pylocalytics(api_key = 'YOU_API_KEY', api_secret= 'YOUR_API_SECRET_KEY')
```


### Download Data
There is a method  `download_data` that downloads data to local folder. Example shows how to export data for last 2 days:

```python
    >>> loctx.download_data(
            app_ids = ['YOUR_APP_ID'],
            start_date = datetime.today() - timedelta(2),
            end_date = datetime.today()
        )
```

You can also specify optional parameters. This is more complex example:

```python
    >>> loctx.download_data(
        app_ids = [YOUR_APP_ID],
        start_date = datetime.today() - timedelta(2),
        end_date = datetime.today(),
        destination_folder = 'data',
        compressed=True
    )
```

On default data are stored in `localytics_data` folder and compressed in `gz` format.
 IF don't want to store the compressed version and just need Json file,  set `compressed = False`.


##### Because I'm working on a project which collect our App data from the Localytics and them import them to our Data WareHouse , I'm working on this Library and If I see some global features which is useful for others, I'll add it.
