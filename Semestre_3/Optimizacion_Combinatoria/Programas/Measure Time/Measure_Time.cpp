#include <iostream>
#include <time.h>
#include "insort.h"

using namespace std;
int main(void)
{ //Program 2.31
int a[100000], step = 10000;
clock_t start, finish;
long double t0,t1;
cout << "CLOCKS PER SECOND: " << CLOCKS_PER_SEC<< endl;
for (int n = step; n <= 100000; n += step) {
for (int i = 0; i < n; i++) a[i] = n - i; // initialize
start = clock( );
InsertionSort(a, n);
finish = clock( );
t0= (finish - start); t1= t0/ CLOCKS_PER_SEC;
cout << "# of cycles: " << t0 << "; Running-time: " << t1 << "secs." << endl << endl;
}
}