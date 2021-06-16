class Test:
    def __init__(self,url) -> None:
        self.url = url


    def self_print(self):
        print(self.url)

def main():
    x = Test("helllo")
    x.self_print()
if __name__ == '__main__':
    main()
    