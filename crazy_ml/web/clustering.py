




            
# set the number of clusters
def how_many_clusters(no_users):

    return round(no_users**(1/3))


# kmeans clustering
def kmeans(no_clusters, data):

    return KMeans(n_clusters=no_clusters, random_state=0).fit_transform(data)


# for each cluster make the pearson correlation on their scores
def make_map(users, k_means):
    
    user_map = {}
    k = np.frombuffer(k_means)
    k = k.transpose()
    # for all keys in k -> values 
    zipped = zip(k, users)
    for label, user in zipped:
        if label not in user_map:
            user_map[label] = []
        user_map[label].append(user)   
    return user_map
        

def main_f(users, tags):
    no_users = len(users)
    data = make_vectors(users, tags)
    no_clusters = how_many_clusters(no_users)
    k_means = kmeans(no_clusters, data)
    user_map = make_map(users, k_means)
    return user_map
    
    
# new function with events
    # events = list of events
    # scores = 2D list of scores for each event
    # for line in scores:
    #   calculate mean from the whole event
    #
    