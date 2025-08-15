
d_1 = {
    "articles": [
        {
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
                "username": "jake",
                "bio": "I work at statefarm",
                "following": False
            }
        },
        {
            "slug": "and another article",
            "body": "I’m getting bored",
            "tagList": ["bored", "article"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 20,
            "author": {
                "username": "cap",
                "following": True
            }
        }
    ],
    "tweets": [
        {
            "body": "See my article on training mules.",
            "author": {
                "username": "jake"
            }
        }
    ]
}


# def get_types(dit):
#     list=[]

#     for i in dit:
#         list.append(i)

#     return list

# print(get_types(d))


def get_types_counts(d):
    result={}
    for i in d:
        count=0
        key=d[i]
        for y in key:
            if isinstance(y,dict):
                count+=1
        result[i]=count
    return result




def get_author_count(d,authorName):
    count=0
    for i in d:
        dit=d[i]
        for y in dit:
            if "author" in y:
                author=y['author']
                for z in author:
                    if author[z]==authorName:
                        count+=1
    return (count)
                    

