import requests



def get_post_tags(post_id):
    # Your code here
    # lo mismo de siempre: 
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response = requests.get(url)    
    data = response.json()
    # primero accedo a los posts y creo una lista vacía
    posts = data['posts']
    tags_list = []

    # ahora loopeo la lista de todos los posts para encontrar el que quiero
    for i in range(len(posts)):
        # comparo el id del post en el que estoy iterando con el post_id introducido en la función
        if posts[i]["id"] == post_id:
            # cuando coincidan los post id's, quiero acceder a los tags de ese post
            tags = posts[i]['tags']
            # por último, añado los tags a la lista de tags del post
            for tag in tags:
                tags_list.append(tag['title'])
            return tags_list
    


print(get_post_tags(146))