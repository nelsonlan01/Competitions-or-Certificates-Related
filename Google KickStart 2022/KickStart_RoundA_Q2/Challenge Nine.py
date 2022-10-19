def check_div_9(new_num):
    if new_num % 9 == 0:
        return True
    return False

def clear_queue():
    queue9.clear()
    sorted_queue.clear()

queue9 = []
sorted_queue = []

T = int(input())

for t in range(T):
    num = input()
    for pre in range(0,10):
        new_num_max = int(str(num) + str(pre))  #add to rear
        if (check_div_9(new_num_max)) == True:
            queue9.append(new_num_max)
        new_num_min = int(str(pre) + str(num))  #add to front
        if (check_div_9(new_num_min)) == True:
            queue9.append(new_num_min)
    sorted_queue = sorted(queue9)
    print("Case #%d: %d" % (t + 1, sorted_queue[0]))
    clear_queue()
    
    
    //Answer in c++ code
    
// L SHAPED PLOTS
// TIME COMPLEXITY:- O(R*C)
// SPACE COMPLEXITY:- O(R*C)

#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define ll long long
#define vi vector<ll>
#define pb push_back
#define F first
#define S second
#define all(v) (v).begin(),(v).end()
#define pii pair<ll,ll>
#define vii vector<pii>
#define calc_fact(n) tgamma(n+1)
#define inf LONG_LONG_MAX
#define MOD 1000000007
#define mod 998244353

// this function returs the total number of L shape plots possible

ll get_ans(ll hor,ll vert)
{
    if(hor==1 or vert==1)return 0;
    
    ll ans = min(hor,vert/2);
    ans--;
    
    ans+=min(vert,hor/2);
    ans--;
    
    return ans;
}

ll solve()
{
    ll n,m;
    cin>>n>>m;
    
    // original matrix
    vector<vi> mat(n,vi(m,0));

    // four matrices
    vector<vi> up(n,vi(m,0));
    vector<vi> down(n,vi(m,0));
    vector<vi> left(n,vi(m,0));
    vector<vi> right(n,vi(m,0));
    
    for(ll i=0;i<n;i++)
    {
        for(ll j=0;j<m;j++)cin>>mat[i][j];
    }
    
    // calculate for each cell
	// in four directions
	// number of consecutive cells ending here
    for(ll j=0;j<m;j++)
    {
        for(ll i=0;i<n;i++)
        {
            if(!mat[i][j])continue;
            
            down[i][j]++;
            if(i>0)down[i][j]+=down[i-1][j];
        }
    }
    
    for(ll j=0;j<m;j++)
    {
        for(ll i=n-1;i>=0;i--)
        {
            if(!mat[i][j])continue;
            
            up[i][j]++;
            if(i+1<n)up[i][j]+=up[i+1][j];
        }
    }
    
    for(ll i=0;i<n;i++)
    {
        for(ll j=0;j<m;j++)
        {
            if(!mat[i][j])continue;
            
            right[i][j]++;
            if(j>0)right[i][j]+=right[i][j-1];
        }
    }
    
    for(ll i=0;i<n;i++)
    {
        for(ll j=m-1;j>=0;j--)
        {
            if(!mat[i][j])continue;
            
            left[i][j]++;
            if(j+1<m)left[i][j]+=left[i][j+1];
        }
    }
    
    ll ans = 0;
    
    for(ll i=0;i<n;i++)
    {
        for(ll j=0;j<m;j++)
        {
            if(!mat[i][j])continue;
            
            ans+=get_ans(left[i][j],down[i][j]);
            ans+=get_ans(left[i][j],up[i][j]);
            ans+=get_ans(right[i][j],down[i][j]);
            ans+=get_ans(right[i][j],up[i][j]);
        }
    }
    
    return ans;
}

signed main()
{
	FIO;

	ll t;
	cin>>t;
	for(ll i=1;i<=t;i++)
	{
	    cout<<"Case #"<<i<<": ";
	    
	    cout<<solve()<<endl;
	}
	
}
