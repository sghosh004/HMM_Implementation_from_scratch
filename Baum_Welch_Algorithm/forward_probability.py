def cal_forward_probability(sequence, transition_matrix, emission_matrix, initial_probability):
  forward_probability=[]
  for i in range(0,len(sequence)): # time stamp
    prob=[]
    for j in range(len(initial_probability)): #no of states
      if(i==0):
        temp_prob=initial_probability[j]*emission_matrix[j][sequence_syms[sequence[0]]]
      else:
        temp_prob=sum([forward_probability[i-1][k]*transition_matrix[k][j]*emission_matrix[j][sequence_syms[sequence[i]]] for k in range(len(initial_probability))])
      prob.append(temp_prob)
    forward_probability.append(prob)

  return forward_probability
