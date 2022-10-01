#include <iostream>
#include <vector>
using namespace std;

template<typename T>
bool isSame(std::vector<T> const &v){
    for (int i = 1; i < v.size(); i++) {
        if (v[0] != v[i]){
            return false;
        }
    }
    return true;
}

int test(){
    int n;
    int day = 0;
    int max = 0;
    cin >> n  ;
    vector<int> v(n);
    for (int i=0; i<n ; i++){
        cin >> v[i];
    }
    bool same = isSame(v);
    for (int i=0; i<=n ; i++){
        if (same == true){
            day = 0;
            break;
        }

        if ((day==0) && (i == v.size())){
            day += 1;
            break;
        }
        
        if ((v[i+1] > v[i]) && (max < v[i+1]) && (v[i+1]< v.size())){
            max = v[i+1];
            day += 1;
        }
        
    }
    return day;
}

int main(){
    int t;
    cin >> t;
    for (int i = 1 ; i<=t ; i++){
        cout << "Case #" << i << ": "<<test()<<"\n";
    }
    return 0;
}