class Get:
    def entities():
        return ((1024.42,72,-477.12),"player1"),((1654.42,32,-400.22),"player2")

class Print:
    def entities(ents):
        for pos,ent in ents:
            print("POS:",pos,"ENTITY:",ent)

if __name__ == '__main__':
    Print.entities(Get.entities())