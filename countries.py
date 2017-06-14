import click, requests, json

@click.command()
@click.option('--country', prompt='Enter Country\'s two character code',
              help='Name of county to lookup Information')
def country(country):
    """Simple program that takes as an argument
    a country's two character code  and returns more info.
    """
    url = 'http://services.groupkt.com/country/get/iso2code/{0}'.format(country)
    response = requests.get(url)
    res = json.loads(response.text)
    mess = 'That Country\'s full name is {0} \n It\'s alpha3_code is {1}'.format(res['RestResponse']['result']['name'], res['RestResponse']['result']['alpha3_code'])
    click.echo(mess)

if __name__ == '__main__':
    country()
