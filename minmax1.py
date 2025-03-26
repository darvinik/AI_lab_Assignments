import math

def minimax(node,depth,is_maximizing,values,path):
    if depth==0 or node not in values:
        return values.get(node,math.inf),[node]
    
    if is_maximizing:
        best_value=-math.inf
        best_path=[]
        for child in values[node]:
            val,p=minimax(child,depth-1,False,values,path)
            if val>best_value:
                best_value,best_path=val,[node]+p
        return best_value,best_path
    else:
        best_value=math.inf
        best_path=[]
        for child in values[node]:
            val,p=minimax(child,depth-1,True,values,path)
            if val<best_value:
                best_value,best_path=val,[node]+p
        return best_value,best_path

fig1={
    'A':['B1','B2','B3'],
    'B1':['C1','C2','C3'],
    'B2':['C4','C5','C6'],
    'B3':['C7','C8','C9'],
    'C1':12,'C2':10,'C3':3,
    'C4':5,'C5':8,'C6':10,
    'C7':11,'C8':2,'C9':12
}

opt_value1,opt_path1=minimax('A',2,True,fig1,[])
print("Optimal value for Figure 1:",opt_value1)
print("Optimal path for Figure 1:"," -> ".join(opt_path1))