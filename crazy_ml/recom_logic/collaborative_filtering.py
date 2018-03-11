def pearson_correlation(x, y):

	x = (x - np.mean(x)) / np.std(x)
	y = (y - np.mean(y)) / np.std(y)

	return np.dot(x, y) / len(x)

def event_score(user, sim_users, event):

	return np.mean([user_sim[(user, u)] * score[(u, event)] for u in sim_users]) 