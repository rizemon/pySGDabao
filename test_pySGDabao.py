from pySGDabao import *

def main():
    postal_code = 760625
    test_foodpanda, test_deliveroo, test_honestbee = Foodpanda(postal_code), Deliveroo(postal_code), Honestbee(postal_code)
    print(test_foodpanda.parse_listing())
    print(test_deliveroo.parse_listing())
    print(test_honestbee.parse_listing())
    

if __name__ == "__main__":
    main()