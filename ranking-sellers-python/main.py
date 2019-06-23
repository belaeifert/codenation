from operator import itemgetter
from more_itertools import sort_together

class SellersRancking:
    def best_seller(self, sellers):
        #return [seller["name"] for seller in sellers if]
        max_value = 0
        best_seller = []
        for seller in sellers:
            if seller["value"] > max_value:
                max_value = seller["value"]
                best_seller = [seller["name"]]
            elif seller["value"] == max_value:
                best_seller.append(seller["name"])
        return best_seller


    def rancking_list(self, sellers):
        ranking_sellers = sorted(sellers, key=lambda x: x.get("value"), reverse=True)
        return [seller["name"] for seller in ranking_sellers]

    def best_seller_store(self, sellers, store):
        store_sellers = list(filter(lambda x: x.get("store") == store, sellers))
        return self.best_seller(store_sellers)

    def sales_goals(self, sellers):
        seller_bellow_target = list(filter(lambda x: x.get("value") < 500, sellers))
        seller_bellow_target.sort(key=lambda x: x.get("value"))
        return [seller["name"] for seller in seller_bellow_target]

