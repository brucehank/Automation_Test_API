import json
import jsonpath_ng
import sys
from Utils.HttpClient import *
from Utils.Log import *

log = Log()
        
class Pokemon(object):

    def __init__(self) -> None:
        self.httpclient = HttpClient()

    def get_pokemon_data(self, id):  #  獲取 API Response Data
        # Make a GET request to the Pokemon API
        response = self.httpclient.request(requestMethod="get", requestUrl=f"https://pokeapi.co/api/v2/pokemon/{id}/",
                                           paramsType="url")

        # Ensure that the response is successful
        if response.status_code == 200:
            # Convert the Response object to a string
            res_json = response.text

            # Parse JSON
            pokemon_data = json.loads(res_json)

            return pokemon_data
        else:
            print(f"Error, status code: {response.status_code}")
            return None

    def get_json_data(self, data, queries):  #  獲取 json 查詢的資料
        # Get data from JSON using jsonpath queries
        results = {}

        for query in queries:
            json_query = jsonpath_ng.parse(query)
            matches = [match.value for match in json_query.find(data)]
            results[query] = matches[0] if matches else None

        return results

    def display_results(self, results):  #  輸出顯示資料結果
        # Display the results
        for query, value in results.items():
            if value is not None:
                print(f"{query}: {value}")
            else:
                print(f"Data not found for query: {query}")

    def get_pokemon_info(self, id, queries):  #  獲取指定 json 查詢資料並顯示
        # Get Pokemon data
        pokemon_data = self.get_pokemon_data(id)

        if pokemon_data:
            # Get JSON data based on queries
            results = self.get_json_data(pokemon_data, queries)

            # Display the results
            self.display_results(results)

            return results
        else:
            return None

    def No1(self, id:int) -> None:  #  透過 id 找 寶可夢 name
        #  paramaters:  id: 寶可夢 id
        #  return:   列出 id 的寶可夢資料

        pokemon_id = id
        json_queries = ['$[id]', '$[name]']

        # Get and display Pokemon info
        results = self.get_pokemon_info(pokemon_id, json_queries)
            
    def No2(self, id_range:int) -> None:  #  透過 id 找 寶可夢 name and types
        #  paramaters:  id_range: 寶可夢 id
        #  return:   列出 id 為 1 ~ id_range 的寶可夢資料

        #  查詢 json 資料
        json_queries = ['$[id]', '$[name]', '$[types]']

        for id in range(1, id_range + 1):
            pokemon_id = id

            # Get and display Pokemon info
            results = self.get_pokemon_info(pokemon_id, json_queries)

    def No3(self, id_range:int) -> None:  #  透過 id 找 寶可夢 name and weight
        #  paramaters:  id_range: 寶可夢 id
        #  return:   列出 id 為 1 ~ id_range 的寶可夢資料

        #  體重小於50的資料存放
        weight_less_50 = {}
        #  查詢 json 資料
        json_queries = ['$[id]', '$[name]', '$[weight]']

        #  打API拿體重小於50的資料
        for id in range(1, id_range + 1):

            # Get Pokemon data
            pokemon_data = self.get_pokemon_data(id)

            if pokemon_data:
                # Get JSON data based on queries
                results = self.get_json_data(pokemon_data, json_queries)
            
                if results['$[weight]'] < 50:
                    weight_less_50[id] = results

        # 按照體重降序對 weight_less_50 進行排序
        sorted_weight_less_50 = dict(sorted(weight_less_50.items(), key=lambda x: x[1]['$[weight]'], reverse=True))

        # 印出每個 Key 的 Value
        for key, value in sorted_weight_less_50.items():
            print(f"{value}")

