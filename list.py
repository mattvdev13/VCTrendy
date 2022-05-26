

from logging import exception


class VClist:
    def __init__(self, location):
        self.location = location
        reader = open(location, 'r')
        try:    
            self.namedList= reader.read().splitlines()
        except:
            print("Error")
            exit
        finally:
            reader.close()

    def listlength(self):
        self.listlength = len(self.namedList)
        return self.listlength

    def add_to_list(self, username):
        #checkusername function
        self.namedList.append(username)
        return self.namedList

    def remove_from_list(self, username):
        #checkusername function
        self.namedList.remove(username)
        return self.namedList

    def write_to_file(self):
        writer = open(self.location, 'w')
        writer.write(self.namedList.copy())
        writer.close()
        return self.namedList

def main():
    test = VClist('/Users/matt/Desktop/VCTrendy/list.txt')
    print(test.listlength())
    print("Completed!")

if __name__== "__main__":
    main()
    
