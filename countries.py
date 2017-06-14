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

    click.echo(response)
    click.echo(response.text)

if __name__ == '__main__':
    country()
