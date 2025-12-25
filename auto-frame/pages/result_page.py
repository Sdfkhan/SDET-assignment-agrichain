class ResultPage:
    def __init__(self, page):
        self.page = page
        self.output_text = "#output"
        self.back_button = "#back-home"

    def get_output(self):
        return self.page.text_content(self.output_text)

    def go_back(self):
        self.page.click(self.back_button)
