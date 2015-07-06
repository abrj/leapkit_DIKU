from scraper import Scraper


class SkillExtractor(Scraper):
    """
    Class used to extract profile information from the public profile of
    LinkedIn users.
    """

    def __init__(self):
        self.headers = {
            'User-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'
        }

    def scrape_skills(self, linked_url):
        """
        Method used to extract the skills of a public LinkedIn profile
        """

        soup = self.scrape(linked_url)

        skills = []
        if soup:
            skills = [skill.string for skill in
                      soup.find_all("a", {"class": "endorse-item-name-text"})]

        return skills

    def scrape_picture(self, linked_url):
        """
        Medthod used to extract the profile picture of a public LinkedIn
        profile.
        """

        soup = self.scrape(linked_url)

        image_url = ""
        image_div = soup.find("div", {"class": "profile-picture"})
        if image_div:
            image = image_div.find("img")
            image_url = image["src"]

        return image_url
