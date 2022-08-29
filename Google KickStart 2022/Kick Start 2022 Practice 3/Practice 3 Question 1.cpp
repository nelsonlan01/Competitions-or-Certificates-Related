#include <iostream>
#include <vector>

using namespace std;

int test(){
    int n, m;
    cin >> n >> m ;
    vector<int> v(n);
    for (int i=0; i<n ; i++){
        cin >> v[i];
    }
    int sum = 0;
    for (int i = 0; i<n;i++){
        sum += v[i];
    }
    return sum%m;
}

int main(){
    int t;
    cin >> t;
    
    for (int i = 1 ; i<=t ; i++){
        cout << "Case #" << i << ": "<<test()<<"\n";
    }
    return 0;
}
