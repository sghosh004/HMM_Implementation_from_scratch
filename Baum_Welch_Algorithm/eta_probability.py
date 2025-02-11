def eta_prob(forward, backward):
  prob=np.zeros((len(forward), len(forward[0])))
  denominator=np.sum(np.multiply(forward,backward))
  for i in range(len(forward)):
    temp=[forward[i][k]*backward[i][k] for k in range(len(forward[1]))]
    prob[i]=temp
  return prob