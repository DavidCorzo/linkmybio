import yaml


def check_dates():
    pass


def open_master(filename='info.yml'):
    with open(filename, mode='r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f'{exc} error on opening yml')
