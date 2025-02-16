class Write:
    def write_to_file(self, words):
        self.words = words
        with open('Encrypted file.txt', 'a') as e:
            e.write(self.words)

    def upload_to_git_hub(self):
        pass


