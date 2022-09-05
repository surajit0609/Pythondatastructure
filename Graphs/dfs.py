visited={}
def dfs(current):
    visited[current]=1
    print(current)
    for chiled in g[current]:
        if chiled not in visited.keys():
            dfs(chiled)
g={"jhargram":["kharagpur",'medinipur'],
    'kharagpur':["jhargram","medinipur","kolkata"],
    "medinipur":["kharagpur","jhargram"],
    "kolkata":["kharagpur"]}
if __name__ == '__main':

dfs(jhargram)