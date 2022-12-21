#include <iostream>
#include <vector> 

using namespace std;

#define MAX 100000

bool prime[MAX+1];
vector <int> p;

int prime_sieve(){
    for (int i=0; i<=MAX; i++){
        prime[i] = 1;
    }
	prime[0] = prime[1] = 0;
	p.clear();
	
	for(int i=2; i*i<=MAX; i++){
        if(prime[i]){
            for(int j=i*i; j<=MAX; j+=i){
                prime[j] = 0;
            }
        }

    }

	for(int i = 0; i<=MAX; i++){
		if(prime[i]){
            p.push_back(i);
        }
	}

    return p.size();
}

int main(){
    int prime_cnt;
    prime_cnt = prime_sieve();
    cout <<"The output is: " <<prime_cnt << endl;
    return 0;
}