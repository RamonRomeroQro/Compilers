#include <iostream>
using namespace std;
#define a (x+1)

int x =2;

void b(){x = a; cout<< x<< endl;}
void c(){ int x = 1; cout<< a << endl;}

int main(){
    b();
    c();
   return 0;
}
