def xi_prob(forward, backward, transition_matrix, emission_matrix):
  prob=np.zeros((len(forward)-1, len(transition_matrix),len(transition_matrix)))
  forward_val=sum(forward[-1])
  for i in range(len(forward)-1):
    temp=[]
    for j in range(len(transition_matrix[0])):
      temp1=[forward[i][j]*transition_matrix[j][k]*emission_matrix[k][sequence_syms[sequence[i]]]*backward[i+1][k] for k in range(len(emission_matrix[0]))]
      temp.append(temp1)
    prob[i]=temp
  prob=prob/forward_val
  return prob
