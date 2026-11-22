#include <iostream>
using namespace std;
int sum(int a, int b){ return a + b; }
void addOne(int n){ n++; }
int main(){
 { double num1 = 5, num2, s; num2 = 12; s = num1 + num2; cout << "The sum is " << s << "\n"; }
 { int x=3; x=8; cout << x << "\n"; }
 cout << 10 - 4 / 2 * 3 << "\n";
 { int x = 7 / 2.0; char c='A'; cout << x << " " << c + 1 << "\n"; }
 { int x=5; cout << x++ << " "; cout << x << " | "; int y=5; cout << ++y << " | "; int a=3; int b=++a; cout << b << "\n"; }
 { int kira=5; cout << 5 * --kira + 10 << "\n"; }
 { int i=4; i+=3; cout << i << "\n"; }
 { int a=8; if (a>5) { cout << "big "; cout << "number"; } cout << "\n"; }
 { int x=7; if (x<3); cout << "small\n"; }
 { char grade='B'; switch(grade){ case 'A': cout << "Excellent!"; case 'B': cout << "Very good!"; case 'C': cout << "Good"; default : cout << "Fail"; } cout << "\n"; }
 { char grade='Z'; switch(grade){ case 'A': cout << "Excellent!"; break; case 'B': cout << "Very good!"; break; default : cout << "Fail"; } cout << "\n"; }
 for (int i=1;i<=2;i++) for (int j=1;j<=3;j++) cout << i << j << " "; cout << "\n";
 { int s=0,c=1; while(c<=5){ s+=c; c++; } cout << s << " counter-after-10: "; s=0;c=1; while(c<=10){s+=c;c++;} cout << c << "\n"; }
 { int d = sum(3,4)*2; cout << d << " " << (3+4>6 && 2==2) << " "; int x=1; if ((x = 5)) cout << x; cout << " "; int a=7,b=2; double c=a/b; cout << c << " "; int k=4; int m=k++ + 1; cout << m << " "; int kk=9; addOne(kk); cout << kk << " " << 7/3 << " " << 7%3 << "\n"; }
}
