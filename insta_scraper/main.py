import click

from insta_scraper import fetch_report_details


@click.command()
@click.option("--username", help="Your Instagram username", required=True)
@click.option("--password", help="Your Instagram password", required=True)
def main(username: str, password: str):
    fetch_report_details(username, password)


if __name__ == "__main__":
    main()
