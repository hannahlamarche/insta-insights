import click

from insta_scraper import fetch_report_details


@click.command()
@click.option("--username", required=True)
def main(username: str):
    fetch_report_details(username)


if __name__ == "__main__":
    main()
