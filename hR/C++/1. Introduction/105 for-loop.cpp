//https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int x,y;
    cin>>x>>y;
    string num[12] = {"even","one","two","three","four","five","six","seven","eight","nine","odd"};
    for(int i = x; i <= y; ++i){
        if(i>9){
            if(i%2==0){
                cout << "even\n" ;
            }
            else{
                cout << "odd\n";
            }
        }
        else{
            cout<<num[i]<<endl;
        }
    }
    
    return 0;
}