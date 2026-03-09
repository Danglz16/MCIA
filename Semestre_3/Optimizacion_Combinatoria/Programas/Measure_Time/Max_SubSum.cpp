#include <iostream>
#include <time.h>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <fstream>
#include <ctime>

using namespace std;

int maxSubSum1( const vector<int> & a )
{
    int maxSum = 0;
    for( int i = 0; i < a.size( ); i++ )
        for( int j = i; j < a.size( ); j++ )
        {
            int thisSum = 0;
            for( int k = i; k <= j; k++ )
                thisSum += a[ k ];
            if( thisSum > maxSum )
                maxSum = thisSum;
        }
    return maxSum;
}

int maxSubSum2( const vector<int> & a )
{
    int maxSum = 0;
    for( int i = 0; i < a.size( ); i++ )
    {
    int thisSum = 0;
        for( int j = i; j < a.size( ); j++ )
        {
            thisSum += a[ j ];
            if( thisSum > maxSum )
                maxSum = thisSum;
        }
    }
    return maxSum;
}

int MaxSumRec( const vector<int> & a, int left, int right )
{
    if( left == right ) // Base case
        if( a[ left ] > 0 )
            return a[ left ];
        else
    return 0;
    int center = ( left + right ) / 2;
    int maxLeftSum = MaxSumRec( a, left, center );
    int maxRightSum = MaxSumRec( a, center + 1, right);
    int maxLeftBorderSum = 0, leftBorderSum = 0;
    
    for( int i = center; i >= left; i-- )
    {
        leftBorderSum += a[ i ];
        if( leftBorderSum > maxLeftBorderSum )
        maxLeftBorderSum = leftBorderSum;
    }
    int maxRightBorderSum = 0, rightBorderSum = 0;
    for( int j = center + 1; j <= right; j++ )
    {
        rightBorderSum += a[ j ];
        if( rightBorderSum > maxRightBorderSum )
        maxRightBorderSum = rightBorderSum;
    }
    return max({maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum});
}

int MaxSubSum3( const vector<int> & a )
{
 return MaxSumRec( a, 0, a.size( ) - 1 );
}
int maxSubSum4( const vector<int> & a )
{
 int maxSum = 0, thisSum = 0;
 for( int j = 0; j < a.size( ); j++ )
 {
 thisSum += a[ j ];
 if( thisSum > maxSum )
 maxSum = thisSum;
 else if( thisSum < 0 )
 thisSum = 0;
 }
 return maxSum;
}

int maxSubSum5(const vector<int>& a) {
    int best = 0;
    int cur  = 0;
    for (int x : a) {
        cur = max(0, cur + x);
        best = max(best, cur);
    }
    return best;
}

int main ()
{
    srand((unsigned)time(nullptr));

    const int n = 20000;
    vector<int> a( n );

    for( int i = 0; i < n; i++ )
        a[ i ] = rand() % 200 - 100;

    clock_t start, finish;
    long double t0;

    ofstream file("resultados.txt", ios::app);

    if (!file) {
        cout << "Error al abrir el archivo" << endl;
        return 1;
    }

    cout << "With " << n << " elements" << endl;
    file << "\nWith " << n << " elements" << endl;

    // maxSubSum1
    start = clock();
    int r = maxSubSum1(a);
    finish = clock();
    t0 = ((long double)(finish - start)) / CLOCKS_PER_SEC;

    cout << "The maximum sum 1 is " << r << endl;
    cout << "Time taken: " << t0 << " seconds\n" << endl;

    file << "The maximum sum 1 is " << r << endl;
    file << "Time taken: " << t0 << " seconds\n" << endl;

    // maxSubSum2
    start = clock();
    r = maxSubSum2(a);
    finish = clock();
    t0 = ((long double)(finish - start)) / CLOCKS_PER_SEC;

    cout << "The maximum sum 2 is " << r << endl;
    cout << "Time taken: " << t0 << " seconds\n" << endl;

    file << "The maximum sum 2 is " << r << endl;
    file << "Time taken: " << t0 << " seconds\n" << endl;

    // maxSubSum3
    start = clock();
    r = MaxSubSum3(a);
    finish = clock();
    t0 = ((long double)(finish - start)) / CLOCKS_PER_SEC;

    cout << "The maximum sum 3 is " << r << endl;
    cout << "Time taken: " << t0 << " seconds\n" << endl;

    file << "The maximum sum 3 is " << r << endl;
    file << "Time taken: " << t0 << " seconds\n" << endl;

    // maxSubSum4
    start = clock();
    r = maxSubSum4(a);
    finish = clock();
    t0 = ((long double)(finish - start)) / CLOCKS_PER_SEC;

    cout << "The maximum sum 4 is " << r << endl;
    cout << "Time taken: " << t0 << " seconds\n" << endl;

    file << "The maximum sum 4 is " << r << endl;
    file << "Time taken: " << t0 << " seconds\n" << endl;

    // maxSubSum5
    start = clock();
    r = maxSubSum5(a);
    finish = clock();
    t0 = ((long double)(finish - start)) / CLOCKS_PER_SEC;

    cout << "The maximum sum 5 is " << r << endl;
    cout << "Time taken: " << t0 << " seconds\n" << endl;

    file << "The maximum sum 5 is " << r << endl;
    file << "Time taken: " << t0 << " seconds\n" << endl;

    file.close();
}