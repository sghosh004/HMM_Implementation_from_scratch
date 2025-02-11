def cal_backward_probability(sequence, transition_matrix, emission_matrix, initial_probability):
  backward_probability=[[1]*len(initial_probability)]
  for i in reversed(range(len(sequence)-1)): # timestamp
    prob=[]
    for j in range(len(initial_probability)): #no of states
      temp=sum([backward_probability[0][k]*transition_matrix[j][k]*emission_matrix[k][sequence_syms[sequence[i+1]]] for k in range(len(initial_probability))])
      prob.append(temp)
    backward_probability.insert(0, prob)

  return backward_probability