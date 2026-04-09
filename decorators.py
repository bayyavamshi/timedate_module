# def hello_world(ajay):
#     def vamshi():
#         print("hii vamshi")
#         ajay()
#         print('when your are coming to my village')
#     return vamshi
# @hello_world
# def raju():
#     print("hii sir,")
# raju()


def hii(bab):
    def hlo():
        print('hello')
        bab()
        print('i am sorry')
    return hlo
@hii
def k():
    print('nenu ranu')
k()