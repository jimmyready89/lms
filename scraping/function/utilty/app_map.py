class AppMap:
    url = {
        "newbinusmaya.binus.ac.id": {
            "Code": "LMS",
            "URL": "https://newbinusmaya.binus.ac.id"
        },
        "login.microsoftonline.com": {
            "Code": "Login",
            "URL": "https://login.microsoftonline.com"
        }
    }

    def getURL(self, domain: str) -> dict:
        return self.url[domain]
