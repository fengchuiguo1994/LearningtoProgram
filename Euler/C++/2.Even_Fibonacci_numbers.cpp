#include <iostream>
#include <time.h>
using namespace std;
int main(){
    clock_t start = clock();
    int i = 1;
    int j = 2;
    int total = 2;
    while(j < 4000000){
        int tmp = j;
        j = i+j;
        i = tmp;
        if(j%2 == 0){
            total += j;
        }
    }
    cout << "the total is " << total << endl;
    clock_t finish = clock();
    double consumeTime = (double)(finish-start)/CLOCKS_PER_SEC;
    cout << "use time" << consumeTime << "s" << endl; 
    return 0;
}