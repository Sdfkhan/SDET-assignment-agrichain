class HomePage:
    def __init__(self, page):
        self.page = page
        self.input_box = "#input-string"
        self.submit_button = "#submit-btn"

    def enter_text(self, text):
        self.page.fill(self.input_box, text)

    def submit(self):
        self.page.click(self.submit_button)
