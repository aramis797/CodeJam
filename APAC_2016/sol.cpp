#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<cmath>
#include<iomanip>
#include<cstdlib>
#include<sstream>
#include<climits>
#include<cassert>
#include<time.h>

using namespace std;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define pb push_back
#define ss second
#define ff first
#define vi vector<int>
#define vl vector<ll>
#define s(n) scanf("%d",&n)
#define ll long long
#define mp make_pair
#define PII pair <int ,int >
#define PLL pair<ll,ll>
#define inf 1000*1000*1000+5
#define v(a,size,value) vi a(size,value)
#define sz(a) a.size()
#define all(a) a.begin(),a.end()
#define tri pair < int , PII >
#define TRI(a,b,c) mp(a,mp(b,c))
#define xx ff
#define yy ss.ff
#define zz ss.ss
#define in(n) n = inp()
#define vii vector < PII >
#define vll vector< PLL >
#define viii vector < tri >
#define vs vector<string>
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end());
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define ok if(debug)
#define trace1(x) ok cerr << #x << ": " << x << endl;
#define trace2(x, y) ok cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)    ok      cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)  ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
                                << #d << ": " << d << endl;
#define trace5(a, b, c, d, e) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
                                     << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
                                    << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)
ll MOD = int(1e9) + 7;

int debug = 0;
const int N = int(1e6) + 5;
using namespace std;
string a[105];
int r,c,vis[105][105];
int dx[] = {-1,0,1,0},dy[] = {0,1,0,-1};
void dfs(int x,int y)
{
        trace3(x,y,int(a[x][y]));
        if(a[x][y] == ' ' || a[x][y] == '0' || vis[x][y])
                return;
        int i;
        vis[x][y] = 1;
        rep(i,4)
        {
                dfs(x+dx[i],y+dy[i]);
        }
}
int query()
{
        int i,j,ret = 0;
        memset(vis,0,sizeof(vis));
        f(i,1,r+1)
        {
                f(j,1,c+1)
                {
                        if(vis[i][j] || a[i][j] == '0')
                                continue;
                        ret++;
                        dfs(i,j);
                }
        }
        return ret;
}
int main()
{
        int i,j,n,t;
        ios::sync_with_stdio(false);
        cin>>t;
        int t1 = t;
        while(t--)
        {
                cin>>r>>c;
                a[0] = a[r+1] = string(c+2,'0');
                rep(i,r)
                {
                        cin>>a[i+1];
                        a[i+1] = "0" + a[i+1] + "0";
                }
                f(i,0,r+2)trace1(a[i]);
                int q;
                cin>>q;
                cout<<"Case #"<<t1-t<<": "<<endl;
                while(q--)
                {
                        char type;
                        cin>>type;
                        if(type == 'Q')
                        {
                                cout<<query()<<endl;
                        }
                        else
                        {
                                int l,r,val;
                                cin>>l>>r>>val;
                                a[l+1][r+1] = '0' + val;
                        }
                }
        }
}
 