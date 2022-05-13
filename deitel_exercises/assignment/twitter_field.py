from functools import reduce
fields = [
    {"username": "Adesoba Samson", "age": 30, "verified": True, "tweets": ["I'm rich",
                                                                           "I'm bless",
                                                                           "I'm successful"
                                                                           "I'm handsome"
                                                                           ]},
    {"username": "Adewale Joseph", "age": 25, "verified": False, "tweets": ["fuck off",
                                                                            "She is a bitch",
                                                                            "She is lazy",
                                                                            "She is cumming",
                                                                            "See my life"
                                                                            ]},
    {"username": "Adesola Solomon", "age": 19, "verified": True, "tweets": []},
    {"username": "Bayo Joshua", "age": 28, "verified": False, "tweets": ["Elon musk just bought twitter",
                                                                         "Just coming from home",
                                                                         "Always enter my DM"
                                                                         ]},
    {"username": "Titi Goke", "age": 18, "verified": False, "tweets": ["Why",
                                                                       "Glory be to God"
                                                                       ]},
    {"username": "Tayo Femi", "age": 20, "verified": True, "tweets": ["Me",
                                                                      "Python class"]},
    {"username": "Ajala Ebenezer", "age": 90, "verified": True, "tweets": []},
    {"username": "Ife Titi", "age": 25, "verified": False, "tweets": []},
    {"username": "Andrew Foluke", "age": 46, "verified": False, "tweets": ["Always",
                                                                           "On the",
                                                                           "Move"
                                                                           ]},
    {"username": "Usman Chibuzor", "age": 70, "verified": True, "tweets": []}
]
verified_users = [field["username"] for field in fields if field["verified"] == True]
active_users = [field["username"] for field in fields for tweets in field["tweets"]]
users_below_25_and_verified = [field["username"] for field in fields if field["age"] < 25 if field["verified"] == True ]
users_age = list(field["age"] for field in fields)
users_max_age = max(users_age)
users_min_age = min(users_age)
user_ave = (reduce(lambda x, y: x+y, users_age))/len(fields)
user_ascending_order = sorted(fields, key=lambda field: field["username"])
user_descending_order = sorted(fields, key=lambda field: field["username"], reverse=True)
user_longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, list(field["username"] for field in fields))
tweets = list(field["tweets"] for field in fields)
tweets_2 = max(fields, key=lambda user: len(user["tweets"]))
user_with_most_tweets = max(tweets)

print(verified_users)
print(list(dict.fromkeys(active_users)))
print(list(dict.fromkeys(users_below_25_and_verified)))
print(users_max_age)
print(users_min_age)
print(user_ave)
print(user_ascending_order)
print(user_descending_order)
print(user_longest_name)
print(tweets)
print(user_with_most_tweets)
print(tweets_2)

