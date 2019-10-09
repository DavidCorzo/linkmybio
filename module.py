import yaml
import datetime


def check_dates(end_date):
    end_date = datetime.date(end_date[0], end_date[1], end_date[2])
    now = datetime.date.today()
    if now <= end_date:
        return True
    else:
        return False


def open_master(filename='info.yml'):
    with open(filename, mode='r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f'{exc} error on opening yml')
