from WriteInterFace import IWrite

class Write(IWrite):
    def write_to_file(self, words):
        self.words = words
        with open('Encrypted file.txt', 'a') as e:
            e.write(self.words)

    def upload_to_git_hub(self):
        pass

if __name__ == "__main__":
    fw = Write()
    fw.write_to_file("test")
