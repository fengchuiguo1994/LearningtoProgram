#include <iostream>
#include <time.h>
using namespace std;
int main(){
    clock_t start = clock();
    int num = 1000;
    int total = 0;
    for(int i=1;i<num;i++){
        if(i%3 == 0 || i%5==0){
            total += i;
        }
    }
    cout << total << endl;
    clock_t finish = clock();
    double consumeTime = (double)(finish-start)/CLOCKS_PER_SEC;
    cout << "use time" << consumeTime << "s" << endl;
    return 0;
}
