#include <iostream>

using namespace std;
int main()
{
    int t,swapc=0;
    cin >> t;
    int d[t];
    for (int i = 0; i < t; i++)
    {
        cin >> d[i];
    }
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < t - 1; j++)
        {
            if (d[j] > d[j + 1])
            {
                swap(d[j], d[j + 1]);
                swapc++;
            }
        }
        if (swapc == 0)
        {
            break;
        }
        }
        cout << "Array is sorted in " << swapc << " swaps." << endl;
        cout << "First Element: " << d[0] << endl;
        cout << "Lasts Element: " << d[t - 1] << endl;


    for (int i = 0; i < t; i++)
    {
       cout << d[i];
    }
    return 0;
}